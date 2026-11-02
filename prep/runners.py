"""Code execution backends. Each runner compiles+runs C source with one stdin
(plus optional input files) and returns a RunResult; the judge never cares
which backend was used.

    runner.run(source, stdin, time_limit=2.0, memory_limit=65536, files=None)

`files` maps a file name to its text content; the program finds those files
in its working directory (for tasks that read e.g. "znak.txt").
"""
import base64
import logging
import os
import re
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

import requests

log = logging.getLogger(__name__)

OK = "ok"
COMPILE_ERROR = "compile_error"
RUNTIME_ERROR = "runtime_error"
TIMEOUT = "timeout"
INTERNAL_ERROR = "internal_error"


@dataclass
class RunResult:
    status: str
    stdout: str = ""
    stderr: str = ""
    compile_output: str = ""
    time_ms: float | None = None
    message: str = ""


class OnlineCompilerRunner:
    """https://onlinecompiler.io — POST /api/run-code-sync/ with the raw key in Authorization.

    The API compiles with `gcc -O2 code.c -o code.out -lm` (GCC 15) and reports
    compile errors only as a non-zero exit code plus gcc's messages in `error`.
    """

    _COMPILE_ERROR_RE = re.compile(r"^code\.c:\d+:\d+: (fatal )?error:|collect2: error|undefined reference to",
                                   re.MULTILINE)

    def __init__(self, url, key, compiler="gcc-15", http_timeout=40, retries=2, session=None, sleep=time.sleep):
        self.url = url.rstrip("/")
        self.compiler = compiler
        self.http_timeout = http_timeout
        self.retries = retries
        self.session = session or requests.Session()
        self.sleep = sleep
        self.headers = {"Authorization": key, "Content-Type": "application/json"}

    def run(self, source, stdin, time_limit=2.0, memory_limit=65536, files=None):
        payload = {"compiler": self.compiler, "code": source, "input": stdin or "", "time_limit": time_limit}
        if files:
            payload["files"] = [{"name": name, "content": content} for name, content in files.items()]
        try:
            for attempt in range(self.retries + 1):
                resp = self.session.post(f"{self.url}/api/run-code-sync/", json=payload,
                                         headers=self.headers, timeout=self.http_timeout)
                # 429 = our 2 parallel runs are busy or the per-minute limit is hit: back off briefly.
                if resp.status_code != 429 or attempt == self.retries:
                    break
                self.sleep(1.5 * (attempt + 1))
            if resp.status_code == 429:
                return RunResult(INTERNAL_ERROR, message="Kompilátor je preťažený, skúste o chvíľu. / "
                                                         "Компилятор перегружен, попробуйте позже.")
            resp.raise_for_status()
            data = resp.json()
        except (requests.RequestException, ValueError) as exc:
            log.warning("onlinecompiler request failed: %s", exc)
            return RunResult(INTERNAL_ERROR, message=f"Compiler API unavailable: {exc}")

        code = data.get("exit_code")
        out, err = data.get("output", ""), data.get("error", "")
        t = data.get("time")
        time_ms = float(t) * 1000 if t else None
        if code == 0:
            return RunResult(OK, stdout=out, stderr=err, time_ms=time_ms)
        if code == 124:
            return RunResult(TIMEOUT, stdout=out, time_ms=time_ms)
        if code == -1 or code is None:
            return RunResult(INTERNAL_ERROR, message=err or "Run failed on the compiler side")
        if self._COMPILE_ERROR_RE.search(err) and not out:
            return RunResult(COMPILE_ERROR, compile_output=err)
        msg = {137: "Memory limit (512 MB)", 139: "Segmentation fault", 153: "Output limit"}.get(code, "")
        return RunResult(RUNTIME_ERROR, stdout=out, stderr=err, time_ms=time_ms,
                         message=msg or f"Exit code {code}")


class Judge0Runner:
    # https://ce.judge0.com/statuses
    _STATUS = {3: OK, 4: OK, 5: TIMEOUT, 6: COMPILE_ERROR}

    def __init__(self, url, key="", host="", language_id=50, http_timeout=30, session=None):
        self.url = url.rstrip("/")
        self.language_id = language_id
        self.http_timeout = http_timeout
        self.session = session or requests.Session()
        self.headers = {"Content-Type": "application/json"}
        if key:
            self.headers["X-RapidAPI-Key"] = key
            self.headers["X-RapidAPI-Host"] = host or self.url.split("//")[-1]

    def run(self, source, stdin, time_limit=2.0, memory_limit=65536, files=None):
        if files:
            # Judge0 wants extra files as a base64 zip; no task needs that with this backend yet.
            return RunResult(INTERNAL_ERROR, message="Judge0 backend does not support input files")
        payload = {
            "language_id": self.language_id,
            "source_code": _b64(source),
            "stdin": _b64(stdin),
            "cpu_time_limit": time_limit,
            "wall_time_limit": max(time_limit * 3, 5),
            "memory_limit": memory_limit,
        }
        try:
            resp = self.session.post(
                f"{self.url}/submissions?base64_encoded=true&wait=true",
                json=payload, headers=self.headers, timeout=self.http_timeout,
            )
            resp.raise_for_status()
            data = resp.json()
        except (requests.RequestException, ValueError) as exc:
            log.warning("Judge0 request failed: %s", exc)
            return RunResult(INTERNAL_ERROR, message=f"Compiler API unavailable: {exc}")

        status_id = (data.get("status") or {}).get("id")
        status = self._STATUS.get(status_id, RUNTIME_ERROR if status_id and 7 <= status_id <= 12 else INTERNAL_ERROR)
        t = data.get("time")
        return RunResult(
            status=status,
            stdout=_unb64(data.get("stdout")),
            stderr=_unb64(data.get("stderr")),
            compile_output=_unb64(data.get("compile_output")),
            time_ms=float(t) * 1000 if t else None,
            message=_unb64(data.get("message")) or (data.get("status") or {}).get("description", ""),
        )


class PistonRunner:
    def __init__(self, url, token="", http_timeout=30, session=None):
        self.url = url.rstrip("/")
        self.http_timeout = http_timeout
        self.session = session or requests.Session()
        self.headers = {"Authorization": token} if token else {}

    def run(self, source, stdin, time_limit=2.0, memory_limit=65536, files=None):
        extra = [{"name": n, "content": c} for n, c in (files or {}).items()]
        payload = {
            "language": "c",
            "version": "*",
            "files": [{"name": "main.c", "content": source}] + extra,
            "stdin": stdin,
            "run_timeout": int(time_limit * 1000),
            "compile_timeout": 10000,
            "run_memory_limit": memory_limit * 1024,
        }
        try:
            resp = self.session.post(f"{self.url}/execute", json=payload,
                                     headers=self.headers, timeout=self.http_timeout)
            resp.raise_for_status()
            data = resp.json()
        except (requests.RequestException, ValueError) as exc:
            log.warning("Piston request failed: %s", exc)
            return RunResult(INTERNAL_ERROR, message=f"Compiler API unavailable: {exc}")

        comp = data.get("compile") or {}
        if comp.get("code"):
            return RunResult(COMPILE_ERROR, compile_output=comp.get("output", ""))
        run = data.get("run") or {}
        if run.get("status") == "TO" or (run.get("signal") == "SIGKILL" and run.get("code") is None):
            status = TIMEOUT
        elif run.get("code") or run.get("signal"):
            status = RUNTIME_ERROR
        else:
            status = OK
        wall = run.get("wall_time")
        return RunResult(status, stdout=run.get("stdout", ""), stderr=run.get("stderr", ""),
                         time_ms=float(wall) if wall is not None else None,
                         message=run.get("message") or "")


class LocalGccRunner:
    """Development only: compiles with the gcc on PATH. Not a sandbox."""

    def run(self, source, stdin, time_limit=2.0, memory_limit=65536, files=None):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "code.c"
            exe = Path(tmp) / ("code.exe" if os.name == "nt" else "code.out")
            src.write_text(source, encoding="utf-8")
            for name, content in (files or {}).items():
                (Path(tmp) / name).write_text(content, encoding="utf-8", newline="")
            # Same flags as onlinecompiler.io, so results match production.
            comp = subprocess.run(["gcc", "-O2", str(src), "-o", str(exe), "-lm"],
                                  capture_output=True, text=True, cwd=tmp)
            if comp.returncode:
                return RunResult(COMPILE_ERROR, compile_output=comp.stderr)
            start = time.perf_counter()
            try:
                proc = subprocess.run([str(exe)], input=stdin.encode(), capture_output=True,
                                      timeout=time_limit, cwd=tmp)
            except subprocess.TimeoutExpired:
                return RunResult(TIMEOUT, time_ms=time_limit * 1000)
            elapsed = (time.perf_counter() - start) * 1000
            return RunResult(OK if proc.returncode == 0 else RUNTIME_ERROR,
                             stdout=proc.stdout.decode(errors="replace").replace("\r\n", "\n"),
                             stderr=proc.stderr.decode(errors="replace"), time_ms=elapsed)


def make_runner(config):
    backend = config["COMPILER_BACKEND"]
    if backend == "onlinecompiler":
        return OnlineCompilerRunner(config["ONLINECOMPILER_URL"], config["ONLINECOMPILER_KEY"],
                                    config["ONLINECOMPILER_COMPILER"], config["HTTP_TIMEOUT"])
    if backend == "judge0":
        return Judge0Runner(config["JUDGE0_URL"], config["JUDGE0_KEY"], config["JUDGE0_HOST"],
                            config["JUDGE0_LANGUAGE_ID"], config["HTTP_TIMEOUT"])
    if backend == "piston":
        return PistonRunner(config["PISTON_URL"], config["PISTON_TOKEN"], config["HTTP_TIMEOUT"])
    if backend == "local":
        return LocalGccRunner()
    raise ValueError(f"Unknown COMPILER_BACKEND: {backend}")


def _b64(text):
    return base64.b64encode((text or "").encode("utf-8")).decode("ascii")


def _unb64(text):
    if not text:
        return ""
    return base64.b64decode(text).decode("utf-8", errors="replace")

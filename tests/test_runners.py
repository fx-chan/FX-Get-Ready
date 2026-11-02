"""Runner adapters, tested against canned API responses (no network)."""
import base64
import shutil

import pytest
import requests

from prep import content, judge, runners
from prep.config import Config


def b64(s):
    return base64.b64encode(s.encode()).decode()


class FakeResponse:
    def __init__(self, data, status=200):
        self._data, self.status_code = data, status

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP {self.status_code}")

    def json(self):
        return self._data


class FakeSession:
    def __init__(self, response=None, exc=None):
        self.response, self.exc, self.requests = response, exc, []

    def post(self, url, **kwargs):
        self.requests.append((url, kwargs))
        if self.exc:
            raise self.exc
        return self.response


# --- Judge0 -----------------------------------------------------------------

def judge0(data=None, **kw):
    session = FakeSession(FakeResponse(data or {}), **kw)
    return runners.Judge0Runner("https://judge0.test/", session=session), session


def test_judge0_request_shape():
    r, s = judge0({"status": {"id": 3}, "stdout": b64("ok\n"), "time": "0.012"})
    res = r.run("int main(){}", "5\n", time_limit=1.5)
    url, kw = s.requests[0]
    assert url == "https://judge0.test/submissions?base64_encoded=true&wait=true"
    body = kw["json"]
    assert body["language_id"] == 50 and body["cpu_time_limit"] == 1.5
    assert base64.b64decode(body["source_code"]).decode() == "int main(){}"
    assert base64.b64decode(body["stdin"]).decode() == "5\n"
    assert res.status == runners.OK and res.stdout == "ok\n" and res.time_ms == pytest.approx(12)


def test_judge0_rapidapi_headers():
    r = runners.Judge0Runner("https://judge0-ce.p.rapidapi.com", key="k", session=FakeSession())
    assert r.headers["X-RapidAPI-Key"] == "k"
    assert r.headers["X-RapidAPI-Host"] == "judge0-ce.p.rapidapi.com"


@pytest.mark.parametrize("status_id, expected", [
    (3, runners.OK), (4, runners.OK), (5, runners.TIMEOUT), (6, runners.COMPILE_ERROR),
    (11, runners.RUNTIME_ERROR), (13, runners.INTERNAL_ERROR),
])
def test_judge0_status_mapping(status_id, expected):
    r, _ = judge0({"status": {"id": status_id}, "compile_output": b64("err")})
    assert r.run("x", "").status == expected


def test_judge0_unicode_roundtrip():
    r, _ = judge0({"status": {"id": 3}, "stdout": b64("Príklad — пример\n")})
    assert r.run("x", "").stdout == "Príklad — пример\n"


@pytest.mark.parametrize("kw", [
    {"exc": requests.ConnectionError("down")},
])
def test_judge0_network_error(kw):
    r, _ = judge0(**kw)
    res = r.run("x", "")
    assert res.status == runners.INTERNAL_ERROR and "down" in res.message


def test_judge0_http_error():
    r = runners.Judge0Runner("https://j.test", session=FakeSession(FakeResponse({}, status=429)))
    assert r.run("x", "").status == runners.INTERNAL_ERROR


# --- Piston -----------------------------------------------------------------

def piston(data):
    s = FakeSession(FakeResponse(data))
    return runners.PistonRunner("https://piston.test/api/v2", session=s), s


def test_piston_ok():
    r, s = piston({"compile": {"code": 0, "output": ""}, "run": {"stdout": "4\n", "stderr": "", "code": 0, "signal": None}})
    res = r.run("src", "2\n", time_limit=1)
    url, kw = s.requests[0]
    assert url == "https://piston.test/api/v2/execute"
    assert kw["json"]["files"][0]["content"] == "src" and kw["json"]["run_timeout"] == 1000
    assert res.status == runners.OK and res.stdout == "4\n"


@pytest.mark.parametrize("data, expected", [
    ({"compile": {"code": 1, "output": "error: x"}}, runners.COMPILE_ERROR),
    ({"compile": {"code": 0}, "run": {"code": None, "signal": "SIGKILL"}}, runners.TIMEOUT),
    ({"compile": {"code": 0}, "run": {"code": None, "signal": "SIGKILL", "status": "TO"}}, runners.TIMEOUT),
    ({"compile": {"code": 0}, "run": {"code": 139, "signal": None}}, runners.RUNTIME_ERROR),
])
def test_piston_failures(data, expected):
    r, _ = piston(data)
    assert r.run("src", "").status == expected


def test_make_runner():
    cfg = {k: getattr(Config, k) for k in dir(Config) if k.isupper()}
    for backend, cls in [("onlinecompiler", runners.OnlineCompilerRunner), ("judge0", runners.Judge0Runner),
                         ("piston", runners.PistonRunner), ("local", runners.LocalGccRunner)]:
        assert isinstance(runners.make_runner({**cfg, "COMPILER_BACKEND": backend}), cls)
    with pytest.raises(ValueError):
        runners.make_runner({**cfg, "COMPILER_BACKEND": "nope"})


def test_piston_sends_input_files():
    r, s = piston({"compile": {"code": 0}, "run": {"stdout": "", "code": 0}})
    r.run("src", "", files={"a.txt": "x"})
    assert s.requests[0][1]["json"]["files"][1] == {"name": "a.txt", "content": "x"}


def test_judge0_refuses_input_files():
    r, s = judge0({"status": {"id": 3}})
    assert r.run("x", "", files={"a.txt": "x"}).status == runners.INTERNAL_ERROR
    assert s.requests == []


# --- onlinecompiler.io --------------------------------------------------------
# Response shapes below were captured from the real API (gcc-15) on 2026-11-02.

class SeqSession(FakeSession):
    def __init__(self, responses):
        super().__init__()
        self.responses = list(responses)

    def post(self, url, **kwargs):
        self.requests.append((url, kwargs))
        return self.responses.pop(0)


def oc(*responses):
    s = SeqSession([FakeResponse(d, status) for d, status in responses])
    sleeps = []
    return runners.OnlineCompilerRunner("https://api.oc.test/", "KEY", session=s, sleep=sleeps.append), s, sleeps


def oc_result(**kw):
    base = {"output": "", "error": "", "status": "success", "exit_code": 0, "signal": None,
            "truncated": False, "time": "0.0120", "total": "0.05", "memory": "3000", "files": [],
            "files_truncated": False, "time_limit": 2}
    base.update(kw)
    return base


def test_onlinecompiler_request_shape_and_ok():
    r, s, _ = oc((oc_result(output="5\n"), 200))
    res = r.run("int main(){}", "2 3\n", time_limit=1.5, files={"znak.txt": "abc"})
    url, kw = s.requests[0]
    assert url == "https://api.oc.test/api/run-code-sync/"
    assert kw["headers"]["Authorization"] == "KEY"  # raw key, no "Bearer"
    assert kw["json"] == {"compiler": "gcc-15", "code": "int main(){}", "input": "2 3\n", "time_limit": 1.5,
                          "files": [{"name": "znak.txt", "content": "abc"}]}
    assert res.status == runners.OK and res.stdout == "5\n" and res.time_ms == pytest.approx(12)


@pytest.mark.parametrize("data, expected", [
    (oc_result(status="error", exit_code=1, time="0.0000", memory="0",
               error="code.c: In function 'main':\ncode.c:2:28: error: expected ';' before 'return'\n"),
     runners.COMPILE_ERROR),
    (oc_result(status="error", exit_code=1, error="/usr/bin/ld: undefined reference to `foo'\n"
                                                  "collect2: error: ld returned 1 exit status\n"),
     runners.COMPILE_ERROR),
    (oc_result(status="error", exit_code=124, time="1.0129"), runners.TIMEOUT),
    (oc_result(status="error", exit_code=139, signal=11), runners.RUNTIME_ERROR),
    (oc_result(status="error", exit_code=1, output="partial\n"), runners.RUNTIME_ERROR),
    (oc_result(status="error", exit_code=-1, error="sandbox failed"), runners.INTERNAL_ERROR),
])
def test_onlinecompiler_status_mapping(data, expected):
    r, _, _ = oc((data, 200))
    assert r.run("x", "").status == expected


def test_onlinecompiler_segfault_message():
    r, _, _ = oc((oc_result(status="error", exit_code=139, signal=11), 200))
    assert r.run("x", "").message == "Segmentation fault"


def test_onlinecompiler_retries_on_429_then_succeeds():
    r, s, sleeps = oc(({}, 429), (oc_result(output="ok\n"), 200))
    res = r.run("x", "")
    assert res.status == runners.OK and len(s.requests) == 2 and sleeps == [1.5]


def test_onlinecompiler_gives_up_after_retries():
    r, s, sleeps = oc(({}, 429), ({}, 429), ({}, 429))
    res = r.run("x", "")
    assert res.status == runners.INTERNAL_ERROR and "preťažený" in res.message
    assert len(s.requests) == 3 and len(sleeps) == 2


def test_onlinecompiler_bad_key():
    r, _, _ = oc(({"error": "Invalid API key"}, 404))
    assert r.run("x", "").status == runners.INTERNAL_ERROR


# --- Real content, real compiler (only where gcc is installed) --------------

def _all_items():
    for s in content.load_subjects(Config.CONTENT_DIR):
        for b in s.blocks:
            yield from b.tasks + b.drills


@pytest.mark.skipif(not shutil.which("gcc"), reason="gcc not installed")
def test_reference_solutions_pass_with_local_gcc():
    """Proves the shipped .out files are actually correct (tasks and drills)."""
    runner = runners.LocalGccRunner()
    checked = 0
    for t in _all_items():
        rep = judge.judge(t, (t.path / "solution.c").read_text(encoding="utf-8"), runner)
        assert rep.verdict == "AC", f"{t.path}: {rep.to_dict()}"
        checked += 1
    assert checked >= 50


@pytest.mark.skipif(not shutil.which("gcc"), reason="gcc not installed")
def test_unchanged_templates_are_not_accepted():
    """A student who submits a drill/task template as-is must not get AC."""
    runner = runners.LocalGccRunner()
    for t in _all_items():
        if "// TODO\n\n    return 0;" in t.template:
            continue  # the generic empty skeleton prints nothing, nothing to prove
        assert judge.judge(t, t.template, runner).verdict != "AC", t.path


@pytest.mark.skipif(not shutil.which("gcc"), reason="gcc not installed")
def test_local_gcc_compile_error():
    assert runners.LocalGccRunner().run("int main( {", "").status == runners.COMPILE_ERROR


@pytest.mark.skipif(not shutil.which("gcc"), reason="gcc not installed")
def test_local_gcc_input_files():
    src = '#include <stdio.h>\nint main(void){FILE*f=fopen("a.txt","r");int c;while((c=getc(f))!=EOF)putchar(c);return 0;}'
    assert runners.LocalGccRunner().run(src, "", files={"a.txt": "obsah\n"}).stdout == "obsah\n"

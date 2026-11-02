"""Generate or verify expected outputs (.out) from each task's solution.c.

    python tools/build_outputs.py                 # write missing .out files with local gcc
    python tools/build_outputs.py --force         # rewrite all .out files
    python tools/build_outputs.py --check         # only compare, exit 1 on mismatch
    python tools/build_outputs.py --check --backend onlinecompiler   # verify against production compiler

Never edit .out files by hand: fix solution.c or the .in file and rerun this.
"""
import argparse
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from prep import content, judge, runners  # noqa: E402
from prep.config import Config  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", default="local")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--only", help="substring of a task path to limit the run")
    args = ap.parse_args()

    cfg = {k: getattr(Config, k) for k in dir(Config) if k.isupper()}
    cfg["COMPILER_BACKEND"] = args.backend
    runner = runners.make_runner(cfg)
    remote = args.backend != "local"

    problems = 0
    for subject in content.load_subjects(Config.CONTENT_DIR):
        for block in subject.blocks:
            for task in block.tasks + block.drills:
                if args.only and args.only not in str(task.path):
                    continue
                sol = task.path / "solution.c"
                if not sol.exists():
                    print(f"!! {task.path}: no solution.c")
                    problems += 1
                    continue
                source = sol.read_text(encoding="utf-8")
                shared = content._read_files(task.path / "files")
                for inp in sorted((task.path / "tests").glob("*.in")):
                    out = inp.with_suffix(".out")
                    if out.exists() and not (args.force or args.check):
                        continue
                    own = inp.parent / f"{inp.stem}.files"
                    files = content._read_files(own) if own.is_dir() else shared
                    res = runner.run(source, inp.read_text(encoding="utf-8"), task.time_limit, files=files or None)
                    if remote:
                        time.sleep(2.1)  # stay under 30 runs/minute
                    label = f"{task.path.relative_to(Config.CONTENT_DIR)}/{inp.name}"
                    if res.status != runners.OK:
                        print(f"!! {label}: {res.status} {res.compile_output or res.stderr or res.message}")
                        problems += 1
                        continue
                    if args.check:
                        expected = out.read_text(encoding="utf-8") if out.exists() else None
                        if expected is None or not judge.outputs_match(res.stdout, expected, task.checker):
                            print(f"!! {label}: output differs\n--- expected\n{expected}\n--- got\n{res.stdout}")
                            problems += 1
                        continue
                    out.write_text(res.stdout, encoding="utf-8", newline="\n")
                    print(f"   wrote {label}")
    print("OK" if not problems else f"{problems} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()

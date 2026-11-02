"""Judging pipeline: run the student's code on every hidden test via a runner,
compare outputs, and produce one verdict."""
from dataclasses import asdict, dataclass, field

from . import runners

AC, WA, CE, TLE, RE, IE = "AC", "WA", "CE", "TLE", "RE", "IE"

_RUN_TO_VERDICT = {
    runners.COMPILE_ERROR: CE,
    runners.TIMEOUT: TLE,
    runners.RUNTIME_ERROR: RE,
    runners.INTERNAL_ERROR: IE,
}


def normalize(text, checker="lines"):
    text = (text or "").replace("\r\n", "\n").replace("\r", "\n")
    if checker == "exact":
        return text
    if checker == "tokens":
        return text.split()
    # "lines": ignore trailing spaces on each line and trailing blank lines.
    return "\n".join(line.rstrip() for line in text.split("\n")).rstrip("\n")


def outputs_match(actual, expected, checker="lines"):
    return normalize(actual, checker) == normalize(expected, checker)


@dataclass
class TestReport:
    name: str
    verdict: str
    time_ms: float | None = None
    # Only filled for public tests, so hidden data never leaves the server.
    input: str | None = None
    expected: str | None = None
    actual: str | None = None
    message: str = ""


@dataclass
class JudgeReport:
    verdict: str
    passed: int
    total: int
    tests: list = field(default_factory=list)
    compile_output: str = ""
    message: str = ""

    def to_dict(self):
        return asdict(self)


def judge(task, source, runner, stop_on_first_fail=True):
    cases = task.load_tests()
    if not cases:
        return JudgeReport(IE, 0, 0, message="Task has no tests.")

    reports = []
    final = AC
    for case in cases:
        res = runner.run(source, case.input, task.time_limit, task.memory_limit, files=case.files or None)
        if res.status == runners.COMPILE_ERROR:
            # Compilation does not depend on the test, no point in going on.
            return JudgeReport(CE, 0, len(cases), compile_output=res.compile_output)
        if res.status == runners.OK:
            verdict = AC if outputs_match(res.stdout, case.expected, task.checker) else WA
        else:
            verdict = _RUN_TO_VERDICT[res.status]

        rep = TestReport(case.name, verdict, res.time_ms, message=res.message if verdict == RE else "")
        if case.name in task.public_tests:
            rep.input, rep.expected, rep.actual = case.input, case.expected, res.stdout
        reports.append(rep)

        if verdict != AC:
            if final == AC:
                final = verdict
            if verdict == IE:
                return JudgeReport(IE, _passed(reports), len(cases), reports, message=res.message)
            if stop_on_first_fail:
                break

    return JudgeReport(final, _passed(reports), len(cases), reports)


def _passed(reports):
    return sum(r.verdict == AC for r in reports)

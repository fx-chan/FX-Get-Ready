import pytest

from prep import content, judge
from prep.runners import COMPILE_ERROR, INTERNAL_ERROR, OK, RUNTIME_ERROR, TIMEOUT, RunResult

from conftest import FakeRunner, doubling


@pytest.fixture
def task(content_dir):
    return content.find(content_dir, "demo", "cv01", "01_double")[2]


@pytest.mark.parametrize("actual, expected, checker, match", [
    ("2\n", "2\n", "lines", True),
    ("2", "2\n", "lines", True),               # missing final newline
    ("2   \r\n\n\n", "2\n", "lines", True),     # trailing spaces, CRLF, blank lines
    ("2 \n", "2\n", "exact", False),
    ("1  2\n3", "1 2 3\n", "tokens", True),
    ("1 2\n", "1\n2\n", "lines", False),
    ("", "2\n", "lines", False),
])
def test_outputs_match(actual, expected, checker, match):
    assert judge.outputs_match(actual, expected, checker) is match


def test_accepted(task):
    runner = FakeRunner(fn=doubling)
    rep = judge.judge(task, "src", runner)
    assert rep.verdict == "AC" and rep.passed == rep.total == 3
    assert [stdin for _, stdin, _ in runner.calls] == ["1\n", "5\n", "21\n"]


def test_wrong_answer_stops_early_and_hides_private_data(task):
    runner = FakeRunner([RunResult(OK, "2\n"), RunResult(OK, "11\n"), RunResult(OK, "42\n")])
    rep = judge.judge(task, "src", runner)
    assert rep.verdict == "WA" and rep.passed == 1 and rep.total == 3
    assert len(runner.calls) == 2  # stopped after first failure
    public, private = rep.tests
    assert public.input == "1\n" and public.expected == "2\n"
    assert private.input is None and private.expected is None and private.actual is None


def test_wrong_answer_without_early_stop(task):
    runner = FakeRunner([RunResult(OK, "0\n"), RunResult(OK, "10\n"), RunResult(OK, "0\n")])
    rep = judge.judge(task, "src", runner, stop_on_first_fail=False)
    assert rep.verdict == "WA" and rep.passed == 1 and len(rep.tests) == 3


def test_compile_error_short_circuits(task):
    runner = FakeRunner([RunResult(COMPILE_ERROR, compile_output="main.c:1: error")])
    rep = judge.judge(task, "src", runner)
    assert rep.verdict == "CE" and rep.compile_output == "main.c:1: error"
    assert len(runner.calls) == 1 and rep.tests == []


@pytest.mark.parametrize("status, verdict", [(TIMEOUT, "TLE"), (RUNTIME_ERROR, "RE"), (INTERNAL_ERROR, "IE")])
def test_other_failures(task, status, verdict):
    runner = FakeRunner([RunResult(OK, "2\n"), RunResult(status, message="boom")])
    rep = judge.judge(task, "src", runner, stop_on_first_fail=False)
    assert rep.verdict == verdict
    if verdict == "IE":
        assert len(runner.calls) == 2 and rep.message == "boom"  # API down: never keep hammering it


def test_first_failure_wins(task):
    runner = FakeRunner([RunResult(TIMEOUT), RunResult(OK, "0\n"), RunResult(OK, "42\n")])
    rep = judge.judge(task, "src", runner, stop_on_first_fail=False)
    assert rep.verdict == "TLE"


def test_task_without_tests(task):
    for f in (task.path / "tests").iterdir():
        f.unlink()
    assert judge.judge(task, "src", FakeRunner()).verdict == "IE"


def test_input_files_reach_the_runner(content_dir):
    drill = content.find(content_dir, "demo", "cv01", "d-echo")[2]
    runner = FakeRunner([RunResult(OK, "shared\n"), RunResult(OK, "own\n")])
    rep = judge.judge(drill, "src", runner)
    assert rep.verdict == "AC"
    assert [files for _, _, files in runner.calls] == [{"data.txt": "shared\n"}, {"data.txt": "own\n"}]


def test_runtime_error_message_is_reported(task):
    runner = FakeRunner([RunResult(RUNTIME_ERROR, message="Segmentation fault")])
    rep = judge.judge(task, "src", runner)
    assert rep.verdict == "RE" and rep.tests[0].message == "Segmentation fault"

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from prep import create_app  # noqa: E402
from prep.runners import OK, RunResult  # noqa: E402


class FakeRunner:
    """Returns queued results (or a callable's result) and records every call."""

    def __init__(self, results=None, fn=None):
        self.results = list(results or [])
        self.fn = fn
        self.calls = []

    def run(self, source, stdin, time_limit=2.0, memory_limit=65536, files=None):
        self.calls.append((source, stdin, files))
        if self.fn:
            return self.fn(source, stdin)
        return self.results.pop(0) if self.results else RunResult(OK)


THEORY = """## Teória

`printf`

::: quiz
Koľko je 1 + 1?
- [ ] 1
- [x] 2
> Lebo matematika.
:::

::: drill d-echo
::: drill missing-drill
"""


@pytest.fixture
def content_dir(tmp_path):
    """A tiny subject: one task (doubles the input, three tests) and one drill reading a file."""
    root = tmp_path / "content"
    block = root / "demo" / "cv01"
    task = block / "tasks" / "01_double"
    (task / "tests").mkdir(parents=True)
    (root / "demo" / "subject.json").write_text(json.dumps({"title": "Demo"}), encoding="utf-8")
    (block / "block.json").write_text(json.dumps({"title": "CV 1", "lecture": "P1"}), encoding="utf-8")
    (block / "theory.md").write_text(THEORY, encoding="utf-8")
    (task / "metadata.json").write_text(json.dumps({
        "title": "Double", "limits": {"time": 1}, "public_tests": ["01"],
    }), encoding="utf-8")
    (task / "description.md").write_text("Vypíš **dvojnásobok**.", encoding="utf-8")
    (task / "template.c").write_text("int main(void){return 0;}\n", encoding="utf-8")
    for name, n in [("01", 1), ("02", 5), ("03", 21)]:
        (task / "tests" / f"{name}.in").write_text(f"{n}\n", encoding="utf-8")
        (task / "tests" / f"{name}.out").write_text(f"{2 * n}\n", encoding="utf-8")
    (task / "tests" / "orphan.in").write_text("x", encoding="utf-8")  # no .out -> ignored

    drill = block / "drills" / "d-echo"
    (drill / "tests" / "02.files").mkdir(parents=True)
    (drill / "files").mkdir()
    (drill / "metadata.json").write_text(json.dumps({"title": "Echo"}), encoding="utf-8")
    (drill / "description.md").write_text("Vypíš súbor.", encoding="utf-8")
    (drill / "template.c").write_text("/* DOPLŇ */\n", encoding="utf-8")
    (drill / "files" / "data.txt").write_text("shared\n", encoding="utf-8")
    (drill / "tests" / "02.files" / "data.txt").write_text("own\n", encoding="utf-8")
    for name, out in [("01", "shared\n"), ("02", "own\n")]:
        (drill / "tests" / f"{name}.in").write_text("", encoding="utf-8")
        (drill / "tests" / f"{name}.out").write_text(out, encoding="utf-8")
    return root


def doubling(source, stdin):
    return RunResult(OK, stdout=f"{2 * int(stdin)}\n", time_ms=3)


def csrf_of(client):
    html = client.get("/").get_data(as_text=True)
    return re.search(r'name="csrf-token" content="([^"]+)"', html).group(1)


@pytest.fixture
def make_app(content_dir, tmp_path):
    def _make(runner=None, **overrides):
        cfg = {"CONTENT_DIR": content_dir, "DATABASE": tmp_path / "db" / "test.sqlite", "TESTING": True,
               "SECRET_KEY": "test", "USER_RUNS_PER_MINUTE": 100, "ALLOW_REGISTRATION": True}
        cfg.update(overrides)
        return create_app(cfg, runner=runner or FakeRunner())
    return _make


@pytest.fixture
def make_client(make_app):
    """Anonymous client (pages only)."""
    def _make(runner=None, **overrides):
        return make_app(runner, **overrides).test_client()
    return _make


class ApiClient:
    """Logged-in test client that sends the CSRF header like ide.js does."""

    def __init__(self, client):
        self.client = client
        self.csrf = csrf_of(client)

    def post(self, url, **kw):
        kw.setdefault("headers", {})["X-CSRF-Token"] = self.csrf
        return self.client.post(url, **kw)

    def get(self, url, **kw):
        return self.client.get(url, **kw)


def register(client, username="student", password="tajneheslo"):
    token = csrf_of(client)
    return client.post("/register", data={"csrf": token, "username": username,
                                          "password": password, "password2": password})


@pytest.fixture
def api_client(make_app):
    def _make(runner=None, **overrides):
        client = make_app(runner, **overrides).test_client()
        assert register(client).status_code == 302
        return ApiClient(client)
    return _make

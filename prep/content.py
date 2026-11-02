"""File-based content store.

Layout:
    content/<subject>/subject.json
    content/<subject>/<block>/block.json
    content/<subject>/<block>/theory.md            (lesson; may embed drills and quizzes)
    content/<subject>/<block>/tasks/<task>/        practice task (own page with IDE)
    content/<subject>/<block>/drills/<drill>/      mini exercise embedded in the lesson

A task or drill folder holds:
    metadata.json  description.md  template.c  solution.c (never served)
    tests/<name>.in + <name>.out
    files/<file>                 input files every test gets in its working dir (optional)
    tests/<name>.files/<file>    input files for one test, replacing files/ (optional)

Directories are ordered by name, so prefix them (cv01, cv02, 01_hello, ...).
Only folders found by scanning are reachable, so URL slugs never touch the
filesystem directly.

Lesson syntax inside theory.md:
    ::: drill <slug>            embeds drills/<slug>
    ::: quiz                    multiple-choice question, checked in the browser
    Question text (markdown)
    - [ ] wrong option
    - [x] correct option
    > explanation shown after answering
    :::
"""
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9_-]*$")


@dataclass
class TestCase:
    name: str
    input: str
    expected: str
    files: dict = field(default_factory=dict)


@dataclass
class Task:
    slug: str
    path: Path
    title: str
    kind: str = "task"  # task | drill
    difficulty: str = "easy"
    time_limit: float = 2.0  # seconds per test
    memory_limit: int = 65536  # KB
    checker: str = "lines"  # lines | exact | tokens
    public_tests: list = field(default_factory=list)  # test names whose details are shown

    @property
    def description_md(self):
        return _read(self.path / "description.md")

    @property
    def template(self):
        return _read(self.path / "template.c")

    def load_tests(self):
        tests_dir = self.path / "tests"
        shared = _read_files(self.path / "files")
        cases = []
        for inp in sorted(tests_dir.glob("*.in")):
            out = inp.with_suffix(".out")
            if out.exists():
                own = tests_dir / f"{inp.stem}.files"
                files = _read_files(own) if own.is_dir() else shared
                cases.append(TestCase(inp.stem, _read(inp), _read(out), files))
        return cases


@dataclass
class Block:
    slug: str
    path: Path
    title: str
    summary: str = ""
    lecture: str = ""
    tasks: list = field(default_factory=list)
    drills: list = field(default_factory=list)

    @property
    def theory_md(self):
        return _read(self.path / "theory.md")

    def task(self, slug):
        return next((t for t in self.tasks + self.drills if t.slug == slug), None)


@dataclass
class Subject:
    slug: str
    path: Path
    title: str
    summary: str = ""
    blocks: list = field(default_factory=list)

    def block(self, slug):
        return next((b for b in self.blocks if b.slug == slug), None)


def _read(path):
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def _read_files(directory):
    if not directory.is_dir():
        return {}
    return {p.name: _read(p) for p in sorted(directory.iterdir()) if p.is_file()}


def _meta(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}


def _subdirs(path):
    if not path.is_dir():
        return []
    return [p for p in sorted(path.iterdir()) if p.is_dir() and SLUG_RE.match(p.name)]


def load_task(path, kind="task"):
    meta = _meta(path / "metadata.json")
    limits = meta.get("limits", {})
    return Task(
        slug=path.name,
        path=path,
        title=meta.get("title", path.name),
        kind=kind,
        difficulty=meta.get("difficulty", "easy"),
        time_limit=float(limits.get("time", 2.0)),
        memory_limit=int(limits.get("memory_kb", 65536)),
        checker=meta.get("checker", "lines"),
        public_tests=list(meta.get("public_tests", [])),
    )


def load_subjects(content_dir):
    subjects = []
    for s_dir in _subdirs(Path(content_dir)):
        s_meta = _meta(s_dir / "subject.json")
        subject = Subject(s_dir.name, s_dir, s_meta.get("title", s_dir.name), s_meta.get("summary", ""))
        for b_dir in _subdirs(s_dir):
            b_meta = _meta(b_dir / "block.json")
            block = Block(b_dir.name, b_dir, b_meta.get("title", b_dir.name), b_meta.get("summary", ""),
                          b_meta.get("lecture", ""))
            block.tasks = [load_task(t) for t in _subdirs(b_dir / "tasks")]
            block.drills = [load_task(t, "drill") for t in _subdirs(b_dir / "drills")]
            subject.blocks.append(block)
        subjects.append(subject)
    return subjects


def find(content_dir, subject_slug, block_slug=None, task_slug=None):
    """Return (subject, block, task); missing parts are None. task may be a drill."""
    subject = next((s for s in load_subjects(content_dir) if s.slug == subject_slug), None)
    block = subject.block(block_slug) if subject and block_slug else None
    task = block.task(task_slug) if block and task_slug else None
    return subject, block, task


# --- lesson parsing ---------------------------------------------------------

_DRILL_RE = re.compile(r"^:::\s*drill\s+([a-z0-9][a-z0-9_-]*)\s*$")
_OPTION_RE = re.compile(r"^-\s*\[( |x|X)\]\s+(.*)$")


def parse_lesson(text):
    """Split theory.md into segments: ("md", text), ("drill", slug), ("quiz", dict)."""
    segments, buf = [], []
    lines = text.splitlines()
    i = 0

    def flush():
        if any(line.strip() for line in buf):
            segments.append(("md", "\n".join(buf)))
        buf.clear()

    while i < len(lines):
        line = lines[i]
        drill = _DRILL_RE.match(line.strip())
        if drill:
            flush()
            segments.append(("drill", drill.group(1)))
        elif line.strip() == "::: quiz":
            flush()
            quiz = {"question": [], "options": [], "explanation": []}
            i += 1
            while i < len(lines) and lines[i].strip() != ":::":
                body = lines[i].strip()
                opt = _OPTION_RE.match(body)
                if opt:
                    quiz["options"].append((opt.group(2), opt.group(1).lower() == "x"))
                elif body.startswith(">"):
                    quiz["explanation"].append(body[1:].strip())
                else:
                    quiz["question"].append(lines[i])
                i += 1
            segments.append(("quiz", {
                "question": "\n".join(quiz["question"]).strip(),
                "options": quiz["options"],
                "explanation": " ".join(quiz["explanation"]),
            }))
        else:
            buf.append(line)
        i += 1
    flush()
    return segments

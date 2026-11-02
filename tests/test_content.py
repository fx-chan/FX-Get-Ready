import re

from prep import content
from prep.config import Config


def test_load_subjects_structure(content_dir):
    subjects = content.load_subjects(content_dir)
    assert [s.slug for s in subjects] == ["demo"]
    block = subjects[0].blocks[0]
    assert block.title == "CV 1" and block.lecture == "P1"
    task = block.tasks[0]
    assert task.title == "Double" and task.kind == "task"
    assert task.time_limit == 1.0
    assert task.public_tests == ["01"]
    assert [d.slug for d in block.drills] == ["d-echo"] and block.drills[0].kind == "drill"
    assert block.task("d-echo") is block.drills[0]


def test_tests_paired_and_sorted(content_dir):
    _, _, task = content.find(content_dir, "demo", "cv01", "01_double")
    cases = task.load_tests()
    assert [c.name for c in cases] == ["01", "02", "03"]  # orphan.in skipped
    assert cases[1].input == "5\n" and cases[1].expected == "10\n"
    assert cases[0].files == {}


def test_input_files_shared_and_per_test(content_dir):
    _, _, drill = content.find(content_dir, "demo", "cv01", "d-echo")
    first, second = drill.load_tests()
    assert first.files == {"data.txt": "shared\n"}
    assert second.files == {"data.txt": "own\n"}  # tests/02.files replaces files/


def test_find_unknown_and_traversal(content_dir):
    assert content.find(content_dir, "nope") == (None, None, None)
    subj, blk, tsk = content.find(content_dir, "demo", "..", "..")
    assert subj is not None and blk is None and tsk is None


def test_parse_lesson():
    segs = content.parse_lesson(
        "# Nadpis\ntext\n::: drill d1-x\n::: quiz\nOtázka?\n- [ ] nie\n- [x] **áno**\n> preto\n:::\nkoniec\n")
    assert [k for k, _ in segs] == ["md", "drill", "quiz", "md"]
    assert segs[1][1] == "d1-x"
    quiz = segs[2][1]
    assert quiz["question"] == "Otázka?"
    assert quiz["options"] == [("nie", False), ("**áno**", True)]
    assert quiz["explanation"] == "preto"


def _all_items():
    for s in content.load_subjects(Config.CONTENT_DIR):
        for b in s.blocks:
            yield s, b


def test_real_content_is_well_formed():
    """Every shipped task/drill has a description, template, solution and paired tests."""
    count = 0
    for _, b in _all_items():
        slugs = [t.slug for t in b.tasks + b.drills]
        assert len(slugs) == len(set(slugs)), f"{b.path}: task and drill slugs must be unique"
        for t in b.tasks + b.drills:
            count += 1
            assert t.description_md.strip(), t.path
            assert t.template.strip(), t.path
            assert (t.path / "solution.c").exists(), t.path
            cases = t.load_tests()
            assert cases, f"{t.path} has no tests"
            assert len(cases) == len(list((t.path / "tests").glob("*.in"))), f"{t.path}: .in without .out"
            assert set(t.public_tests) <= {c.name for c in cases}, t.path
    assert count >= 50


def test_lessons_reference_existing_drills_and_valid_quizzes():
    for _, b in _all_items():
        segs = content.parse_lesson(b.theory_md)
        referenced = [v for k, v in segs if k == "drill"]
        assert sorted(referenced) == sorted(d.slug for d in b.drills), f"{b.path}: every drill embedded once"
        for kind, quiz in segs:
            if kind == "quiz":
                assert quiz["question"] and len(quiz["options"]) >= 2, b.path
                assert sum(ok for _, ok in quiz["options"]) == 1, f"{b.path}: one correct option"


def test_drill_templates_mark_the_gap():
    for _, b in _all_items():
        for d in b.drills:
            assert re.search(r"DOPLŇ", d.template), f"{d.path}: template must show where to write"

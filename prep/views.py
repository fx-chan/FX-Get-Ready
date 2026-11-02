import re

import markdown as md
from flask import Blueprint, abort, current_app, g, jsonify, make_response, render_template, request
from markupsafe import Markup

from . import content, db, judge
from .auth import api_login_required

bp = Blueprint("main", __name__)

MD_EXTENSIONS = ["fenced_code", "tables", "sane_lists"]


def render_md(text):
    # Content is authored by the course team, not by students, so it is trusted.
    return Markup(md.markdown(text, extensions=MD_EXTENSIONS))


def render_inline_md(text):
    html = md.markdown(text, extensions=MD_EXTENSIONS)
    return Markup(re.sub(r"^<p>(.*)</p>$", r"\1", html.strip(), flags=re.S))


def _content_dir():
    return current_app.config["CONTENT_DIR"]


def task_key(subject, block, task):
    return f"{subject.slug}/{block.slug}/{task.slug}"


def _solved():
    return db.solved_keys(g.user["id"]) if g.user else set()


def _progress(subject, block, solved):
    items = block.tasks + block.drills
    done = sum(task_key(subject, block, t) in solved for t in items)
    return {"done": done, "total": len(items), "pct": round(100 * done / len(items)) if items else 0}


@bp.app_context_processor
def inject_helpers():
    return {"task_key": task_key}


@bp.route("/")
def index():
    solved = _solved()
    subjects = content.load_subjects(_content_dir())
    stats = {}
    for s in subjects:
        done = total = 0
        for b in s.blocks:
            p = _progress(s, b, solved)
            done, total = done + p["done"], total + p["total"]
        stats[s.slug] = {"done": done, "total": total, "pct": round(100 * done / total) if total else 0}
    return render_template("index.html", subjects=subjects, stats=stats)


@bp.route("/<subject_slug>/")
def subject(subject_slug):
    subj, _, _ = content.find(_content_dir(), subject_slug)
    if not subj:
        abort(404)
    solved = _solved()
    progress = {b.slug: _progress(subj, b, solved) for b in subj.blocks}
    return render_template("subject.html", subject=subj, progress=progress)


@bp.route("/<subject_slug>/<block_slug>/")
def block(subject_slug, block_slug):
    subj, blk, _ = content.find(_content_dir(), subject_slug, block_slug)
    if not blk:
        abort(404)
    segments = []
    for kind, value in content.parse_lesson(blk.theory_md):
        if kind == "md":
            segments.append(("md", render_md(value)))
        elif kind == "drill":
            drill = blk.task(value)
            if drill is not None:
                segments.append(("drill", drill))
        else:
            segments.append(("quiz", {
                "question": render_md(value["question"]),
                "options": [(render_inline_md(text), ok) for text, ok in value["options"]],
                "explanation": render_inline_md(value["explanation"]) if value["explanation"] else "",
            }))
    solved = _solved()
    idx = subj.blocks.index(blk)
    return render_template("block.html", subject=subj, block=blk, segments=segments, solved=solved,
                           progress=_progress(subj, blk, solved), render_md=render_md,
                           prev_block=subj.blocks[idx - 1] if idx > 0 else None,
                           next_block=subj.blocks[idx + 1] if idx + 1 < len(subj.blocks) else None)


@bp.route("/<subject_slug>/<block_slug>/<task_slug>/")
def task(subject_slug, block_slug, task_slug):
    subj, blk, tsk = content.find(_content_dir(), subject_slug, block_slug, task_slug)
    if not tsk:
        abort(404)
    key = task_key(subj, blk, tsk)
    last = db.last_source(g.user["id"], key) if g.user else None
    idx = blk.tasks.index(tsk) if tsk in blk.tasks else -1
    return render_template("task.html", subject=subj, block=blk, task=tsk, key=key, last_source=last,
                           description=render_md(tsk.description_md), solved=_solved(),
                           next_task=blk.tasks[idx + 1] if 0 <= idx < len(blk.tasks) - 1 else None)


def _fail(message, code):
    abort(make_response(jsonify(error=message), code))


def _read_source():
    data = request.get_json(silent=True) or {}
    source = data.get("source")
    if not isinstance(source, str) or not source.strip():
        _fail("Missing source code / Chýba zdrojový kód / Нет кода", 400)
    if len(source.encode("utf-8")) > current_app.config["MAX_SOURCE_BYTES"]:
        _fail("Source too large", 413)
    return data, source


def _rate_limit():
    if not current_app.extensions["rate_limiter"].allow(g.user["id"], current_app.config["USER_RUNS_PER_MINUTE"]):
        _fail("Príliš veľa spustení, počkajte minútu. / Слишком много запусков, подождите минуту.", 429)


@bp.post("/api/<subject_slug>/<block_slug>/<task_slug>/submit")
@api_login_required
def submit(subject_slug, block_slug, task_slug):
    subj, blk, tsk = content.find(_content_dir(), subject_slug, block_slug, task_slug)
    if not tsk:
        abort(404)
    _, source = _read_source()
    _rate_limit()
    report = judge.judge(tsk, source, current_app.extensions["runner"],
                         current_app.config["STOP_ON_FIRST_FAIL"])
    key = task_key(subj, blk, tsk)
    if report.verdict != judge.IE:
        db.record_submission(g.user["id"], key, report, source)
    current_app.logger.info("submit %s by %s -> %s (%d/%d)", key, g.user["username"],
                            report.verdict, report.passed, report.total)
    return jsonify(report.to_dict())


@bp.post("/api/<subject_slug>/<block_slug>/<task_slug>/run")
@api_login_required
def run(subject_slug, block_slug, task_slug):
    """Run with the student's own stdin, no judging."""
    _, _, tsk = content.find(_content_dir(), subject_slug, block_slug, task_slug)
    if not tsk:
        abort(404)
    data, source = _read_source()
    stdin = data.get("stdin") or ""
    if not isinstance(stdin, str) or len(stdin.encode("utf-8")) > current_app.config["MAX_STDIN_BYTES"]:
        _fail("Invalid stdin", 400)
    _rate_limit()
    # Tasks that read files get the first test's files, so "Run" behaves like the judge.
    cases = tsk.load_tests()
    files = cases[0].files if cases else None
    res = current_app.extensions["runner"].run(source, stdin, tsk.time_limit, tsk.memory_limit, files=files or None)
    return jsonify(status=res.status, stdout=res.stdout, stderr=res.stderr,
                   compile_output=res.compile_output, time_ms=res.time_ms, message=res.message)


@bp.app_errorhandler(404)
def not_found(_):
    if request.path.startswith("/api/"):
        return jsonify(error="Not found"), 404
    return render_template("404.html"), 404

import json
import re

import markdown as md
from flask import Blueprint, abort, current_app, g, jsonify, make_response, redirect, render_template, request
from markupsafe import Markup, escape

from . import content, db, i18n, judge, mathcheck
from .auth import _safe_next, api_login_required
from .i18n import t

bp = Blueprint("main", __name__)

MD_EXTENSIONS = ["fenced_code", "tables", "sane_lists"]
_MATH_RE = re.compile(r"\$\$(.+?)\$\$|(?<![\\$])\$(?!\s)([^$\n]+?)(?<!\s)\$", re.S)


def _protect_math(text):
    """Swap $...$ / $$...$$ for placeholders so markdown leaves the TeX alone."""
    stash = []

    def keep(m):
        display = m.group(1) is not None
        stash.append((m.group(1) if display else m.group(2), display))
        return f"@@MATH{len(stash) - 1}@@"

    return _MATH_RE.sub(keep, text), stash


def _restore_math(html, stash):
    def put(m):
        tex, display = stash[int(m.group(1))]
        tag = "div" if display else "span"
        return f'<{tag} class="math" data-display="{int(display)}">{escape(tex)}</{tag}>'

    return re.sub(r"@@MATH(\d+)@@", put, html)


def render_md(text, math=False):
    # Content is authored by the course team, not by students, so it is trusted.
    stash = []
    if math:
        text, stash = _protect_math(text)
    html = md.markdown(text, extensions=MD_EXTENSIONS)
    return Markup(_restore_math(html, stash) if stash else html)


def render_inline_md(text, math=False):
    html = str(render_md(text, math)).strip()
    return Markup(re.sub(r"^<p>(.*)</p>$", r"\1", html, flags=re.S))


def md_filter(text, math=False, inline=False):
    return render_inline_md(text, math) if inline else render_md(text, math)


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
    return {"task_key": task_key, "md": md_filter, "none_labels": mathcheck.NONE_LABELS,
            "public_part": mathcheck.public_part}


@bp.route("/lang/<code>")
def set_lang(code):
    if code not in i18n.LANGS:
        abort(404)
    resp = redirect(_safe_next(request.args.get("next")))
    resp.set_cookie(i18n.COOKIE, code, max_age=365 * 24 * 3600, samesite="Lax", httponly=True)
    return resp


@bp.route("/")
def index():
    solved = _solved()
    subjects = content.load_subjects(_content_dir(), g.lang)
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
    subj, _, _ = content.find(_content_dir(), subject_slug, lang=g.lang)
    if not subj:
        abort(404)
    solved = _solved()
    progress = {b.slug: _progress(subj, b, solved) for b in subj.blocks}
    return render_template("subject.html", subject=subj, progress=progress)


@bp.route("/<subject_slug>/<block_slug>/")
def block(subject_slug, block_slug):
    subj, blk, _ = content.find(_content_dir(), subject_slug, block_slug, lang=g.lang)
    if not blk:
        abort(404)
    segments = []
    for kind, value in content.parse_lesson(blk.theory_md):
        if kind == "md":
            segments.append(("md", render_md(value, subj.math)))
        elif kind == "drill":
            drill = blk.task(value)
            if drill is not None:
                segments.append(("drill", drill))
        else:
            segments.append(("quiz", {
                "question": render_md(value["question"], subj.math),
                "options": [(render_inline_md(text, subj.math), ok) for text, ok in value["options"]],
                "explanation": render_inline_md(value["explanation"], subj.math) if value["explanation"] else "",
            }))
    solved = _solved()
    idx = subj.blocks.index(blk)
    return render_template("block.html", subject=subj, block=blk, segments=segments, solved=solved,
                           progress=_progress(subj, blk, solved), render_md=lambda t: render_md(t, subj.math),
                           has_code=any(d.type == "code" for d in blk.drills),
                           prev_block=subj.blocks[idx - 1] if idx > 0 else None,
                           next_block=subj.blocks[idx + 1] if idx + 1 < len(subj.blocks) else None)


@bp.route("/<subject_slug>/<block_slug>/<task_slug>/")
def task(subject_slug, block_slug, task_slug):
    subj, blk, tsk = content.find(_content_dir(), subject_slug, block_slug, task_slug, lang=g.lang)
    if not tsk:
        abort(404)
    key = task_key(subj, blk, tsk)
    last = db.last_source(g.user["id"], key) if g.user else None
    idx = blk.tasks.index(tsk) if tsk in blk.tasks else -1
    page = "answer_task.html" if tsk.type == "answer" else "task.html"
    return render_template(page, subject=subj, block=blk, task=tsk, key=key, last_source=last,
                           last_answers=last_answers(last) if tsk.type == "answer" else None,
                           description=render_md(tsk.description_md, subj.math), solved=_solved(),
                           next_task=blk.tasks[idx + 1] if 0 <= idx < len(blk.tasks) - 1 else None)


def last_answers(source):
    try:
        data = json.loads(source) if source else {}
    except ValueError:
        return {}
    return data if isinstance(data, dict) else {}


def _fail(message, code):
    abort(make_response(jsonify(error=message), code))


def _read_source():
    data = request.get_json(silent=True) or {}
    source = data.get("source")
    if not isinstance(source, str) or not source.strip():
        _fail(t("Chýba zdrojový kód."), 400)
    if len(source.encode("utf-8")) > current_app.config["MAX_SOURCE_BYTES"]:
        _fail("Source too large", 413)
    return data, source


def _rate_limit():
    if not current_app.extensions["rate_limiter"].allow(g.user["id"], current_app.config["USER_RUNS_PER_MINUTE"]):
        _fail(t("Príliš veľa spustení, počkajte minútu."), 429)


@bp.post("/api/<subject_slug>/<block_slug>/<task_slug>/submit")
@api_login_required
def submit(subject_slug, block_slug, task_slug):
    subj, blk, tsk = content.find(_content_dir(), subject_slug, block_slug, task_slug)
    if not tsk:
        abort(404)
    if tsk.type == "answer":
        _fail("Use the check endpoint for answer tasks", 400)
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


@bp.post("/api/<subject_slug>/<block_slug>/<task_slug>/check")
@api_login_required
def check(subject_slug, block_slug, task_slug):
    """Answer tasks: compare typed answers with the key in answers.json."""
    subj, blk, tsk = content.find(_content_dir(), subject_slug, block_slug, task_slug)
    if not tsk or tsk.type != "answer":
        abort(404)
    data = request.get_json(silent=True) or {}
    answers = data.get("answers")
    if not isinstance(answers, dict):
        _fail(t("Chýbajú odpovede."), 400)
    raw = json.dumps(answers, ensure_ascii=False)
    if len(raw.encode("utf-8")) > current_app.config["MAX_SOURCE_BYTES"]:
        _fail("Answers too large", 413)
    report = mathcheck.check_task(tsk.parts, answers)
    key = task_key(subj, blk, tsk)
    db.record_submission(g.user["id"], key, report, raw)
    current_app.logger.info("check %s by %s -> %s (%d/%d)", key, g.user["username"],
                            report.verdict, report.passed, report.total)
    return jsonify(report.to_dict())


@bp.app_errorhandler(404)
def not_found(_):
    if request.path.startswith("/api/"):
        return jsonify(error="Not found"), 404
    return render_template("404.html"), 404

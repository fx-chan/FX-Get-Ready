"""Minimal accounts: username + password, no e-mail. Session cookie based."""
import functools
import re
import secrets
import sqlite3
import time
from collections import defaultdict, deque

from flask import (Blueprint, abort, current_app, flash, g, jsonify, make_response, redirect,
                   render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db
from .i18n import t

bp = Blueprint("auth", __name__)

USERNAME_RE = re.compile(r"^[A-Za-z0-9_.-]{3,32}$")
MIN_PASSWORD = 6


def load_user():
    g.user = None
    uid = session.get("user_id")
    if uid is not None:
        g.user = get_db().execute("SELECT id, username FROM users WHERE id = ?", (uid,)).fetchone()


def csrf_token():
    if "csrf" not in session:
        session["csrf"] = secrets.token_urlsafe(32)
    return session["csrf"]


def check_csrf():
    sent = request.form.get("csrf") or request.headers.get("X-CSRF-Token")
    if not sent or not secrets.compare_digest(sent, session.get("csrf", "")):
        abort(400, "CSRF token invalid")


def api_login_required(view):
    @functools.wraps(view)
    def wrapped(*args, **kwargs):
        if g.user is None:
            abort(make_response(jsonify(error=t("Prihláste sa, prosím."), login=True), 401))
        check_csrf()
        return view(*args, **kwargs)
    return wrapped


class RateLimiter:
    """Sliding one-minute window per user, in process memory (one worker on PythonAnywhere)."""

    def __init__(self, clock=time.monotonic):
        self.clock = clock
        self.hits = defaultdict(deque)

    def allow(self, key, per_minute):
        now = self.clock()
        q = self.hits[key]
        while q and now - q[0] > 60:
            q.popleft()
        if len(q) >= per_minute:
            return False
        q.append(now)
        return True


def _safe_next(target):
    return target if target and target.startswith("/") and not target.startswith("//") else url_for("main.index")


@bp.route("/register", methods=["GET", "POST"])
def register():
    if not current_app.config["ALLOW_REGISTRATION"]:
        abort(404)
    if request.method == "POST":
        check_csrf()
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        error = None
        if not USERNAME_RE.match(username):
            error = t("Meno: 3–32 znakov (písmená, čísla, _ . -).")
        elif len(password) < MIN_PASSWORD:
            error = t("Heslo musí mať aspoň {n} znakov.", n=MIN_PASSWORD)
        elif password != request.form.get("password2", ""):
            error = t("Heslá sa nezhodujú.")
        if error is None:
            try:
                db = get_db()
                cur = db.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                                 (username, generate_password_hash(password)))
                db.commit()
            except sqlite3.IntegrityError:
                error = t("Toto meno je obsadené.")
            else:
                session.clear()
                session["user_id"] = cur.lastrowid
                return redirect(_safe_next(request.args.get("next")))
        flash(error, "error")
    return render_template("auth.html", mode="register")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        check_csrf()
        username = request.form.get("username", "").strip()
        user = get_db().execute("SELECT id, password_hash FROM users WHERE username = ?", (username,)).fetchone()
        if user and check_password_hash(user["password_hash"], request.form.get("password", "")):
            session.clear()
            session.permanent = True
            session["user_id"] = user["id"]
            return redirect(_safe_next(request.args.get("next")))
        flash(t("Nesprávne meno alebo heslo."), "error")
    return render_template("auth.html", mode="login")


@bp.post("/logout")
def logout():
    check_csrf()
    session.clear()
    return redirect(url_for("main.index"))

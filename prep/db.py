"""SQLite storage for accounts and submissions (stdlib only, fine for PythonAnywhere)."""
import sqlite3

from flask import current_app, g

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE COLLATE NOCASE,
    password_hash TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS submissions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    task_key TEXT NOT NULL,
    verdict TEXT NOT NULL,
    passed INTEGER NOT NULL,
    total INTEGER NOT NULL,
    source TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS submissions_user_task ON submissions(user_id, task_key);
"""


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(_=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_app(app):
    app.config["DATABASE"].parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(app.config["DATABASE"]) as conn:
        conn.executescript(SCHEMA)
    app.teardown_appcontext(close_db)


def record_submission(user_id, task_key, report, source):
    db = get_db()
    db.execute("INSERT INTO submissions (user_id, task_key, verdict, passed, total, source) VALUES (?,?,?,?,?,?)",
               (user_id, task_key, report.verdict, report.passed, report.total, source))
    db.commit()


def solved_keys(user_id):
    rows = get_db().execute("SELECT DISTINCT task_key FROM submissions WHERE user_id = ? AND verdict = 'AC'",
                            (user_id,))
    return {r["task_key"] for r in rows}


def last_source(user_id, task_key):
    row = get_db().execute("SELECT source FROM submissions WHERE user_id = ? AND task_key = ? "
                           "ORDER BY id DESC LIMIT 1", (user_id, task_key)).fetchone()
    return row["source"] if row else None

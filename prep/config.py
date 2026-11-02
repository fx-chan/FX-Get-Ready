"""App settings.

Priority: PREP_<NAME> environment variable > config.local.json > default below.
config.local.json holds secrets (API key, SECRET_KEY) and is never committed;
copy config.example.json to start.
"""
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOCAL_CONFIG = Path(os.environ.get("PREP_LOCAL_CONFIG", BASE_DIR / "config.local.json"))

try:
    _LOCAL = json.loads(LOCAL_CONFIG.read_text(encoding="utf-8"))
except FileNotFoundError:
    _LOCAL = {}


def _get(name, default):
    return os.environ.get(f"PREP_{name}", _LOCAL.get(name, default))


def _bool(name, default):
    return str(_get(name, default)).lower() in ("1", "true", "yes")


class Config:
    SECRET_KEY = _get("SECRET_KEY", "dev-change-me")
    CONTENT_DIR = Path(_get("CONTENT_DIR", BASE_DIR / "content"))
    DATABASE = Path(_get("DATABASE", BASE_DIR / "instance" / "prep.sqlite"))

    # "onlinecompiler", "judge0", "piston", or "local" (dev only, uses your gcc).
    COMPILER_BACKEND = _get("COMPILER_BACKEND", "onlinecompiler")

    ONLINECOMPILER_URL = _get("ONLINECOMPILER_URL", "https://api.onlinecompiler.io")
    ONLINECOMPILER_KEY = _get("ONLINECOMPILER_KEY", "")
    ONLINECOMPILER_COMPILER = _get("ONLINECOMPILER_COMPILER", "gcc-15")

    JUDGE0_URL = _get("JUDGE0_URL", "https://ce.judge0.com")
    JUDGE0_KEY = _get("JUDGE0_KEY", "")
    JUDGE0_HOST = _get("JUDGE0_HOST", "")
    JUDGE0_LANGUAGE_ID = int(_get("JUDGE0_LANGUAGE_ID", 50))

    PISTON_URL = _get("PISTON_URL", "https://emkc.org/api/v2/piston")
    PISTON_TOKEN = _get("PISTON_TOKEN", "")

    HTTP_TIMEOUT = float(_get("HTTP_TIMEOUT", 40))
    MAX_SOURCE_BYTES = int(_get("MAX_SOURCE_BYTES", 64 * 1024))
    MAX_STDIN_BYTES = int(_get("MAX_STDIN_BYTES", 16 * 1024))
    # Stop judging at the first failing test to save API quota.
    STOP_ON_FIRST_FAIL = _bool("STOP_ON_FIRST_FAIL", True)
    # Runs + submits per user per minute (the free API allows 30/min for the whole site).
    USER_RUNS_PER_MINUTE = int(_get("USER_RUNS_PER_MINUTE", 6))
    ALLOW_REGISTRATION = _bool("ALLOW_REGISTRATION", True)

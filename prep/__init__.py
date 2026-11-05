import logging
from datetime import timedelta

from flask import Flask, g

from . import auth, db, i18n
from .config import Config
from .runners import make_runner


def set_language():
    g.lang = i18n.pick_language()


def create_app(overrides=None, runner=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.update(SESSION_COOKIE_SAMESITE="Lax", SESSION_COOKIE_HTTPONLY=True,
                      PERMANENT_SESSION_LIFETIME=timedelta(days=30))
    if overrides:
        app.config.update(overrides)
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    # Tests pass a fake runner; normally it is built from config.
    app.extensions["runner"] = runner or make_runner(app.config)
    app.extensions["rate_limiter"] = auth.RateLimiter()

    db.init_app(app)
    app.before_request(auth.load_user)
    app.before_request(set_language)
    app.jinja_env.globals.update(csrf_token=auth.csrf_token, _=i18n.t, lang=i18n.current, js_strings=i18n.js_strings,
                                 languages=i18n.LANGS)

    from .views import bp
    app.register_blueprint(auth.bp)
    app.register_blueprint(bp)
    return app

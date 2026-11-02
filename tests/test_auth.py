from prep.auth import RateLimiter

from conftest import csrf_of, register


def test_register_logs_in(make_client):
    c = make_client()
    r = register(c, "Jana", "heslo123")
    assert r.status_code == 302
    assert "Jana" in c.get("/").get_data(as_text=True)


def test_register_validation(make_client):
    c = make_client()
    assert "3–32 znakov" in register(c, "ab", "heslo123").get_data(as_text=True)
    assert "aspoň 6" in register(c, "jana", "123").get_data(as_text=True)
    token = csrf_of(c)
    r = c.post("/register", data={"csrf": token, "username": "jana", "password": "heslo123", "password2": "ine"})
    assert "nezhodujú" in r.get_data(as_text=True)


def test_duplicate_username_case_insensitive(make_client):
    c = make_client()
    register(c, "Jana", "heslo123")
    c2 = c.application.test_client()
    assert "obsadené" in register(c2, "jana", "heslo456").get_data(as_text=True)


def test_login_logout(make_client):
    app_client = make_client()
    register(app_client, "peter", "heslo123")
    c = app_client.application.test_client()
    token = csrf_of(c)
    bad = c.post("/login", data={"csrf": token, "username": "peter", "password": "zle"})
    assert "Nesprávne" in bad.get_data(as_text=True)
    ok = c.post("/login?next=/demo/", data={"csrf": token, "username": "peter", "password": "heslo123"})
    assert ok.status_code == 302 and ok.headers["Location"].endswith("/demo/")
    assert "peter" in c.get("/").get_data(as_text=True)
    c.post("/logout", data={"csrf": csrf_of(c)})
    assert "Prihlásiť" in c.get("/").get_data(as_text=True)


def test_login_rejects_open_redirect(make_client):
    app_client = make_client()
    register(app_client, "eva", "heslo123")
    c = app_client.application.test_client()
    r = c.post("/login?next=//evil.example", data={"csrf": csrf_of(c), "username": "eva", "password": "heslo123"})
    assert r.headers["Location"] == "/"


def test_forms_need_csrf(make_client):
    c = make_client()
    r = c.post("/register", data={"username": "jana", "password": "heslo123", "password2": "heslo123"})
    assert r.status_code == 400


def test_passwords_are_hashed(make_client):
    c = make_client()
    register(c, "jana", "heslo123")
    import sqlite3
    with sqlite3.connect(c.application.config["DATABASE"]) as db:
        stored = db.execute("SELECT password_hash FROM users").fetchone()[0]
    assert "heslo123" not in stored and stored.startswith(("scrypt:", "pbkdf2:"))


def test_registration_can_be_disabled(make_client):
    assert make_client(ALLOW_REGISTRATION=False).get("/register").status_code == 404


def test_rate_limiter_window():
    now = [0.0]
    rl = RateLimiter(clock=lambda: now[0])
    assert rl.allow(1, 2) and rl.allow(1, 2) and not rl.allow(1, 2)
    assert rl.allow(2, 2)  # per user
    now[0] = 61
    assert rl.allow(1, 2)

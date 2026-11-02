from prep.runners import COMPILE_ERROR, OK, RunResult

from conftest import FakeRunner, doubling

URL = "/api/demo/cv01/01_double"


def test_pages_render(make_client):
    c = make_client()
    assert "Demo" in c.get("/").get_data(as_text=True)
    assert "CV 1" in c.get("/demo/").get_data(as_text=True)
    task_page = c.get("/demo/cv01/01_double/").get_data(as_text=True)
    assert "<strong>dvojnásobok</strong>" in task_page and "int main(void){return 0;}" in task_page


def test_lesson_renders_quiz_and_drill(make_client):
    page = make_client().get("/demo/cv01/").get_data(as_text=True)
    assert "<h2>Teória</h2>" in page
    assert 'data-quiz' in page and 'data-ok="1"' in page and "Lebo matematika." in page
    assert 'id="d-echo"' in page and "Vypíš súbor." in page and 'class="code-widget compact"' in page
    assert "missing-drill" not in page  # unknown drill reference is skipped, not a crash


def test_hidden_tests_not_in_page(make_client):
    page = make_client().get("/demo/cv01/01_double/").get_data(as_text=True)
    assert "42" not in page  # expected output of a hidden test (2*21)


def test_404s(api_client):
    c = api_client()
    assert c.get("/nope/").status_code == 404
    assert c.get("/demo/cv01/nope/").status_code == 404
    r = c.post("/api/demo/cv01/nope/submit", json={"source": "x"})
    assert r.status_code == 404 and r.get_json()["error"]


def test_api_requires_login(make_client):
    c = make_client(FakeRunner(fn=doubling))
    r = c.post(f"{URL}/submit", json={"source": "x"})
    assert r.status_code == 401 and r.get_json()["login"] is True
    assert c.post(f"{URL}/run", json={"source": "x"}).status_code == 401


def test_api_requires_csrf(api_client):
    c = api_client()
    assert c.client.post(f"{URL}/submit", json={"source": "x"}).status_code == 400
    assert c.client.post(f"{URL}/submit", json={"source": "x"},
                         headers={"X-CSRF-Token": "wrong"}).status_code == 400


def test_submit_accepted_marks_solved(api_client):
    c = api_client(FakeRunner(fn=doubling))
    r = c.post(f"{URL}/submit", json={"source": "int main(){}"})
    data = r.get_json()
    assert r.status_code == 200
    assert data["verdict"] == "AC" and data["passed"] == 3 and data["total"] == 3
    block_page = c.get("/demo/cv01/").get_data(as_text=True)
    assert '<li class="solved">' in block_page and "1 / 2 hotovo" in block_page
    # The last submitted code is restored on the task page.
    assert "int main(){}" in c.get("/demo/cv01/01_double/").get_data(as_text=True)


def test_submit_compile_error(api_client):
    runner = FakeRunner([RunResult(COMPILE_ERROR, compile_output="oops")])
    data = api_client(runner).post(f"{URL}/submit", json={"source": "x"}).get_json()
    assert data["verdict"] == "CE" and data["compile_output"] == "oops"


def test_submit_validation(api_client):
    c = api_client()
    assert c.post(f"{URL}/submit", json={}).status_code == 400
    assert c.post(f"{URL}/submit", json={"source": "   "}).status_code == 400
    assert c.post(f"{URL}/submit", data="not json").status_code == 400
    assert c.post(f"{URL}/submit", json={"source": "x" * 70_000}).status_code == 413


def test_run_custom_stdin(api_client):
    runner = FakeRunner([RunResult(OK, stdout="hi\n")])
    data = api_client(runner).post(f"{URL}/run", json={"source": "x", "stdin": "abc"}).get_json()
    assert data["status"] == "ok" and data["stdout"] == "hi\n"
    assert runner.calls == [("x", "abc", None)]


def test_run_gets_task_input_files(api_client):
    runner = FakeRunner([RunResult(OK, stdout="")])
    api_client(runner).post("/api/demo/cv01/d-echo/run", json={"source": "x"})
    assert runner.calls[0][2] == {"data.txt": "shared\n"}


def test_run_rejects_bad_stdin(api_client):
    assert api_client().post(f"{URL}/run", json={"source": "x", "stdin": 5}).status_code == 400


def test_rate_limit_per_user(api_client):
    c = api_client(FakeRunner(fn=doubling), USER_RUNS_PER_MINUTE=2)
    assert c.post(f"{URL}/submit", json={"source": "x"}).status_code == 200
    assert c.post(f"{URL}/run", json={"source": "x", "stdin": "1"}).status_code == 200
    r = c.post(f"{URL}/submit", json={"source": "x"})
    assert r.status_code == 429 and "minútu" in r.get_json()["error"]

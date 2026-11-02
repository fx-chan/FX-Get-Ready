# Prep — príprava na písomky a skúšky

Flask platform for practising for written tests (písomky) and exams (skúšky). Subject: **PRPR** (C).

- lessons (theory from lectures P1–P7) with **quizzes** and **mini drills** (fill in a line of code) embedded in the text,
- practice tasks from the exercise sheets CV1–CV7 plus a **final test** block (from the sample test photo),
- accounts (username + password, no e-mail), progress, last submitted code,
- the server never compiles code itself: it sends the code and hidden test inputs to an external
  compiler API (default **onlinecompiler.io**) and compares stdout with the expected `.out` files.

## Run locally

```bash
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt     # Linux/macOS: .venv/bin/pip
copy config.example.json config.local.json         # then put your API key in it
.venv/Scripts/python run.py                        # http://127.0.0.1:5000
.venv/Scripts/python -m pytest -q
```

## Configuration

Priority: environment variable `PREP_<NAME>` > `config.local.json` > default. `config.local.json`
holds secrets and is git-ignored.

| Name | Default | Notes |
|---|---|---|
| `SECRET_KEY` | dev value | **required in production**, long random string (signs session cookies) |
| `COMPILER_BACKEND` | `onlinecompiler` | `onlinecompiler`, `judge0`, `piston`, `local` |
| `ONLINECOMPILER_KEY` | – | API key from api.onlinecompiler.io |
| `ONLINECOMPILER_COMPILER` | `gcc-15` | compiler id at onlinecompiler.io |
| `USER_RUNS_PER_MINUTE` | `6` | per-user limit; the free API allows 30 runs/min for the whole site |
| `STOP_ON_FIRST_FAIL` | `true` | stop judging at the first failed test (saves quota) |
| `ALLOW_REGISTRATION` | `true` | set `false` to close sign-ups |
| `DATABASE` | `instance/prep.sqlite` | SQLite file, created automatically |
| `CONTENT_DIR` | `content/` | |

Quota math: every test of a submission is one API run. Free plan = 100 000 runs/month,
30 runs/minute, 2 at once; the runner retries briefly on HTTP 429.

### Compiling locally (no API)

`COMPILER_BACKEND=local` uses the `gcc` on your PATH (`gcc -O2 code.c -o code -lm`, the same flags as
onlinecompiler.io) in a temporary folder. It is **not a sandbox** — only for development.
Note that onlinecompiler.io uses GCC 15 (default standard C23, implicit function declarations are
errors), while an old local gcc may be more permissive.

## Content

```
content/<subject>/subject.json                 {"title", "summary"}
content/<subject>/<block>/block.json           {"title", "summary", "lecture"}
content/<subject>/<block>/theory.md            lesson, may embed drills and quizzes
content/<subject>/<block>/tasks/<task>/        practice task (own page with editor)
content/<subject>/<block>/drills/<drill>/      mini exercise shown inside the lesson
  metadata.json   {"title", "difficulty", "limits": {"time"}, "checker": "lines|exact|tokens", "public_tests": ["01"]}
  description.md  template.c  solution.c (never served)
  tests/01.in, 01.out, ...
  files/<name>             input files every test gets in its working directory (optional)
  tests/01.files/<name>    input files for one test (optional, replaces files/)
```

Lesson syntax in `theory.md`:

```
::: drill d1-scanf          ← embeds drills/d1-scanf

::: quiz
Question text (markdown)
- [ ] wrong
- [x] right
> explanation shown after answering
:::
```

**Never write `.out` files by hand** — write `solution.c` and `.in` files, then:

```bash
.venv/Scripts/python tools/build_outputs.py                                   # create missing .out (local gcc)
.venv/Scripts/python tools/build_outputs.py --check --backend onlinecompiler  # verify on the production compiler
```

The test suite also checks that every reference solution passes, every unchanged drill template
fails, every drill is embedded in its lesson and every quiz has exactly one right answer.

## PythonAnywhere

1. Upload the project, create a virtualenv, `pip install -r requirements.txt`.
2. Create `config.local.json` next to `wsgi.py` (`SECRET_KEY`, `ONLINECOMPILER_KEY`).
3. Web tab → Manual configuration → WSGI file:
   ```python
   import sys; sys.path.insert(0, "/home/<user>/Prep_web_proj")
   from wsgi import application
   ```
4. Static files: URL `/static/` → `/home/<user>/Prep_web_proj/prep/static`.
5. Force HTTPS in the Web tab (login sends passwords).
6. **Free accounts can only reach allow-listed hosts.** Check that `api.onlinecompiler.io` is on the
   PythonAnywhere allowlist (or request it); otherwise every run returns *IE*.

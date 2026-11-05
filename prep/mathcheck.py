"""Checking typed answers for math tasks (no code, no external API).

An answer task keeps its key in answers.json (never served):

    {"parts": [{"id": "a", "prompt": "$A+B$", "kind": "matrix", "answer": [["1", "2"]]}, ...]}

Kinds and their fields:
    number      answer: expression string, or null = "cannot be computed"
    matrix      answer: list of rows of expressions, or null
    vector      answer: list of expressions (row or column accepted), or null
    dims        answer: [rows, cols], or null
    choice      options: [...], answer: index of the right option
    multi       options: [...], answer: list of indices
    set         answer: list of distinct values (order and repeats ignored); [] = no value
    multiset    answer: list of values with multiplicity (order ignored)
    system      A, b: the student gives a (parametric) solution or "no solution"
    eigbasis    A, lambda: the student gives a basis of the eigenspace
    diagonalize A, diagonalizable: the student gives P with P^-1 A P diagonal, or "not diagonalizable"
    elem_product A: the student gives elementary matrices whose product is A
    row_equiv   A, B: the student gives an invertible C with C A = B
    power_identity n, p, exclude ("diagonal" | "identity"): a matrix with A^p = I
    pair_not_diff_squares: two 2x2 matrices with (A+B)(A-B) != A^2 - B^2

Optional per part: "vars" (names the student may use, e.g. ["a", "b"]).

Student input for a part is {"value": str | int | list, "none": bool}; "none" is the
"cannot be computed / no solution / no value" checkbox. Expressions are parsed by a
small recursive-descent parser and compared numerically at random points, so
equivalent forms (1/2, 0.5, 2/4, sqrt(4)/4) are all accepted.
"""
import cmath
import math
import random
import re
from fractions import Fraction

from .i18n import t

FUNCS = {
    "sqrt": cmath.sqrt, "sin": cmath.sin, "cos": cmath.cos, "tan": cmath.tan, "exp": cmath.exp,
    "ln": cmath.log, "sinh": cmath.sinh, "cosh": cmath.cosh, "abs": lambda z: complex(abs(z)),
}
CONSTS = {"pi": cmath.pi, "e": cmath.e, "i": 1j}
PARAMS = ["t", "s", "u", "r", "p", "q", "t1", "t2", "t3", "t4"]  # free parameters of a solution set

KINDS = {"number", "matrix", "vector", "dims", "choice", "multi", "set", "multiset", "system", "eigbasis",
         "diagonalize", "elem_product", "row_equiv", "power_identity", "pair_not_diff_squares"}
NONE_LABELS = {
    "number": "nedá sa vypočítať",
    "matrix": "nedá sa vypočítať",
    "vector": "nedá sa vypočítať",
    "dims": "nedá sa vypočítať",
    "set": "žiadna hodnota",
    "system": "systém nemá riešenie",
    "diagonalize": "nie je diagonalizovateľná",
}
MAX_INPUT = 4000


class ParseError(ValueError):
    """Message is a Slovak UI string (translated by i18n when shown)."""

    def __init__(self, message, **args):
        super().__init__(message)
        self.message, self.args_ = message, args

    def text(self, lang=None):
        return t(self.message, lang, **self.args_)


class EvalError(ArithmeticError):
    pass


# --- expressions ---------------------------------------------------------------

_REPLACE = [("−", "-"), ("–", "-"), ("·", "*"), ("⋅", "*"), ("×", "*"), ("√", " sqrt "), ("π", " pi "),
            ("λ", " lambda "), ("θ", " theta "), ("α", " alpha "), ("²", "^2"), ("³", "^3"), ("**", "^"),
            ("[", "("), ("]", ")"), ("{", "("), ("}", ")")]
_TOKEN = re.compile(r"\s*(?:(\d+\.?\d*|\.\d+)|([A-Za-z_][A-Za-z0-9_]*)|(.))")


def _normalize(text):
    for a, b in _REPLACE:
        text = text.replace(a, b)
    return text


def _split_ident(word, names):
    """Split an identifier into known names: 'ab' -> a, b; 'sqrt2' -> sqrt, 2; 'k1' stays if known."""
    out = []
    while word:
        digits = re.match(r"\d+", word)
        if digits:
            out.append(("num", digits.group()))
            word = word[digits.end():]
            continue
        head = next((word[:n] for n in range(len(word), 0, -1) if word[:n] in names), None)
        if head is None:
            raise ParseError("neznámy symbol „{x}“", x=word)
        out.append(("id", head))
        word = word[len(head):]
    return out


def tokenize(text, names):
    tokens = []
    for num, ident, op in _TOKEN.findall(_normalize(text)):
        if num:
            tokens.append(("num", num))
        elif ident:
            tokens.extend(_split_ident(ident, names))
        elif op.strip():
            if op not in "+-*/^()":
                raise ParseError("neznámy znak „{x}“", x=op)
            tokens.append(("op", op))
    return tokens


class _Parser:
    def __init__(self, tokens, variables):
        self.t, self.i, self.vars = tokens, 0, variables

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else (None, None)

    def take(self):
        tok = self.peek()
        self.i += 1
        return tok

    def expect(self, op):
        if self.take() != ("op", op):
            raise ParseError("chýba „{x}“", x=op)

    def parse(self):
        if not self.t:
            raise ParseError("prázdny výraz")
        node = self.expr()
        if self.i != len(self.t):
            raise ParseError("nečakaný koniec výrazu")
        return node

    def expr(self):
        node = self.term()
        while self.peek() in (("op", "+"), ("op", "-")):
            op = self.take()[1]
            node = (op, node, self.term())
        return node

    def starts_primary(self):
        kind, val = self.peek()
        return kind in ("num", "id") or (kind, val) == ("op", "(")

    def term(self):
        node = self.unary()
        while True:
            if self.peek() in (("op", "*"), ("op", "/")):
                op = self.take()[1]
                node = (op, node, self.unary())
            elif self.starts_primary():           # implicit multiplication: 2t, 3sqrt(2), (a+b)(a-b)
                node = ("*", node, self.power())
            else:
                return node

    def unary(self):
        if self.peek() == ("op", "-"):
            self.take()
            return ("neg", self.unary())
        if self.peek() == ("op", "+"):
            self.take()
            return self.unary()
        return self.power()

    def power(self):
        base = self.primary()
        if self.peek() == ("op", "^"):
            self.take()
            return ("^", base, self.unary())
        return base

    def primary(self):
        kind, val = self.take()
        if kind == "num":
            return ("num", Fraction(val))
        if kind == "id":
            if val in FUNCS:
                if self.peek() == ("op", "("):
                    self.take()
                    arg = self.expr()
                    self.expect(")")
                else:
                    arg = self.power()
                return ("fn", val, arg)
            if val in self.vars:
                return ("var", val)
            return ("const", val)
        if (kind, val) == ("op", "("):
            node = self.expr()
            self.expect(")")
            return node
        raise ParseError("neúplný výraz")


def parse_expr(text, variables=()):
    if not isinstance(text, str):
        text = str(text)
    variables = set(variables)
    names = set(FUNCS) | variables | {c for c in CONSTS if c not in variables}
    return _Parser(tokenize(text, names), variables).parse()


def evaluate(node, env):
    tag = node[0]
    try:
        if tag == "num":
            return complex(node[1])
        if tag == "var":
            return env[node[1]]
        if tag == "const":
            return CONSTS[node[1]]
        if tag == "neg":
            return 0 - evaluate(node[1], env)     # not -x: keeps +0.0j, so sqrt(-3) = +i*sqrt(3)
        if tag == "fn":
            return FUNCS[node[1]](evaluate(node[2], env))
        a, b = evaluate(node[1], env), evaluate(node[2], env)
        if tag == "+":
            return a + b
        if tag == "-":
            return a - b
        if tag == "*":
            return a * b
        if tag == "/":
            return a / b
        if tag == "^":
            if b == int(b.real) and b.imag == 0 and abs(b.real) <= 64:
                return a ** int(b.real)
            return a ** b
    except (ZeroDivisionError, OverflowError, ValueError) as exc:
        raise EvalError(str(exc)) from exc
    raise EvalError("bad node")


def free_names(node):
    if node[0] == "var":
        return {node[1]}
    return set().union(*(free_names(c) for c in node[1:] if isinstance(c, tuple)))


def _rng(seed):
    return random.Random(seed)


def _envs(variables, count=4, seed=12345):
    rnd = _rng(seed)
    return [{v: complex(rnd.uniform(0.3, 1.7)) for v in variables} for _ in range(count)]


def _close(a, b, loose):
    tol = 5e-3 if loose else 1e-7
    return abs(a - b) <= tol * max(1.0, abs(b))


def same_value(expected, given_text, variables=()):
    """True if the student's expression equals the expected one at several random points."""
    given_text = str(given_text).replace(",", ".")      # decimal comma: 0,5
    exp_node = parse_expr(expected, variables)
    got_node = parse_expr(given_text, variables)
    loose = "." in given_text
    checked = 0
    for env in _envs(variables, 6):
        try:
            e, g = evaluate(exp_node, env), evaluate(got_node, env)
        except EvalError:
            continue
        if not _close(g, e, loose):
            return False
        checked += 1
    return checked > 0


# --- matrices ----------------------------------------------------------------------

def _unwrap(s):
    """Drop brackets/bars around a whole row: '[1 2]', '(1, 2)', '|1 2|' (but not '(a+1)/2')."""
    s = s.strip()
    while len(s) >= 2 and s[0] in "[(|" and s[-1] == {"[": "]", "(": ")", "|": "|"}[s[0]]:
        depth = 0
        for k, ch in enumerate(s):
            depth += ch in "[(" and 1 or 0
            depth -= ch in "])" and 1 or 0
            if depth == 0 and s[0] != "|" and k < len(s) - 1:
                return s                     # the first bracket closes early: it is part of an entry
        s = s[1:-1].strip()
    return s


def parse_rows(text):
    """'1 2; 3 4' or lines; entries split by commas when a row has one, else by spaces."""
    text = text.strip()
    rows = []
    for line in re.split(r"[;\n]", text):
        line = _unwrap(line.replace("[", "(").replace("]", ")")) if line.strip() else ""
        if not line:
            continue
        cells = [c.strip() for c in line.split(",")] if "," in line else line.split()
        if any(not c for c in cells):
            raise ParseError("prázdny prvok")
        rows.append(cells)
    if not rows:
        raise ParseError("prázdna odpoveď")
    if len({len(r) for r in rows}) != 1:
        raise ParseError("riadky majú rôzny počet prvkov")
    return rows


def parse_matrix_list(text):
    """Matrices separated by an empty line."""
    blocks = [b for b in re.split(r"\n\s*\n", text.strip()) if b.strip()]
    if not blocks:
        raise ParseError("prázdna odpoveď")
    return [parse_rows(b) for b in blocks]


def numeric_matrix(rows, variables=(), env=None):
    env = env or {}
    return [[evaluate(parse_expr(c, variables), env) for c in row] for row in rows]


def as_vector(rows):
    if len(rows) == 1:
        return rows[0]
    if all(len(r) == 1 for r in rows):
        return [r[0] for r in rows]
    raise ParseError("očakáva sa vektor (jeden riadok alebo stĺpec)")


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def identity(n):
    return [[1.0 + 0j if i == j else 0j for j in range(n)] for i in range(n)]


def num_rank(rows, tol=1e-8):
    m = [list(map(complex, r)) for r in rows]
    if not m:
        return 0
    rank, cols = 0, len(m[0])
    scale = max([abs(x) for r in m for x in r] + [1.0])
    for c in range(cols):
        piv = max(range(rank, len(m)), key=lambda r: abs(m[r][c]), default=None)
        if piv is None or abs(m[piv][c]) <= tol * scale:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        for r in range(len(m)):
            if r != rank:
                f = m[r][c] / m[rank][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[rank])]
        rank += 1
        if rank == len(m):
            break
    return rank


def num_inverse(a):
    n = len(a)
    m = [list(map(complex, r)) + identity(n)[i] for i, r in enumerate(a)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(m[r][c]))
        if abs(m[piv][c]) < 1e-12:
            return None
        m[c], m[piv] = m[piv], m[c]
        p = m[c][c]
        m[c] = [x / p for x in m[c]]
        for r in range(n):
            if r != c:
                f = m[r][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[c])]
    return [r[n:] for r in m]


def exact_rank(rows):
    m = [[Fraction(x) for x in r] for r in rows]
    rank = 0
    for c in range(len(m[0]) if m else 0):
        piv = next((r for r in range(rank, len(m)) if m[r][c] != 0), None)
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        for r in range(len(m)):
            if r != rank and m[r][c] != 0:
                f = m[r][c] / m[rank][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[rank])]
        rank += 1
    return rank


def _all_close(a, b, tol=1e-7):
    return len(a) == len(b) and all(
        len(ra) == len(rb) and all(abs(x - y) <= tol * max(1.0, abs(y)) for x, y in zip(ra, rb))
        for ra, rb in zip(a, b))


def is_elementary(m, tol=1e-9):
    n = len(m)
    if any(len(r) != n for r in m):
        return False
    diff = [(i, j) for i in range(n) for j in range(n) if abs(m[i][j] - (1 if i == j else 0)) > tol]
    if not diff:
        return False                       # the identity itself is not counted as an operation
    if len(diff) == 1:
        i, j = diff[0]
        return i != j or abs(m[i][i]) > tol    # one off-diagonal entry, or one non-zero scale
    rows = sorted({i for i, _ in diff})
    if len(rows) == 2:                       # swap of two rows
        a, b = rows
        return (sorted(diff) == [(a, a), (a, b), (b, a), (b, b)] and abs(m[a][a]) < tol and abs(m[b][b]) < tol
                and abs(m[a][b] - 1) < tol and abs(m[b][a] - 1) < tol)
    return False


# --- checking ----------------------------------------------------------------------

OK, WRONG, INVALID = "ok", "wrong", "invalid"


def public_part(part):
    """What the page may show: everything except the key."""
    return {k: v for k, v in part.items() if k in ("id", "prompt", "kind", "options", "vars", "hint")}


def _text(value):
    if not isinstance(value, str):
        raise ParseError("chýba odpoveď")
    if len(value) > MAX_INPUT:
        raise ParseError("príliš dlhá odpoveď")
    if not value.strip():
        raise ParseError("chýba odpoveď")
    return value


def _check_matrix(expected, text, variables):
    rows = parse_rows(text)
    if len(rows) != len(expected) or len(rows[0]) != len(expected[0]):
        for r in rows:
            for c in r:
                parse_expr(c, variables)   # surface syntax errors before saying "wrong"
        return WRONG
    ok = all(same_value(e, g, variables) for er, gr in zip(expected, rows) for e, g in zip(er, gr))
    return OK if ok else WRONG


def _values(text, variables):
    parts = [p.strip() for p in re.split(r"[;,]", text.strip().strip("{}"))]
    parts = [p for p in parts if p]
    if not parts:
        raise ParseError("prázdna odpoveď")
    for p in parts:
        parse_expr(p, variables)
    return parts


def _match_multiset(expected, given, variables):
    env_list = _envs(variables, 2)
    left = list(given)
    for e in expected:
        hit = next((g for g in left if all(
            _close(evaluate(parse_expr(g, variables), env), evaluate(parse_expr(e, variables), env), "." in g)
            for env in env_list)), None)
        if hit is None:
            return False
        left.remove(hit)
    return not left


def _check_system(part, ans):
    a = [[Fraction(str(x)) for x in row] for row in part["A"]]
    b = [Fraction(str(x)) for x in part["b"]]
    rank_a = exact_rank(a)
    consistent = rank_a == exact_rank([row + [bi] for row, bi in zip(a, b)])
    if ans.get("none"):
        return OK if not consistent else WRONG
    text = _text(ans.get("value"))
    vec = as_vector(parse_rows(text))
    n = len(a[0])
    nodes = [parse_expr(v, PARAMS) for v in vec]
    if not consistent or len(vec) != n:
        return WRONG
    used = sorted(set().union(*(free_names(x) for x in nodes)))
    af = [[complex(x) for x in r] for r in a]
    bf = [complex(x) for x in b]

    def at(env):
        return [evaluate(x, env) for x in nodes]

    for env in _envs(used, 3, seed=7):
        x = at(env)
        if any(abs(sum(c * xi for c, xi in zip(row, x)) - bi) > 1e-7 * max(1.0, abs(bi)) for row, bi in zip(af, bf)):
            return WRONG
    base = _envs(used, 1, seed=99)[0]
    x0 = at(base)
    dirs = []
    for p in used:
        step = dict(base, **{p: base[p] + 1})
        dirs.append([u - v for u, v in zip(at(step), x0)])
    return OK if num_rank(dirs) == n - rank_a else WRONG


def _check_eigbasis(part, text):
    a = numeric_matrix(part["A"])
    lam = evaluate(parse_expr(part["lambda"]), {})
    n = len(a)
    shifted = [[a[i][j] - (lam if i == j else 0) for j in range(n)] for i in range(n)]
    rows = parse_rows(text)
    if len(rows) == n and len(rows[0]) == 1:
        rows = [[r[0] for r in rows]]          # a single column vector
    vecs = numeric_matrix(rows)
    if any(len(v) != n for v in vecs):
        return WRONG
    for v in vecs:
        if max(abs(x) for x in v) < 1e-12:
            return WRONG
        if any(abs(sum(shifted[i][j] * v[j] for j in range(n))) > 1e-7 * max(1.0, max(abs(x) for x in v))
               for i in range(n)):
            return WRONG
    dim = n - num_rank(shifted)
    return OK if len(vecs) == dim and num_rank(vecs) == dim else WRONG


def _check_diagonalize(part, ans):
    if ans.get("none"):
        return OK if not part["diagonalizable"] else WRONG
    p = numeric_matrix(parse_rows(_text(ans.get("value"))))
    a = numeric_matrix(part["A"])
    if not part["diagonalizable"] or len(p) != len(a) or len(p[0]) != len(a):
        return WRONG
    inv = num_inverse(p)
    if inv is None:
        return WRONG
    d = matmul(matmul(inv, a), p)
    off = max(abs(d[i][j]) for i in range(len(d)) for j in range(len(d)) if i != j)
    return OK if off < 1e-7 * max(1.0, max(abs(x) for r in a for x in r)) else WRONG


def _check_elem_product(part, text):
    mats = [numeric_matrix(m) for m in parse_matrix_list(text)]
    target = numeric_matrix(part["A"])
    if not all(is_elementary(m) and len(m) == len(target) for m in mats):
        return WRONG
    prod = mats[0]
    for m in mats[1:]:
        prod = matmul(prod, m)
    return OK if _all_close(prod, target) else WRONG


def _check_row_equiv(part, text):
    c = numeric_matrix(parse_rows(text))
    a, b = numeric_matrix(part["A"]), numeric_matrix(part["B"])
    if len(c) != len(a) or len(c[0]) != len(a) or num_inverse(c) is None:
        return WRONG
    return OK if _all_close(matmul(c, a), b) else WRONG


def _check_power_identity(part, text):
    a = numeric_matrix(parse_rows(text))
    n = part["n"]
    if len(a) != n or len(a[0]) != n:
        return WRONG
    prod = identity(n)
    for _ in range(part["p"]):
        prod = matmul(prod, a)
    if not _all_close(prod, identity(n)):
        return WRONG
    if part.get("exclude") == "diagonal" and all(abs(a[i][j]) < 1e-12 for i in range(n) for j in range(n) if i != j):
        return WRONG
    if part.get("exclude") == "identity" and _all_close(a, identity(n)):
        return WRONG
    return OK


def _check_pair(text):
    mats = [numeric_matrix(m) for m in parse_matrix_list(text)]
    if len(mats) != 2 or any(len(m) != 2 or len(m[0]) != 2 for m in mats):
        return WRONG
    a, b = mats
    s = [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]
    d = [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]
    a2, b2 = matmul(a, a), matmul(b, b)
    return WRONG if _all_close(matmul(s, d), [[a2[i][j] - b2[i][j] for j in range(2)] for i in range(2)]) else OK


def check_part(part, ans):
    """Return (status, message). ans = {"value": ..., "none": bool}."""
    ans = ans if isinstance(ans, dict) else {}
    kind, variables = part["kind"], part.get("vars", [])
    try:
        if kind in ("choice", "multi"):
            value = ans.get("value")
            if kind == "choice":
                ok = str(value) == str(part["answer"])
            else:
                chosen = sorted({int(v) for v in value}) if isinstance(value, list) else None
                ok = chosen == sorted(part["answer"])
            return (OK if ok else WRONG), ""
        if kind == "system":
            return _check_system(part, ans), ""
        if kind == "diagonalize":
            return _check_diagonalize(part, ans), ""
        expected = part.get("answer")
        if ans.get("none"):
            if kind == "set":
                return (OK if expected == [] else WRONG), ""
            return (OK if expected is None and kind in NONE_LABELS else WRONG), ""
        text = _text(ans.get("value"))
        if kind == "number":
            if expected is None:
                parse_expr(text.replace(",", "."), variables)
                return WRONG, ""
            return (OK if same_value(expected, text.replace(",", "."), variables) else WRONG), ""
        if kind == "matrix":
            if expected is None:
                parse_rows(text)
                return WRONG, ""
            return _check_matrix(expected, text, variables), ""
        if kind == "vector":
            vec = as_vector(parse_rows(text))
            if expected is None:
                return WRONG, ""
            if len(vec) != len(expected):
                return WRONG, ""
            return (OK if all(same_value(e, g, variables) for e, g in zip(expected, vec)) else WRONG), ""
        if kind == "dims":
            m = re.fullmatch(r"\s*(\d+)\s*[x×*X]\s*(\d+)\s*", text)
            if not m:
                raise ParseError("zapíšte rozmer v tvare 3x2")
            return (OK if expected is not None and [int(m.group(1)), int(m.group(2))] == list(expected) else WRONG), ""
        if kind == "set":
            given = _values(text, variables)
            uniq = []
            for g in given:
                if not any(same_value(g, u, variables) for u in uniq):
                    uniq.append(g)
            return (OK if len(uniq) == len(expected) and _match_multiset(expected, uniq, variables) else WRONG), ""
        if kind == "multiset":
            return (OK if _match_multiset(expected, _values(text, variables), variables) else WRONG), ""
        if kind == "eigbasis":
            return _check_eigbasis(part, text), ""
        if kind == "elem_product":
            return _check_elem_product(part, text), ""
        if kind == "row_equiv":
            return _check_row_equiv(part, text), ""
        if kind == "power_identity":
            return _check_power_identity(part, text), ""
        if kind == "pair_not_diff_squares":
            return _check_pair(text), ""
    except ParseError as exc:
        return INVALID, t("Nerozumiem zápisu: {detail}.", detail=exc.text())
    except (EvalError, TypeError, ValueError):
        return INVALID, t("Nerozumiem zápisu.")
    return INVALID, "Neznámy typ úlohy."


class AnswerReport:
    def __init__(self, results):
        self.results = results  # {id: (status, message)}
        self.passed = sum(s == OK for s, _ in results.values())
        self.total = len(results)
        self.verdict = "AC" if self.passed == self.total and self.total else "WA"

    def to_dict(self):
        return {"verdict": self.verdict, "passed": self.passed, "total": self.total,
                "parts": {k: {"status": s, "message": m} for k, (s, m) in self.results.items()}}


def check_task(parts, answers):
    answers = answers if isinstance(answers, dict) else {}
    return AnswerReport({p["id"]: check_part(p, answers.get(p["id"])) for p in parts})

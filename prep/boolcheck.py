"""Boolean expressions and the 4-bit teaching CPU for PPI answers (no eval).

Syntax of a Boolean expression (variables are given per part, e.g. ["a", "b", "c"]):
    negation    a'   !a   ~a   ¬a   (a+b)'   and the combining overline a̅
    product     ab   a*b   a.b   a·b   a&b   a∧b        (juxtaposition is a product)
    sum         a+b   a|b   a∨b
    XOR         a^b   a⊕b
    NAND, NOR   a↑b↑c (one n-input NAND), a↓b (n-input NOR); mixing them with other operators needs brackets
    constants   0  1
Precedence: negation > product/NAND > XOR > sum/NOR.

A tree is a tuple: ("var", name) | ("const", 0|1) | ("not", x) | (op, [children]) with op in
and, or, xor, nand, nor.
"""
import re

from .i18n import t


class BoolParseError(ValueError):
    def __init__(self, message, **args):
        super().__init__(message)
        self.message, self.args_ = message, args

    def text(self, lang=None):
        return t(self.message, lang, **self.args_)


_SYMBOLS = {
    "'": "'", "’": "'", "´": "'", "`": "'", "̅": "'", "̄": "'",
    "!": "!", "~": "!", "¬": "!",
    "*": "*", ".": "*", "·": "*", "⋅": "*", "&": "*", "∧": "*", "×": "*",
    "+": "+", "|": "+", "∨": "+",
    "^": "^", "⊕": "^",
    "↑": "nand", "↓": "nor",
    "(": "(", ")": ")", "[": "(", "]": ")",
}
_WORDS = {"not": "!", "and": "*", "or": "+", "xor": "^", "nand": "nand", "nor": "nor"}
_NAME = re.compile(r"[A-Za-z][0-9]*")


def _resolve(variables):
    """Map typed names to variables; case-insensitive when that is unambiguous."""
    exact = {v: v for v in variables}
    lower = {}
    for v in variables:
        lower.setdefault(v.lower(), []).append(v)
    folded = {k: vs[0] for k, vs in lower.items() if len(vs) == 1}
    return exact, folded


def tokenize(text, variables):
    exact, folded = _resolve(variables)
    tokens, i = [], 0
    while i < len(text):
        ch = text[i]
        if ch.isspace():
            i += 1
            continue
        if ch in "01":
            tokens.append(("const", int(ch)))
            i += 1
            continue
        if ch.isalpha() and ch.isascii():
            m = re.match(r"[A-Za-z][A-Za-z0-9]*", text[i:])
            word = m.group(0)
            if word.lower() in _WORDS and not all(c in exact or c.lower() in folded for c in _NAME.findall(word)):
                tokens.append(("op", _WORDS[word.lower()]))
                i += len(word)
                continue
            for name in _split(word, exact, folded):
                tokens.append(("var", name))
            i += len(word)
            continue
        if ch in _SYMBOLS:
            tokens.append(("op", _SYMBOLS[ch]))
            i += 1
            continue
        raise BoolParseError("neznámy znak „{x}“", x=ch)
    return tokens


def _split(word, exact, folded):
    """'ab' -> a, b; 'x1x2' -> x1, x2; 'Q1' stays when known."""
    out, j = [], 0
    while j < len(word):
        for size in range(len(word) - j, 0, -1):
            piece = word[j:j + size]
            name = exact.get(piece) or folded.get(piece.lower())
            if name:
                out.append(name)
                j += size
                break
        else:
            m = _NAME.match(word, j)
            raise BoolParseError("neznáma premenná „{x}“", x=m.group(0) if m else word[j:])
    return out


class _Parser:
    def __init__(self, tokens):
        self.tokens, self.pos = tokens, 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else (None, None)

    def take(self):
        tok = self.peek()
        self.pos += 1
        return tok

    def parse(self):
        if not self.tokens:
            raise BoolParseError("prázdny výraz")
        node = self.sum()
        if self.pos != len(self.tokens):
            raise BoolParseError("nadbytočný znak „{x}“", x=_show(self.peek()))
        return node

    def _chain(self, sub, joiners, plain, special):
        """Operands joined by one operator kind; the special one (NAND/NOR) may not mix with the plain one."""
        items, ops = [sub()], set()
        while True:
            kind, val = self.peek()
            if kind == "op" and val in joiners:
                self.take()
                ops.add(val)
                items.append(sub())
            elif plain == "and" and self._starts_operand():
                ops.add("*")
                items.append(sub())
            else:
                break
        if len(items) == 1:
            return items[0]
        if special in ops and len(ops) > 1:
            raise BoolParseError("pri kombinácii {op} s inými operátormi použite zátvorky", op="↑" if special == "nand" else "↓")
        return ((special if special in ops else plain), items)

    def _starts_operand(self):
        kind, val = self.peek()
        return kind in ("var", "const") or (kind == "op" and val in ("(", "!"))

    def sum(self):
        return self._chain(self.xor, ("+", "nor"), "or", "nor")

    def xor(self):
        items = [self.product()]
        while self.peek() == ("op", "^"):
            self.take()
            items.append(self.product())
        return items[0] if len(items) == 1 else ("xor", items)

    def product(self):
        return self._chain(self.unary, ("*", "nand"), "and", "nand")

    def unary(self):
        if self.peek() == ("op", "!"):
            self.take()
            return ("not", self.unary())
        node = self.primary()
        while self.peek() == ("op", "'"):
            self.take()
            node = ("not", node)
        return node

    def primary(self):
        kind, val = self.take()
        if kind == "var":
            return ("var", val)
        if kind == "const":
            return ("const", val)
        if (kind, val) == ("op", "("):
            node = self.sum()
            if self.take() != ("op", ")"):
                raise BoolParseError("chýba zatváracia zátvorka")
            return node
        if kind is None:
            raise BoolParseError("výraz je neúplný")
        raise BoolParseError("nečakaný znak „{x}“", x=_show((kind, val)))


def _show(tok):
    kind, val = tok
    return {"nand": "↑", "nor": "↓"}.get(val, str(val)) if kind else ""


def parse(text, variables):
    return _Parser(tokenize(text, variables)).parse()


def evaluate(node, env):
    kind = node[0]
    if kind == "var":
        return env[node[1]]
    if kind == "const":
        return node[1]
    if kind == "not":
        return 1 - evaluate(node[1], env)
    vals = [evaluate(c, env) for c in node[1]]
    if kind == "and":
        return int(all(vals))
    if kind == "or":
        return int(any(vals))
    if kind == "xor":
        return sum(vals) % 2
    if kind == "nand":
        return 1 - int(all(vals))
    if kind == "nor":
        return 1 - int(any(vals))
    raise ValueError(kind)


def point(variables, index):
    """Values of the variables at row `index` of the truth table (first variable = highest weight)."""
    n = len(variables)
    return {v: (index >> (n - 1 - k)) & 1 for k, v in enumerate(variables)}


def vector(node, variables):
    return "".join(str(evaluate(node, point(variables, i))) for i in range(2 ** len(variables)))


def matches(vec, expected):
    """expected may contain 'x' (don't care)."""
    return len(vec) == len(expected) and all(e in "xX-" or e == g for e, g in zip(expected, vec))


# --- shape of an expression ------------------------------------------------------------

def is_literal(node):
    return node[0] == "var" or (node[0] == "not" and node[1][0] == "var")


def _flat(node, op):
    return node[1] if node[0] == op else [node]


def terms(node, outer):
    """Terms of a two-level form: outer 'or' (DNF) or 'and' (KNF); None if the shape does not fit."""
    inner = "and" if outer == "or" else "or"
    out = []
    for term in _flat(node, outer):
        lits = _flat(term, inner)
        if not all(is_literal(x) for x in lits):
            return None
        out.append(lits)
    return out


def literal_count(node):
    if node[0] == "var":
        return 1
    if node[0] == "const":
        return 0
    if node[0] == "not":
        return literal_count(node[1])
    return sum(literal_count(c) for c in node[1])


def only_gate(node, gate):
    """Every operator is the gate, inputs are literals (a negated input counts as available)."""
    if is_literal(node):
        return True
    return node[0] == gate and all(only_gate(c, gate) for c in node[1])


def _lit(x):
    return (x[1], 1) if x[0] == "var" else (x[1][1], 0)


def hazard_free(node, variables, expected):
    """DNF: every two neighbouring 1-points are covered by one common product."""
    prods = [dict(_lit(x) for x in lits) for lits in terms(node, "or")]
    ones = [i for i, e in enumerate(expected) if e == "1"]
    n = len(variables)
    for i in ones:
        for k in range(n):
            j = i ^ (1 << (n - 1 - k))
            if j > i and expected[j] == "1":
                pi, pj = point(variables, i), point(variables, j)
                if not any(all(pi[v] == b and pj[v] == b for v, b in p.items()) for p in prods):
                    return False
    return True


# --- the 4-bit CPU from the lecture ------------------------------------------------------

OPCODES = {"LDA": 0, "ADD": 1, "STA": 2, "JMP": 3}


def parse_program(text):
    """One instruction per line: 'LDA 2', 'ADD 1' or binary '0110'. At most 4 words."""
    words = []
    for line in re.split(r"[\n;]+", text):
        line = line.strip()
        if not line:
            continue
        m = re.fullmatch(r"([01]{2})\s*([01]{2})", line)
        if m:
            words.append((int(m.group(1), 2), int(m.group(2), 2)))
            continue
        m = re.fullmatch(r"([A-Za-z]{3})\s*(\d+)", line)
        if not m or m.group(1).upper() not in OPCODES:
            raise BoolParseError("neznáma inštrukcia „{x}“", x=line[:20])
        adr = int(m.group(2))
        if adr > 3:
            raise BoolParseError("adresa musí byť 0 až 3: „{x}“", x=line[:20])
        words.append((OPCODES[m.group(1).upper()], adr))
    if not words:
        raise BoolParseError("prázdny program")
    if len(words) > 4:
        raise BoolParseError("pamäť programu má len 4 slová")
    return words


def run_program(words, memory, steps=40):
    """Run instruction by instruction; returns the data memory after `steps` instructions."""
    mem, acc, pc = list(memory), 0, 0
    program = words + [(3, len(words))] * (4 - len(words)) if len(words) < 4 else list(words)
    # an empty program slot behaves as a jump to itself: the program stops there
    for _ in range(steps):
        oc, adr = program[pc]
        pc = (pc + 1) % 4
        if oc == 0:
            acc = mem[adr]
        elif oc == 1:
            acc = (acc + mem[adr]) % 16
        elif oc == 2:
            mem[adr] = acc
        else:
            pc = adr
    return mem

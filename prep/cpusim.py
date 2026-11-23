"""A faithful model of the basic CPUSim simulator (cpusim.ail-lab.fiit.stuba.sk, von Neumann mode).

Word: operand[31:8] | mode[7:6] | opcode[5:0]; modes 0 = #immediate, 1 = direct, 2 = indirect ([n] or @n).
Memory 2048 words, program 0-1023, data 1024-2047; an empty cell reads as 0 (fetching it is an error).
Jumps take the target from the operand like LOAD does: `JMP #loop` jumps to loop, `JMP loop` jumps to
the address stored in the cell `loop`. CPUSim has no step limit (fast simulation runs a set number of
micro-instructions per press); BUDGET here only stops endless loops.

The assembler follows the code editor: one line = one cell, a line with only a comment takes no cell,
an empty line is an empty cell, `label:` before an instruction, comments after `;`.
"""
import re

from .i18n import t

SIZE, INSTR_SIZE = 2048, 1024
BUDGET = 1_000_000
MASK24 = 0xFFFFFF
IMM_MIN, IMM_MAX = -8388608, (1 << 24) - 1
C, V, N, Z = 8, 4, 2, 1

# name: (opcode, takes operand, allowed modes)
ISA = {
    "NOP": (0, False, ()), "ADD": (1, True, (0, 1, 2)), "SUB": (2, True, (0, 1, 2)),
    "MUL": (3, True, (0, 1, 2)), "DIV": (4, True, (0, 1, 2)), "NOT": (5, False, ()),
    "AND": (6, True, (0, 1, 2)), "OR": (7, True, (0, 1, 2)), "XOR": (8, True, (0, 1, 2)),
    "CMP": (9, True, (0, 1, 2)), "JZ": (10, True, (0, 1, 2)), "JNZ": (11, True, (0, 1, 2)),
    "JMP": (12, True, (0, 1, 2)), "ROL": (13, False, ()), "ROR": (14, False, ()),
    "INC": (15, False, ()), "DEC": (16, False, ()), "STORE": (17, True, (1, 2)),
    "LOAD": (18, True, (0, 1, 2)), "HALT": (19, False, ()), "JC": (20, True, (0, 1, 2)),
    "JNC": (21, True, (0, 1, 2)), "RLV": (22, False, ()), "RRV": (23, False, ()), "CLSR": (24, False, ()),
}
BY_CODE = {code: (name, op, modes) for name, (code, op, modes) in ISA.items()}
JUMPS = {"JZ", "JNZ", "JMP", "JC", "JNC"}

_LABEL = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*")
_NUMBER = re.compile(r"^[-+]?(0x[0-9a-f]+|0b[01]+|\d+)$", re.I)


class AsmError(ValueError):
    def __init__(self, message, **args):
        super().__init__(message)
        self.message, self.args_ = message, args

    def text(self, lang=None):
        return t(self.message, lang, **self.args_)


def i32(x):
    x &= 0xFFFFFFFF
    return x - (1 << 32) if x & 0x80000000 else x


def number(text):
    text = text.strip()
    if not _NUMBER.match(text):
        return None
    neg = text.startswith("-")
    body = text.lstrip("+-").lower()
    value = int(body[2:], 16) if body.startswith("0x") else int(body[2:], 2) if body.startswith("0b") else int(body)
    return -value if neg else value


def encode(opcode, mode, operand):
    return i32((operand & MASK24) << 8 | (mode & 3) << 6 | opcode & 63)


def _lines(text):
    rows = text.replace("\r", "").split("\n")
    if rows and rows[-1] == "":
        rows.pop()
    out = []
    for row in rows:
        if row.strip().startswith(";"):
            out.append(None)                     # comment line: no cell
            continue
        code = row.split(";", 1)[0].strip()
        label = None
        m = _LABEL.match(code)
        if m:
            label, code = m.group(1), code[m.end():].strip()
        out.append((code, label))
    return out


def assemble(program, data="", data_start=INSTR_SIZE):
    """Return {address: word}. Raises AsmError (Slovak message with the line number)."""
    prog, dat = _lines(program), _lines(data)
    labels = {}

    def place(rows, start, limit):
        addr, where = start, []
        for i, row in enumerate(rows):
            if row is None:
                where.append(None)
                continue
            if addr >= limit and row[0]:
                raise AsmError("riadok {line}: program sa nezmestí do pamäte", line=i + 1)
            where.append(addr)
            if row[1]:
                key = row[1].upper()
                if key in labels or key in ISA:
                    raise AsmError("riadok {line}: návestie {label} je definované viackrát", line=i + 1, label=row[1])
                labels[key] = addr
            addr += 1
        return where

    pwhere = place(prog, 0, INSTR_SIZE)
    dwhere = place(dat, data_start, SIZE)

    def value(text):
        v = number(text)
        if v is None:
            v = labels.get(text.strip().upper())
        return v

    memory = {}
    for i, (row, addr) in enumerate(zip(prog, pwhere)):
        if row is None or not row[0] or addr >= INSTR_SIZE:
            continue
        name, *rest = row[0].split()
        spec = ISA.get(name.upper())
        if spec is None:
            raise AsmError("riadok {line}: neznáma inštrukcia {name}", line=i + 1, name=name)
        code, has_operand, modes = spec
        operand = "".join(rest).strip()
        if not has_operand:
            if operand:
                raise AsmError("riadok {line}: inštrukcia {name} nemá operand", line=i + 1, name=name.upper())
            memory[addr] = encode(code, 0, 0)
            continue
        if not operand:
            raise AsmError("riadok {line}: inštrukcii {name} chýba operand", line=i + 1, name=name.upper())
        if operand.startswith("#"):
            mode, operand = 0, operand[1:]
        elif operand.startswith("@"):
            mode, operand = 2, operand[1:]
        elif operand.startswith("[") and operand.endswith("]"):
            mode, operand = 2, operand[1:-1]
        else:
            mode = 1
        if mode not in modes:
            raise AsmError("riadok {line}: inštrukcia {name} nepovoľuje tento spôsob adresovania",
                           line=i + 1, name=name.upper())
        v = value(operand)
        if v is None:
            raise AsmError("riadok {line}: neznámy operand {x}", line=i + 1, x=operand)
        if mode == 0 and not IMM_MIN <= v <= IMM_MAX:
            raise AsmError("riadok {line}: okamžitý operand je mimo rozsahu", line=i + 1)
        if mode != 0 and not 0 <= v < SIZE:
            raise AsmError("riadok {line}: adresa musí byť od 0 do {max}", line=i + 1, max=SIZE - 1)
        memory[addr] = encode(code, mode, v)
    for i, (row, addr) in enumerate(zip(dat, dwhere)):
        if row is None or not row[0] or addr >= SIZE:
            continue
        v = value(row[0])
        if v is None:
            raise AsmError("údaje, riadok {line}: neplatná hodnota {x}", line=i + 1, x=row[0])
        if not -2147483648 <= v <= 4294967295:
            raise AsmError("údaje, riadok {line}: hodnota je mimo rozsahu", line=i + 1)
        memory[addr] = i32(v)
    return memory


class Result:
    def __init__(self, memory, status, error=None, steps=0, instructions=0):
        self.memory, self.status, self.error = memory, status, error
        self.steps, self.instructions = steps, instructions

    def get(self, addr):
        v = self.memory[addr]
        return 0 if v is None else v


def run(memory, budget=BUDGET):
    """memory: {addr: word}. Runs from PC = 0. status: halted | error | budget."""
    mem = [None] * SIZE
    for a, v in memory.items():
        mem[int(a)] = i32(v)
    acc = pc = sr = 0
    steps = instructions = 0

    def read(addr):
        if not 0 <= addr < SIZE:
            raise AsmError("adresa {addr} je mimo pamäte", addr=addr)
        v = mem[addr]
        return 0 if v is None else v

    def flags_zn(value, keep):
        s = keep & ~(Z | N)
        if value == 0:
            s |= Z
        if value < 0:
            s |= N
        return s

    try:
        while True:
            if steps + 5 > budget:
                return Result(mem, "budget", steps=steps, instructions=instructions)
            if not 0 <= pc < INSTR_SIZE:
                raise AsmError("PC = {addr} je mimo programovej oblasti", addr=pc)
            word = mem[pc]
            if word is None:
                raise AsmError("procesor narazil na prázdnu bunku {addr} (chýba HALT?)", addr=pc)
            pc = (pc + 1) & 0xFFFFFFFF
            steps += 5
            opcode, mode = word & 63, (word >> 6) & 3
            spec = BY_CODE.get(opcode)
            if spec is None:
                raise AsmError("neznámy operačný kód {code}", code=opcode)
            name, has_operand, modes = spec
            if has_operand and mode not in modes:
                raise AsmError("inštrukcia {name} nepovoľuje tento spôsob adresovania", name=name)
            instructions += 1
            raw = word >> 8                                  # signed 24-bit operand (IR >> 8)
            if name in JUMPS:
                if name != "JMP":
                    steps += 1
                    if name == "JZ":
                        cond = acc == 0
                    elif name == "JNZ":
                        cond = acc != 0
                    elif name == "JC":
                        cond = sr & C
                    else:
                        cond = not sr & C
                    if not cond:
                        continue
                target = raw
                steps += 2
                if mode >= 1:
                    target = read(raw & MASK24)
                    steps += 2
                if mode == 2:
                    target = read(target & MASK24)
                    steps += 2
                pc = target & MASK24
                continue
            if name == "STORE":
                addr = raw & MASK24
                steps += 4
                if mode == 2:
                    addr = read(addr) & MASK24
                    steps += 2
                if not 0 <= addr < SIZE:
                    raise AsmError("adresa {addr} je mimo pamäte", addr=addr)
                mem[addr] = acc
                continue
            if has_operand:
                mbr = raw
                steps += 1
                if mode >= 1:
                    mbr = read(raw & MASK24)
                    steps += 2
                if mode == 2:
                    mbr = read(mbr & MASK24)
                    steps += 2
                steps += 1
                if name == "LOAD":
                    acc = mbr
                elif name == "CMP":
                    sr = sr | C if acc == mbr else sr & ~C
                else:
                    if name == "DIV":
                        if mbr == 0:
                            raise AsmError("delenie nulou")
                        exact = abs(acc) // abs(mbr) * (1 if (acc < 0) == (mbr < 0) else -1)
                    elif name == "ADD":
                        exact = acc + mbr
                    elif name == "SUB":
                        exact = acc - mbr
                    elif name == "MUL":
                        exact = acc * mbr
                    elif name == "AND":
                        exact = acc & mbr
                    elif name == "OR":
                        exact = acc | mbr
                    else:
                        exact = acc ^ mbr
                    acc = i32(exact)
                    sr = flags_zn(acc, sr)
                    sr = sr | V if exact != acc else sr & ~V
                continue
            steps += 1
            if name == "HALT":
                return Result(mem, "halted", steps=steps, instructions=instructions)
            if name in ("INC", "DEC"):
                exact = acc + (1 if name == "INC" else -1)
                acc = i32(exact)
                sr = flags_zn(acc, sr)
                sr = sr | V if exact != acc else sr & ~V
            elif name == "NOT":
                acc = i32(~acc)
                sr = flags_zn(acc, sr)
            elif name == "ROL":
                acc = i32(acc << 1)
                sr = flags_zn(acc, sr)
            elif name == "ROR":
                acc = i32((acc & 0xFFFFFFFF) >> 1)
                sr = flags_zn(acc, sr)
            elif name == "RLV":
                carry = 1 if sr & V else 0
                sr = sr | V if acc & 0x80000000 else sr & ~V
                acc = i32(acc << 1 | carry)
                sr = flags_zn(acc, sr)
            elif name == "RRV":
                carry = 1 if sr & V else 0
                sr = sr | V if acc & 1 else sr & ~V
                acc = i32((acc & 0xFFFFFFFF) >> 1 | carry << 31)
                sr = flags_zn(acc, sr)
            elif name == "CLSR":
                sr = 0
    except AsmError as exc:
        return Result(mem, "error", error=exc, steps=steps, instructions=instructions)


def strip_export(text):
    """Accept the code editor text or the whole 'Riešenie na odovzdanie' export: keep the PROGRAM part."""
    m = re.search(r"^\s*PROGRAM\s*$(.*?)^\s*(DATA|END)\s*$", text, re.M | re.S | re.I)
    return m.group(1).strip("\n") if m else text

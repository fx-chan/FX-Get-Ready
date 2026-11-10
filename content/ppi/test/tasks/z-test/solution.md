### Príklad 1

Jednotky v mape tvoria konfigurácie $\overline{a}d$ (body 1, 3, 5, 7), $ab$ (12–15) a $a\overline{d}$ (8, 10, 12, 14).
MDNF: $f = \overline{a}d + ab + a\overline{d}$ (6 písmen). Nuly (0, 2, 4, 6, 9, 11) pokryjú $\overline{a}\,\overline{d}$ a $a\overline{b}d$:
MKNF: $f = (a + d)(\overline{a} + b + \overline{d})$. NAND/NAND vznikne z MDNF nahradením AND aj OR členom NAND:
$(\overline{a} \uparrow d) \uparrow (a \uparrow b) \uparrow (a \uparrow \overline{d})$.

### Príklad 2

Automat rozpoznáva postupnosť $100$ (s prekrývaním: jednotka môže začať novú). Pre $x = 1001000100$ je výstup $0010010001$.
Prechodová tabuľka v kódoch: $00 \to 00 / 01$, $01 \to 10 / 01$, $10 \to 00 / 01$. $Q_1^+ = 1$ len zo stavu $01$ pri $x = 0$,
s využitím nepoužitého kódu: $D_1 = Q_0\overline{x}$. Výstup je 1 len zo stavu $10$ pri $x = 0$: $y = Q_1\overline{x}$.

### Príklad 3

$0101 + 0110 = 1011$, prenos z najvyššieho bitu nevznikol: $C = 0$, $Z = 0$, $N = 1$; dve kladné čísla dali záporný
výsledok, preto $V = 1$ (príznaky $0011$). Ako číslo so znamienkom je $1011$ hodnota $-5$ — skutočný súčet 11 sa do
rozsahu $-8 \dots 7$ nezmestí.

### Príklad 4

Napríklad `LDA 0`, `ADD 0`, `ADD 1`, `STA 2`. Takty: LDA 6, ADD 6, ADD 6, STA 5, spolu 23. Mikroprogramové riadenie
je typické pre CISC.

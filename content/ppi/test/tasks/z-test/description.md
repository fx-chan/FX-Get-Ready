Test má 4 príklady, spolu 12 odpovedí. Čas 60 minút. Negácia `a'`, súčin `ab`, súčet `a+b`, KNF `(a+b)(c+d')`, NAND `↑`, NOR `↓`.

### Príklad 1 — kombinačný obvod

$f(a, b, c, d) = \sum(1, 3, 5, 7, 8, 10, 12, 13, 14, 15)$.

### Príklad 2 — automat

Mealyho automat so vstupom $x$ zo stavu $A$:

| stav | $x = 0$ | $x = 1$ |
|---|---|---|
| $A$ | $A$ / 0 | $B$ / 0 |
| $B$ | $C$ / 0 | $B$ / 0 |
| $C$ | $A$ / 1 | $B$ / 0 |

Kódovanie $A = 00$, $B = 01$, $C = 10$ ($Q_1Q_0$), kód 11 sa nepoužíva. Premenné `Q1, Q0, x`.

### Príklad 3 — aritmetika

4-bitová sčítačka, čísla v dvojkovom doplnku. Príznaky ako štyri bity **C Z N V**.

### Príklad 4 — procesor

Procesor s inštrukciami LDA, ADD, STA, JMP (2 bity OC + 2 bity adresy) a s registrami MAR, MBR.

Automat Moore zo stavu $s_1$; výstup závisí len od stavu:

| stav | $x = 0$ | $x = 1$ | výstup $y$ |
|---|---|---|---|
| $s_1$ | $s_1$ | $s_2$ | 0 |
| $s_2$ | $s_3$ | $s_2$ | 0 |
| $s_3$ | $s_1$ | $s_4$ | 0 |
| $s_4$ | $s_3$ | $s_2$ | 1 |

Vstup $x = 1101010$. Výstup zapisujte pre stav, do ktorého sa automat dostal po každom takte. Bity píšte za sebou, napr. `0110`.

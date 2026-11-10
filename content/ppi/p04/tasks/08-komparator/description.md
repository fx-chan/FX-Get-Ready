Porovnávame dvojbitové čísla $A = a_1a_0$ a $B = b_1b_0$ (premenné v tomto poradí: `a1, a0, b1, b0`;
súčin píšte napr. `a1 b1'` alebo `a1*b1'`). Negácia `a'`, súčin `ab`, súčet `a+b`, NAND `a↑b`, NOR `a↓b`; viacvstupový člen `a↑b↑c`.

Výstup $A > B$ v mape (riadky $a_1a_0$, stĺpce $b_1b_0$):

| a1a0 \\ b1b0 | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 0 | 0 | 0 | 0 |
| **01** | 1 | 0 | 0 | 0 |
| **11** | 1 | 1 | 0 | 1 |
| **10** | 1 | 1 | 0 | 0 |

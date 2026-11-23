Zadanie zrekonštruované z pamäti študentov; nejasné miesta sú tu dourčené tak, aby sedeli oba príklady.

**Vstupy.** Pole má $R$ riadkov (1025) a $C$ stĺpcov (1026), $2 \le R \le 8$, $2 \le C \le 10$; nové bloky
sa objavujú v stĺpci $S$ (1027). Pole je matica 0/1 po riadkoch s adresou políčka
$1100 + (r-1) \cdot C + c$ — začína teda na **1101**. Inštrukcie od 1200 ukončené $-1$:
0 = bez posunu, 1 = vľavo, 2 = vpravo. Pracovné bunky od 1800.

**Pravidlá.** Blok má veľkosť jedného políčka.

1. Nový blok sa objaví na $(1, S)$. Ak je obsadené, hra končí prehrou (1043 = 1).
2. Pred každou inštrukciou sa zistí, či blok stojí — je v poslednom riadku alebo je pod ním obsadené
   políčko. Ak áno, **usadí sa**: políčko dostane 1, počet blokov +1, inštrukcia sa nečíta.
3. Ak je po usadení jeho riadok plný, celý riadok sa vynuluje a skóre +1 (bloky nad ním nepadajú,
   kontroluje sa len tento riadok). Potom krok 1.
4. Ak blok nestojí, prečíta sa inštrukcia ($-1$ → koniec, 1043 = 0). Počet cyklov +1. Pri 1/2 sa blok
   posunie do strany, ak tam nie je okraj ani obsadené políčko. Potom klesne o riadok, ak je pod ním voľno.
   Pokračuje sa krokom 2.

| adresa | výstup |
|---|---|
| 1040 | skóre (vymazané riadky) |
| 1041 | usadené bloky |
| 1042 | cykly (prečítané inštrukcie 0/1/2) |
| 1043 | koniec: 1 = prehra, 0 = značka $-1$ |
| 1044, 1045 | riadok a stĺpec aktívneho bloku |

**Príklad 1.** $R = C = 3$, $S = 2$, prázdne pole, `1, 0, 2, 0, 0, 0, 2, 1, 0, -1` →
`1, 6, 9, 1, 1, 2`, v poli ostane plný stĺpec 2.

**Príklad 2.** $R = C = 4$, $S = 2$, inštrukcie `2, 0, 0, 1, 1, 0, 0, 2, 2, 0, 0, -1`:

```
 1: 0 0 0 0
 2: 0 0 0 1
 3: 1 0 0 0
 4: 1 1 0 1
```

Výstupy `1, 5, 11, 0, 2, 2`, pole po skončení:

```
 1: 1 0 0 0
 2: 1 0 0 1
 3: 1 0 1 0
 4: 0 0 1 0
```

<details class="cpusim-data"><summary>Údaje príkladu 2 pre CPUSim (adresy 1024–1211, jeden riadok = jedna bunka)</summary>

```
0
4
4
2
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
1
1
0
0
0
1
1
0
1
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
2
0
0
1
1
0
0
2
2
0
0
-1
```

</details>

**a)** Ručne: $R = C = 2$, $S = 1$, pole `0 0 / 0 1`, inštrukcie `0, 2, 0, -1`.

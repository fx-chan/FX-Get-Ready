Vytvorte štruktúru pre osobu: meno a priezvisko (max. 100 znakov), ulica (max. 100 znakov), PSČ
a telefónne číslo (reťazce). V statickom poli pre **10 osôb** uložte `n` osôb (`n ≤ 10`) a vypíšte ich.

Vstup: `n`, potom pre každú osobu **4 riadky**: meno a priezvisko, ulica, PSČ, telefón
(meno aj ulica môžu obsahovať medzery — čítajte celé riadky cez `fgets`).

### Ukážka vstupu
```
2
Jan Novak
Hlavna 12
81101
0901123456
Eva Mala
Dlha 3
04001
0944000111
```
### Výstup
```
1. Jan Novak, Hlavna 12, 81101, tel. 0901123456
2. Eva Mala, Dlha 3, 04001, tel. 0944000111
```

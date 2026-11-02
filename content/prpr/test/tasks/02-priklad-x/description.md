Funkcia `x` načíta zo štandardného vstupu celé číslo `k`. **Ošetrite načítanie** tak, aby `k` bolo
kladné a nenulové — kým nie je, čítajte ďalej (preskočte aj nečíselné slová).

Potom z poľa `hodnota` (vstupuje ako parameter) určte histogram zastúpenia cifier na **2., 3. a 4.
desatinnom mieste**, a to iba pre hodnoty na pozíciách deliteľných `k` (teda `0, k, 2k, 3k, …`).
Hodnoty sú nezáporné a majú najviac 6 desatinných miest.

Vypíšte len cifry s nenulovým počtom, vzostupne — každé číslo na šírku 3 (`%3d`):
```
cislice:    2  4  5
pocetnost:  4  4  4
```
(riadok začína `cislice:  ` resp. `pocetnost:` — oba popisy majú 10 znakov.)

### Vstup programu
`main` (už hotový) načíta `n` a `n` hodnôt; potom volá `x`, ktorá načíta `k`.

### Ukážka vstupu
```
7
5.254254
5.254254
5.254254
5.254201
5.254203
5.254205
5.254207
2
```
### Výstup
```
cislice:    2  4  5
pocetnost:  4  4  4
```

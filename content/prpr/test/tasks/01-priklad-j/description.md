Funkcia `j` načíta z klávesnice **mer. modul 1** a **mer. modul 2** (veľké písmeno + dve číslice,
napr. `A12`) a **typ mer. veličiny** (dve veľké písmená, napr. `RM`). Pre každý modul zvlášť zistite
**minimálnu, maximálnu a strednú hodnotu** meraní daného typu (hodnoty jedného modulu vložte do
dynamického poľa a strednú hodnotu počítajte **vlastnou funkciou**).

Percentuálny rozdiel A voči B: `PR(A, B) = B * 100 / A - 100`. Vypočítajte:

- `PRi = PR(min, stred)` — minimum voči strednej hodnote modulu,
- `PRm = PR(max, stred)` — maximum voči strednej hodnote modulu,
- `PRs1 = PR(stred1, stred2)`, `PRs2 = PR(stred2, stred1)` — stredné hodnoty modulov navzájom.

Výstup (všetky čísla na **4 desatinné miesta**):
```
modul1 min (PRi) stred max (PRm)
modul2 min (PRi) stred max (PRm)
```
a potom, ak sú **všetky** rozdiely `PRs1, PRs2, PRi, PRm` oboch modulov v rozmedzí ±5 %:
`modul1 a modul2 su v standardnej odchylke.`, inak `modul1 a modul2 prekracuju limit povoleneho rozmedzia.`

Ak niektorý modul neobsahuje daný typ veličiny, vypíše sa **iba** `modul1 a modul2 sa nemozu porovnat.`

### Vstup programu
`main` (už hotový) načíta `n` a `n` riadkov `modul typ hodnota`; potom volá `j`, ktorá načíta posledný
riadok `modul1 modul2 typ`.

### Ukážka vstupu
```
6
A12 RM 5.20
A12 RM 5.30
A12 RD 9.99
B34 RM 5.10
B34 RM 5.40
B34 RM 5.25
A12 B34 RM
```
### Výstup
```
A12 5.2000 (0.9615) 5.2500 5.3000 (-0.9434)
B34 5.1000 (2.9412) 5.2500 5.4000 (-2.7778)
A12 a B34 su v standardnej odchylke.
```

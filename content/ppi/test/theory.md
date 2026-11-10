> Zhrnutie celého predmetu na jednom mieste a skúška nanečisto. Na konci je test na 60 minút: zadanie uvidíte až po spustení, vyhodnotí sa po odovzdaní.

## Ťahák: Booleova algebra a zápisy funkcií

- De Morgan: $\overline{a + b} = \overline{a}\,\overline{b}$, $\overline{ab} = \overline{a} + \overline{b}$.
- Absorpcia $a + ab = a$, absorpcia negácie $a + \overline{a}b = a + b$, spojovanie $ab + a\overline{b} = a$, konsenzus $ab + \overline{a}c + bc = ab + \overline{a}c$.
- Funkcií $n$ premenných je $2^{2^n}$, bodov $2^n$; bod číslujeme dvojkovo, prvá premenná má najvyššiu váhu.
- Mapa: Grayov kód 00, 01, 11, 10; každé políčko má $n$ susedov, aj cez okraj.

::: quiz
Koľko susedov má políčko v mape 4 premenných?
- [ ] 2
- [ ] 3
- [x] 4
> Toľko, koľko je premenných: každú môžeme zmeniť.
:::

## Ťahák: minimalizácia a obvody

- Konfigurácia $2^s$ políčok v mape $n$ premenných = súčin rádu $r = n - s$.
- MDNF: pokryť **jednotky** čo najväčšími a čo najmenej konfiguráciami; MKNF: to isté s **nulami**, zápis súčtami (0 → premenná, 1 → negácia).
- x (neurčené) používame, len keď konfiguráciu zväčšia.
- NAND/NAND z MDNF, NOR/NOR z MKNF; jednopísmenový člen ide do druhého stupňa negovaný.
- Statický hazard: susedné jednotky bez spoločného súčinu; BDNF ich pokryje (pridáme konsenzus).
- MUX: $2^m = n$ adresových a dátových vstupov; DEMUX = MUX bez OR; dekodér „1 z n“.

::: drill t-mdnf

::: quiz
$f = a\overline{b} + bc$. Ktorý člen treba pridať do BDNF?
- [ ] $\overline{a}c$
- [x] $ac$
- [ ] $ab$
> Konsenzus podľa premennej $b$: $a \cdot c$.
:::

## Ťahák: automaty a preklápacie obvody

- Mealy $v: S \times X \to Y$, Moore $v: S \to Y$ (oneskoruje výstup o takt).
- $Q^+$: D: $D$; T: $T \oplus Q$; JK: $J\overline{Q} + \overline{K}Q$; SR: $S + \overline{R}Q$, $SR = 0$.
- Inverzná funkcia (0→0, 0→1, 1→0, 1→1): D: 0, 1, 0, 1; T: 0, 1, 1, 0; JK: 0x, 1x, x1, x0; SR: 0x, 10, 01, x0.
- Počet PO $\lceil \log_2 |S| \rceil$; pri PO-D je $D_i = Q_i^+$; nepoužité kódy = x.
- Kódovanie: pravidlo 1 (rovnaký nasledujúci stav → susedné kódy), pravidlo 2 (nasledovníci toho istého stavu → susedné).
- Perióda hodín $T \ge t_{PO} + t_K + t_s$.
- Asynchrónne: stabilný stav $p(s, x) = s$, rád $r = k_{max} + 1$, kritický súbeh odstráni priamy alebo nepriamy kód.

::: quiz
PO-JK v stave 0 dostane $J = 1, K = 1$. Nový stav je
- [ ] 0
- [x] 1
> Komplement: $0 \to 1$.
:::

::: quiz
Automat má 9 stavov. Najmenší počet PO je
- [ ] 3
- [x] 4
- [ ] 9
> $2^3 = 8 < 9 \le 16$.
:::

## Ťahák: procesor

- Polovičná sčítačka $S = A \oplus B$, $C = AB$; úplná $S = A \oplus B \oplus C_{in}$, $C_{out}$ = majorita.
- $A - B = A + \overline{B} + 1$; príznaky C (prenos), Z (nula), N (najvyšší bit), V (zlé znamienko pri rovnakých znamienkach sčítancov).
- 4-bitová inštrukcia OC + ADR: 00 LDA, 01 ADD, 10 STA, 11 JMP; výber – dekódovanie – vykonanie.
- Takty s MAR/MBR: výber 3, LDA a ADD spolu 6, STA 5, JMP 4.
- Pevná logika: rýchla, RISC; mikroprogram: pružný, CISC.

::: drill t-procesor

::: quiz
$0111 + 0001$ na 4 bitoch nastaví príznaky
- [ ] C = 1, V = 0
- [x] N = 1, V = 1
- [ ] Z = 1
> Výsledok $1000$: najvyšší bit 1 (N), dve kladné čísla dali „záporné“ (V). Prenos z najvyššieho bitu nevznikol.
:::

> Podľa 1. a 2. prednášky PPI: logické obvody, Booleovské funkcie a spôsoby ich zápisu.

## Logický obvod

**Logický obvod** je elektronický obvod, ktorý pracuje s dvojhodnotovými premennými: **0** (nie, nepravda, L — low) a **1** (áno, pravda, H — high). Má vstupné premenné $x_1, \dots, x_n$ a výstupné $y_1, \dots, y_m$. Vstupné slovo $X = (x_1, \dots, x_n)$ môže nadobudnúť $2^n$ hodnôt, výstupné $Y$ až $2^m$ hodnôt. Správanie opisuje zobrazenie $F: X \to Y$.

Z pohľadu teórie je logický obvod diskrétny dynamický systém, ktorý je daný vstupným a výstupným slovom, **správaním** (čo robí v čase) a **štruktúrou** (z akých logických členov je zložený a ako sú prepojené).

Pri práci s obvodmi sa riešia tieto úlohy:

- **analýza** — poznám štruktúru, hľadám správanie;
- **syntéza** — poznám požadované správanie, navrhujem štruktúru;
- **diagnostika** — testovanie, či obvod funguje (a návrh obvodu tak, aby sa dal dobre testovať);
- **simulácia (verifikácia)** — overenie návrhu ešte pred výrobou.

### Napätie a logická hodnota

Fyzicky je premenná napätie. Hodnote **H** zodpovedá interval $U \ge U_{max}$, hodnote **L** interval $U \le U_{min}$; medzi nimi je zakázané pásmo. Ako priradiť H a L k 0 a 1?

| | 0 | 1 |
|---|---|---|
| **kladná logika** | L | H |
| **záporná logika** | H | L |

Ten istý fyzický obvod teda môže v kladnej logike robiť AND a v zápornej OR (De Morgan). Ak nie je povedané inak, predpokladáme kladnú logiku.

::: quiz
Obvod dá na výstupe H iba vtedy, keď sú oba vstupy H. V **zápornej** logike realizuje
- [ ] AND
- [x] OR
- [ ] NAND
> V zápornej logike H = 0. Výstup je 0 len pri oboch vstupoch 0, inak 1 — to je OR.
:::

### Rozdelenie logických obvodov

- podľa funkcie: **kombinačné** (výstup závisí len od aktuálneho vstupu) a **sekvenčné** (závisí aj od histórie — majú pamäť);
- podľa činnosti v čase: **asynchrónne** a **synchrónne** (riadené hodinovým signálom);
- podľa realizácie: s **pevnou** funkciou a s **programovateľnou** funkciou.

## Booleovská funkcia

**B-funkcia** $n$ premenných je zobrazenie $f: \{0, 1\}^n \to \{0, 1\}$. Má $2^n$ **bodov** (kombinácií vstupov) a v každom hodnotu 0 alebo 1, preto rôznych funkcií $n$ premenných je
$$2^{2^n}$$
Pre $n = 1$ sú to 4 funkcie, pre $n = 2$ ich je 16, pre $n = 3$ už 256.

**Neúplne definovaná** funkcia má v niektorých bodoch hodnotu neurčenú — označujeme ju **x** (je nám jedno, či tam bude 0 alebo 1, napr. ten vstup nikdy nenastane). Pri návrhu si ju môžeme zvoliť tak, aby bol obvod čo najjednoduchší.

## Spôsoby zápisu B-funkcie

Body číslujeme **desiatkovým ekvivalentom**: vstupné hodnoty čítame ako dvojkové číslo, **prvá premenná má najvyššiu váhu**. Pre $f(a, b, c)$ je bod $a = 1, b = 0, c = 1$ číslo $101_2 = 5$.

**a) Pravdivostná tabuľka** — riadok pre každý bod:

| $a$ | $b$ | $c$ | $f$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 |

**b) Číselný zápis** — zoznam bodov, kde je funkcia 1 (a zvlášť zoznam bodov s x). Pre funkciu z tabuľky: $f = \sum(1, 2, 3, 5, 7)$.

**c) Vektorový zápis** — stĺpec výstupov v poradí bodov 0, 1, 2, …: $f = (01110101)$.

**d) Mapa (Karnaughova)** — tabuľka, kde **susedné** políčka sa líšia hodnotou práve jednej premennej. Preto sú riadky a stĺpce v poradí Grayovho kódu 00, 01, 11, 10 (nie 00, 01, 10, 11!). Mapa funkcie $n$ premenných má $2^n$ políčok a každé políčko má práve $n$ susedov — aj „cez okraj“: krajné stĺpce sú susedné, mapa je v skutočnosti zvinutá do valca (pri 4 premenných do anuloidu).

| a \\ bc | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 0 | 1 | 1 | 1 |
| **1** | 0 | 1 | 1 | 0 |

Na prednáške sa mapa kreslí s pruhmi nad riadkami a stĺpcami (pruh = premenná má hodnotu 1); obsah je ten istý.

Mapa pre 4 premenné ($ab$ v riadkoch, $cd$ v stĺpcoch), v políčkach je číslo bodu:

| ab \\ cd | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 0 | 1 | 3 | 2 |
| **01** | 4 | 5 | 7 | 6 |
| **11** | 12 | 13 | 15 | 14 |
| **10** | 8 | 9 | 11 | 10 |

**e) Výraz** — vyjadruje, za akých hodnôt premenných je funkcia 1, napr. $f = \overline{a}b + c$.

::: drill d2-zapisy

::: quiz
Ktoré číslo má bod $a = 0, b = 1, c = 1, d = 0$ funkcie $f(a, b, c, d)$?
- [ ] 3
- [x] 6
- [ ] 9
> $0110_2 = 4 + 2 = 6$.
:::

::: quiz
V mape 4 premenných políčko bodu 0 **nesusedí** s
- [ ] 1
- [ ] 2
- [ ] 8
- [x] 3
> Susedia sa líšia v jednom bite: $0000$ má susedov $0001 = 1$, $0010 = 2$, $0100 = 4$, $1000 = 8$. Bod $3 = 0011$ sa líši v dvoch.
:::

## Funkcie jednej a dvoch premenných

Jedna premenná: konštanta 0, identita $x$, negácia $\overline{x}$, konštanta 1.

Šestnásť funkcií dvoch premenných; dôležité sú najmä tieto (vektor v poradí bodov 00, 01, 10, 11):

| názov | výraz | vektor | symbol |
|---|---|---|---|
| AND (súčin, konjunkcia) | $xy$ | 0001 | $x \cdot y$ |
| OR (súčet, disjunkcia) | $x + y$ | 0111 | |
| NAND (Shefferova funkcia) | $\overline{xy} = \overline{x} + \overline{y}$ | 1110 | $x \uparrow y$ |
| NOR (Peirceova funkcia) | $\overline{x + y} = \overline{x}\,\overline{y}$ | 1000 | $x \downarrow y$ |
| XOR (nonekvivalencia) | $\overline{x}y + x\overline{y}$ | 0110 | $x \oplus y$ |
| XNOR (ekvivalencia) | $\overline{x}\,\overline{y} + xy$ | 1001 | $\overline{x \oplus y}$ |
| implikácia $x \to y$ | $\overline{x} + y$ | 1101 | |
| inhibícia | $x\overline{y}$ | 0010 | |

Zvyšok tvoria konštanty, $x$, $y$, $\overline{x}$, $\overline{y}$ a obrátená implikácia a inhibícia.

**Úplný systém**: každú funkciu vieme zapísať pomocou AND, OR a NOT (stačí napísať súčet bodov, kde je 1). Úplný je aj samotný **NAND** ($\overline{x} = x \uparrow x$) a samotný **NOR**. Preto sa obvody dajú postaviť z jediného typu hradla.

**XOR viacerých premenných** $x_1 \oplus x_2 \oplus \dots \oplus x_n$ je 1 práve vtedy, keď **nepárny** počet premenných je 1 (parita).

::: drill d2-dve-premenne

::: quiz
Funkcia s vektorom 1001 je
- [ ] XOR
- [x] ekvivalencia (XNOR)
- [ ] NOR
> Je 1 v bodoch 00 a 11, teda keď sú premenné rovnaké.
:::

::: quiz
Koľko je rôznych B-funkcií troch premenných?
- [ ] 8
- [ ] 64
- [x] 256
> Bodov je $2^3 = 8$ a v každom volíme 0 alebo 1: $2^8 = 256$.
:::

## Logické členy

Každú základnú funkciu realizuje **logický člen (hradlo)**. Pre AND si môžete predstaviť dva spínače v sérii so žiarovkou, pre OR dva spínače paralelne, pre NOT spínač, ktorý žiarovku skratuje. Krúžok na výstupe značky znamená negáciu (NAND = AND s krúžkom).

Z výrazu sa obvod nakreslí priamo: každý operátor je jeden člen, zátvorky určujú poradie. Napríklad $f = \overline{a}b + c$ potrebuje invertor pre $a$, člen AND pre $\overline{a}b$ a člen OR na konci.

::: drill d2-vyraz

## Ako z tabuľky dostať výraz

Najpriamejšia cesta: pre každý bod s hodnotou 1 napíšte súčin všetkých premenných, kde premennú s hodnotou 0 znegujete; tieto súčiny spojte súčtom. Pre $f = \sum(1, 6)$ troch premenných: $f = \overline{a}\,\overline{b}c + ab\overline{c}$. Takýto výraz je správny, ale dlhý; ako ho skrátiť, ukáže ďalšia lekcia.

::: quiz
Pre $f(a, b) = \sum(0, 3)$ vyjde priamym zápisom
- [ ] $a + b$
- [x] $\overline{a}\,\overline{b} + ab$
- [ ] $\overline{a}b + a\overline{b}$
> Bod 0 = $00$ dáva $\overline{a}\,\overline{b}$, bod 3 = $11$ dáva $ab$.
:::

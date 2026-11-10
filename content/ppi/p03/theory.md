> Podľa 2.–4. prednášky PPI: normálne formy B-výrazov, implikanty a minimalizácia pomocou máp.

## B-výraz a B-algebra

**B-výraz** je reťazec z premenných, operátorov $+$, $\cdot$, negácie a zátvoriek. **B-algebra** je šestica $(B(n), +, \cdot, \overline{\phantom{a}}, 0, 1)$: množina všetkých B-výrazov $n$ premenných, tri operátory a dve konštanty. Platia v nej pravidlá z 1. lekcie. Jedna funkcia má nekonečne veľa výrazov; hľadáme ten, z ktorého vyjde **najlacnejší obvod**.

## Normálne formy

- **písmeno (literál)** — premenná alebo jej negácia: $a$, $\overline{a}$;
- **elementárny súčin** — súčin písmen, v ktorom sa žiadna premenná neopakuje: $a\overline{b}d$; **rád** $r$ = počet písmen;
- **elementárny súčet** — analogicky: $a + \overline{b} + d$.

**DNF** (disjunktívna normálna forma) je súčet elementárnych súčinov: $f = \sum g_j$, napr. $x_1\overline{x_2}x_3 + \overline{x_1}x_3 + x_4$ (rády 3, 2, 1).
**KNF** (konjunktívna normálna forma) je súčin elementárnych súčtov: $f = \prod h_j$, napr. $\overline{x_1}(\overline{x_2} + x_3)(\overline{x_3} + x_4 + x_5)$.

Druhy DNF (pre KNF analogicky):

| skratka | názov | čo obsahuje |
|---|---|---|
| **UDNF** | úplná | súčin rádu $n$ pre každý bod s hodnotou 1 (tzv. minterm) |
| **SDNF** | skrátená | **všetky** prosté implikanty |
| **IDNF** | iredundantná | len prosté implikanty a žiadny sa nedá vynechať |
| **MDNF** | minimálna | IDNF s najmenším počtom písmen (a členov) |
| **BDNF** | bezhazardná | pokrýva každú dvojicu susedných jednotiek spoločným členom (lekcia 4) |

**UKNF** má pre každý bod s hodnotou **0** súčet rádu $n$: premenná s hodnotou 0 je v ňom **bez** negácie, s hodnotou 1 **s** negáciou. Pre bod $a = 0, b = 1, c = 1$ je to $a + \overline{b} + \overline{c}$ — ten súčet je nulový práve v tomto bode.

Príklad: $f(a, b, c) = \sum(1, 3, 4, 5, 7)$.

| a \\ bc | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **0** | 0 | 1 | 1 | 0 |
| **1** | 1 | 1 | 1 | 0 |

- UDNF: $\overline{a}\,\overline{b}c + \overline{a}bc + a\overline{b}\,\overline{c} + a\overline{b}c + abc$
- UKNF (nuly v bodoch 0, 2, 6): $(a + b + c)(a + \overline{b} + c)(\overline{a} + \overline{b} + c)$
- MDNF: $c + a\overline{b}$, MKNF: $(a + c)(\overline{b} + c)$

::: drill d3-udnf

::: quiz
Ktorý súčet patrí do UKNF funkcie, ktorá je 0 v bode $a = 1, b = 0, c = 0$?
- [ ] $a + \overline{b} + \overline{c}$
- [x] $\overline{a} + b + c$
- [ ] $a\overline{b}\,\overline{c}$
> Súčet musí byť 0 práve v bode $100$: $\overline{1} + 0 + 0 = 0$.
:::

## Implikanty

**Implikant** funkcie $f$ je súčin, ktorý je 1 iba v bodoch, kde je $f$ rovná 1 alebo neurčená (x). Inými slovami, implikant „nikdy nepokryje nulu“.

**Prostý implikant** je implikant, z ktorého už nemožno vynechať žiadne písmeno — po vynechaní by pokryl nulu.

Dôsledky:

- SDNF obsahuje **všetky** prosté implikanty;
- IDNF (a teda aj MDNF) obsahuje **iba** prosté implikanty, ale len toľko, aby bol každý jednotkový bod pokrytý aspoň raz.

Duálne: **implicent** je súčet, ktorý je 0 iba tam, kde je $f$ nulová alebo neurčená; z prostých implicentov sa skladá MKNF.

::: quiz
Pre $f = \sum(1, 3, 4, 5, 7)$ je súčin $a\overline{b}c$
- [ ] prostý implikant
- [x] implikant, ale nie prostý
- [ ] nie je implikant
> Pokrýva len bod 5, kde $f = 1$, takže je implikant. Písmeno $a$ sa dá vynechať: $\overline{b}c$ pokrýva body 1 a 5, oba jednotkové. Prostý je až $c$.
:::

## Pravidelné konfigurácie v mape

Implikanty v mape vidíme ako **pravidelné konfigurácie**: obdĺžniky s $2^s$ políčkami ($s$ = stupeň konfigurácie: 1, 2, 4, 8, …), v ktorých má každé políčko práve $s$ susedov vo vnútri konfigurácie. Nezabúdajte, že mapa sa zvíja: okrajové stĺpce aj riadky sú susedné a štyri rohy mapy 4 premenných tvoria konfiguráciu.

Konfigurácia so $2^s$ políčkami v mape $n$ premenných zodpovedá súčinu rádu
$$r = n - s$$
Do súčinu idú len premenné, ktoré majú v celej konfigurácii **rovnakú** hodnotu (1 → premenná, 0 → negácia). Premenné, ktoré sa v konfigurácii menia, vypadnú.

::: drill d3-konfiguracie

## Postup hľadania MDNF z mapy

1. Pokryte všetky jednotky pravidelnými konfiguráciami tak, aby každá jednotka bola pokrytá aspoň raz. Neurčené body (x) **môžete** použiť, ak konfiguráciu zväčšia, ale nemusíte ich pokryť.
2. Konfigurácie volte **čo najväčšie** (menej písmen) a **čo najmenej** (menej členov). Pomáha začať jednotkami, ktoré sa dajú pokryť len jedným spôsobom (jadro, podstatné implikanty).
3. Každú konfiguráciu zapíšte súčinom a súčiny spojte súčtom.

Príklad 4 premenných, $f = \sum(0, 2, 5, 7, 8, 10, 13, 15)$:

| ab \\ cd | 00 | 01 | 11 | 10 |
|---|---|---|---|---|
| **00** | 1 | 0 | 0 | 1 |
| **01** | 0 | 1 | 1 | 0 |
| **11** | 0 | 1 | 1 | 0 |
| **10** | 1 | 0 | 0 | 1 |

Rohy a krajné stĺpce v riadkoch 00 a 10 (body 0, 2, 8, 10) dávajú $\overline{b}\,\overline{d}$; stred (5, 7, 13, 15) dáva $bd$. MDNF: $f = \overline{b}\,\overline{d} + bd$.

**MKNF** (duálny postup): pokryte **nuly** čo najväčšími konfiguráciami, každú zapíšte **súčtom** (hodnota 0 → premenná, hodnota 1 → negácia) a súčty spojte súčinom. Pre funkciu vyššie pokrývajú nuly konfigurácie $\overline{b}d$ a $b\overline{d}$, teda MKNF: $f = (b + \overline{d})(\overline{b} + d)$.

::: drill d3-mdnf

::: quiz
Konfigurácia so 4 políčkami v mape 4 premenných zodpovedá súčinu rádu
- [ ] 1
- [x] 2
- [ ] 4
> $r = n - s = 4 - 2 = 2$, napr. $bd$.
:::

::: quiz
Kedy je výhodnejšie použiť MKNF namiesto MDNF?
- [ ] vždy, KNF je kratšia
- [x] keď majú nuly väčšie a menej konfigurácií ako jednotky
- [ ] keď funkcia nemá neurčené body
> Rozhoduje počet písmen; ak je funkcia „skoro všade 1“, nuly sa pokryjú lacnejšie.
:::

## Neúplne definované funkcie

Políčka s **x** sa správajú ako žolík: v MDNF ich berieme ako 1 tam, kde to konfiguráciu zväčší, inak ako 0. V MKNF ich naopak môžeme pridať k nulám. Dôležité: výsledné MDNF a MKNF môžu x dodefinovať **rôzne**, každá forma zvlášť.

Typický príklad: číslica BCD (0 – 9) na 4 bitoch — kombinácie 10 až 15 nikdy neprídu, sú neurčené.

::: quiz
Funkcia $f(a, b) = \sum(0) + x(1)$, t. j. 1 v bode 0 a neurčená v bode 1. MDNF je
- [ ] $\overline{a}\,\overline{b}$
- [x] $\overline{a}$
- [ ] $\overline{b}$
> Bod 1 ($\overline{a}b$) použijeme ako 1, dvojica bodov 0 a 1 dá $\overline{a}$.
:::

## Skupinová minimalizácia a algoritmy

Ak obvod počíta viac funkcií naraz (napr. $f_1$ a $f_2$), oplatí sa hľadať **spoločné** súčiny — jeden člen AND môže napájať obe výstupné OR. Minimálna skupina DNF nemusí byť zložená z minimálnych DNF jednotlivých funkcií.

Mapy sú prakticky do 4–5 premenných. Pre viac premenných a pre počítače existujú algoritmy **Quine–McCluskey** (systematicky spája susedné body do väčších implikantov) a **Petrickova metóda** (vyberá minimálne pokrytie); ich detail je v odporúčanej literatúre.

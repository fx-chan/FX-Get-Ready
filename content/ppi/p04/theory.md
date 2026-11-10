> Podľa 3., 4. a 6. prednášky PPI: analýza a syntéza kombinačných obvodov, zmiešané normálne formy, hazardy a funkčné bloky (multiplexor, demultiplexor, dekodér, komparátor).

## Analýza kombinačného obvodu

**Úloha:** poznáme štruktúru obvodu (členy a ich prepojenie) a hľadáme jeho správanie. Úloha má vždy **jednoznačné** riešenie.

Postup: každému vnútornému vodiču dáme meno, od vstupov k výstupu zapíšeme výraz každého člena a dosadzujeme. Výsledok prepíšeme do tabuľky, vektora alebo zjednodušíme.

Príklad: $u = a \uparrow b$, $v = b \downarrow c$, $f = u + v$.
Potom $f = \overline{ab} + \overline{b + c} = \overline{a} + \overline{b} + \overline{b}\,\overline{c} = \overline{a} + \overline{b}$ (absorpcia).

::: drill d4-analyza

## Syntéza kombinačného obvodu

**Úloha:** je daná skupina B-funkcií a súbor povolených typov členov; navrhujeme štruktúru. Riešení je veľa, hľadáme **optimálne** — najčastejšie s najmenším počtom členov. Algoritmus poznáme hlavne pre **dvojstupňové** obvody z DNF a KNF:

1. zostavíme MDNF (alebo MKNF) z mapy;
2. každý súčin = jeden člen AND (prvý stupeň), súčet = jeden člen OR (druhý stupeň);
3. ak sú k dispozícii iné členy, výraz prevedieme na zmiešanú normálnu formu.

Dvojstupňové obvody sú **najrýchlejšie** — signál prejde len cez dva členy. Predpokladáme, že máme k dispozícii aj negácie vstupných premenných a že členy môžu mať ľubovoľný počet vstupov.

## Zmiešané normálne formy

Pomocou De Morganových pravidiel ($A + B = \overline{\overline{A}\,\overline{B}}$, $AB = \overline{\overline{A} + \overline{B}}$) prepíšeme DNF a KNF na formy s členmi NAND a NOR. Zápis „prvý stupeň / druhý stupeň“:

| základ | forma | príklad pre $f = ab + \overline{c}d$ resp. $f = (a + b)(\overline{c} + d)$ |
|---|---|---|
| DNF | AND / OR | $ab + \overline{c}d$ |
| DNF | **NAND / NAND** | $(a \uparrow b) \uparrow (\overline{c} \uparrow d)$ |
| DNF | OR / NAND | $(\overline{a} + \overline{b}) \uparrow (c + \overline{d})$ |
| DNF | NOR / OR | $(\overline{a} \downarrow \overline{b}) + (c \downarrow \overline{d})$ |
| KNF | OR / AND | $(a + b)(\overline{c} + d)$ |
| KNF | **NOR / NOR** | $(a \downarrow b) \downarrow (\overline{c} \downarrow d)$ |
| KNF | AND / NOR | $(\overline{a}\,\overline{b}) \downarrow (c\overline{d})$ |
| KNF | NAND / AND | $(\overline{a} \uparrow \overline{b})(c \uparrow \overline{d})$ |

Prakticky najdôležitejšie: **NAND/NAND vznikne z MDNF** (každý AND aj OR nahradíme NAND) a **NOR/NOR z MKNF**. Pozor na člen tvorený jediným písmenom: v NAND/NAND vstupuje do druhého stupňa **negovaný** ($f = ab + \overline{c} = (a \uparrow b) \uparrow c$).

Počet písmen v odvodenej forme je rovnaký ako v DNF alebo KNF, z ktorej vznikla. Pre každú funkciu (okrem konštánt) existuje každý typ formy.

V odpovediach píšte NAND ako `↑` (napr. `(a↑b)↑c`) a NOR ako `↓`.

::: drill d4-nand

::: quiz
Z MKNF sa priamo (bez úprav počtu členov) dostaneme k forme
- [ ] NAND / NAND
- [x] NOR / NOR
- [ ] AND / OR
> Súčin súčtov $\prod h_j = \overline{\sum \overline{h_j}}$ a $\overline{h_j}$ je NOR písmen súčtu.
:::

::: quiz
$f = ab + \overline{c}$ v tvare NAND/NAND je
- [ ] $(a \uparrow b) \uparrow \overline{c}$
- [x] $(a \uparrow b) \uparrow c$
- [ ] $(a \uparrow b) \uparrow (c \uparrow c) \uparrow c$
> $f = \overline{\overline{ab}\cdot\overline{\overline{c}}} = \overline{ab} \uparrow c$. Jednopísmenový člen ide do druhého stupňa negovaný.
:::

## Hazardy

Skutočné členy majú **oneskorenie** a nie všetky cesty signálu sú rovnako dlhé. Keď sa zmení jedna vstupná premenná, výstup môže na krátky okamih nadobudnúť nesprávnu hodnotu — **hazard**.

**Statický hazard** v DNF: výstup má zostať 1, ale pri zmene jednej premennej prechádza „zodpovednosť“ z jedného súčinu na iný. Ak starý súčin zhasne skôr, než sa nový rozsvieti, výstup krátko klesne na 0.

Príklad $f = a\overline{b} + bc$, pri $a = c = 1$ sa mení $b$: body $101$ a $111$ sú susedné jednotky, ale každú pokrýva iný súčin.

Riešenie — **bezhazardná DNF (BDNF)**: každú dvojicu **susedných jednotiek** pokryjeme aj **spoločnou** konfiguráciou. Pridáme teda konsenzus $ac$: $f = a\overline{b} + bc + ac$. Logicky je člen nadbytočný, ale odstráni hazard. Pre KNF duálne (susedné nuly). Vždy bezhazardná je SDNF (všetky prosté implikanty).

V asynchrónnych sekvenčných obvodoch sa objavujú aj **dynamické** a **podstatné** hazardy (lekcia 6).

::: drill d4-hazard

::: quiz
Má $f = \overline{a}b + ac$ statický hazard?
- [x] áno, pri $b = c = 1$ a zmene $a$
- [ ] nie, DNF hazard nikdy nemá
- [ ] áno, pri $a = 1$ a zmene $c$
> Body $011$ a $111$ sú susedné jednotky pokryté rôznymi súčinmi; chýba konsenzus $bc$.
:::

## Funkčné bloky

### Multiplexor (MUX)

Elektronický **prepínač vstupov**: podľa adresy $A_0, \dots, A_{m-1}$ pustí na výstup $Y$ jeden z dátových vstupov $D_0, \dots, D_{n-1}$. Platí
$$2^m = n, \qquad m = \log_2 n$$
Multiplexor 2 → 1: $Y = \overline{s}D_0 + sD_1$ — dva členy AND, jeden OR a jeden invertor. AND tu funguje ako **brána**: pustí údaj, len keď je jeho druhý vstup 1.
Multiplexor 4 → 1 s adresou $A_1A_0$: $Y = \overline{A_1}\,\overline{A_0}D_0 + \overline{A_1}A_0D_1 + A_1\overline{A_0}D_2 + A_1A_0D_3$.

Adresa nie je údaj, ale **riadenie** — tento rozdiel bude dôležitý pri stavbe procesora.

**MUX ako generátor funkcie**: ľubovoľnú $f(a, b, c)$ realizuje MUX 4 → 1, ak $a, b$ privedieme na adresu a na dátové vstupy dáme $0$, $1$, $c$ alebo $\overline{c}$. Pre adresu $ab$ sa pozrieme na dva body $abc$ s $c = 0$ a $c = 1$:

| hodnoty $f$ pre $c = 0, 1$ | 0 0 | 1 1 | 0 1 | 1 0 |
|---|---|---|---|---|
| na vstup $D_{ab}$ | $0$ | $1$ | $c$ | $\overline{c}$ |

::: drill d4-mux

### Demultiplexor (DEMUX)

Opačný smer — **prepínač výstupov**: vstup $D$ pošle na výstup $Y_i$ určený adresou, ostatné výstupy sú 0. Opäť $2^m = n$. Kostra je rovnaká ako pri MUX (invertory a AND), len chýba záverečný OR: $Y_i = D \cdot (\text{súčin adresy } i)$.

### Dekodér

Prevádza $m$-bitový kód na iný tvar. **Binárny dekodér** ($2^m = n$) aktivuje práve jeden z $n$ výstupov — výstup s číslom, ktoré je na vstupe (kód „1 z n“). Ďalší príklad: dekodér pre 7-segmentový displej (BCD → 7 segmentov). Binárny dekodér je vlastne DEMUX so vstupom $D = 1$.

### Komparátor

Porovná dve $n$-bitové čísla $A$, $B$ a nastaví jeden z výstupov $A = B$, $A > B$, $A < B$. Pre jednobitové čísla: $(A > B) = a\overline{b}$, $(A < B) = \overline{a}b$, $(A = B) = \overline{a \oplus b}$.

Ďalšie bloky — sčítačka, odčítačka, ALU — postavíme v 7. lekcii.

::: quiz
Koľko adresových vstupov má multiplexor s 32 dátovými vstupmi?
- [ ] 4
- [x] 5
- [ ] 16
> $2^5 = 32$.
:::

::: quiz
Demultiplexor 1 → 4 má adresu $A_1A_0 = 10$ a vstup $D = 1$. Výstupy $Y_0Y_1Y_2Y_3$ sú
- [ ] 1000
- [x] 0010
- [ ] 0100
> Adresa $10_2 = 2$, aktívny je $Y_2$.
:::

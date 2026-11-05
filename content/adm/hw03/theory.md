> Zdroj: Anton, Rorres, *Elementary Linear Algebra*, 11. vydanie, kapitoly 1.4, 1.5 a 1.6. Čísla viet sú z tejto knihy.

## Vlastnosti maticových operácií

Pre matice vhodných rozmerov a skaláry $a, b$ platí:

| sčítanie a skaláry | násobenie | transpozícia |
|---|---|---|
| $\mathbf{A}+\mathbf{B} = \mathbf{B}+\mathbf{A}$ | $(\mathbf{AB})\mathbf{C} = \mathbf{A}(\mathbf{BC})$ | $(\mathbf{A}^{\top})^{\top} = \mathbf{A}$ |
| $(\mathbf{A}+\mathbf{B})+\mathbf{C} = \mathbf{A}+(\mathbf{B}+\mathbf{C})$ | $\mathbf{A}(\mathbf{B}\pm\mathbf{C}) = \mathbf{AB}\pm\mathbf{AC}$ | $(\mathbf{A}\pm\mathbf{B})^{\top} = \mathbf{A}^{\top}\pm\mathbf{B}^{\top}$ |
| $(a+b)\mathbf{C} = a\mathbf{C}+b\mathbf{C}$ | $(\mathbf{B}+\mathbf{C})\mathbf{A} = \mathbf{BA}+\mathbf{CA}$ | $(a\mathbf{C})^{\top} = a\mathbf{C}^{\top}$ |
| $a(b\mathbf{C}) = (ab)\mathbf{C}$ | $a(\mathbf{BC}) = (a\mathbf{B})\mathbf{C} = \mathbf{B}(a\mathbf{C})$ | $(\mathbf{AB})^{\top} = \mathbf{B}^{\top}\mathbf{A}^{\top}$ |

Nulová matica: $\mathbf{A}+\mathbf{0} = \mathbf{A}$, $\mathbf{A0} = \mathbf{0}$. Jednotková: $\mathbf{AI} = \mathbf{IA} = \mathbf{A}$.
**Neplatí** komutatívnosť $\mathbf{AB} = \mathbf{BA}$ ani krátenie ($\mathbf{AB} = \mathbf{AC} \not\Rightarrow \mathbf{B} = \mathbf{C}$).

## Inverzná matica

Štvorcová matica $\mathbf{A}$ je **invertibilná (regulárna)**, ak existuje $\mathbf{A}^{-1}$ s
$\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$. Inak je **singulárna**. Inverzia je jednoznačná.

**Vzorec pre $2\times2$ (veta 1.4.5):**
$$\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix},\qquad ad - bc \ne 0$$
(prvky na diagonále vymeníme, mimo diagonály zmeníme znamienko, vydelíme determinantom).

::: drill d3-inverzia-2x2

::: quiz
Je $\begin{bmatrix}2&-4\\-4&8\end{bmatrix}$ invertibilná?
- [ ] áno, inverzia je $\frac{1}{16}\begin{bmatrix}8&4\\4&2\end{bmatrix}$
- [x] nie, $ad - bc = 16 - 16 = 0$
- [ ] áno, lebo nemá nulový riadok
> Riadky sú lineárne závislé ($R_2 = -2R_1$), determinant je 0.
:::

**Vlastnosti** (vety 1.4.6, 1.4.7, 1.4.9; pre invertibilné $\mathbf{A}, \mathbf{B}$ a $k \ne 0$):

- $(\mathbf{A}^{-1})^{-1} = \mathbf{A}$, $(\mathbf{A}^{\top})^{-1} = (\mathbf{A}^{-1})^{\top}$,
- $(\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$ a $(\mathbf{ABC})^{-1} = \mathbf{C}^{-1}\mathbf{B}^{-1}\mathbf{A}^{-1}$ — **poradie sa otočí**,
- $(k\mathbf{A})^{-1} = \frac1k\mathbf{A}^{-1}$, $\mathbf{A}^{-n} = (\mathbf{A}^{-1})^n = (\mathbf{A}^n)^{-1}$.

::: drill d3-vlastnosti

**Hľadanie $\mathbf{A}$ z inverzie:** invertujte obe strany. Z $(7\mathbf{A})^{-1} = \mathbf{M}$ dostaneme
$7\mathbf{A} = \mathbf{M}^{-1}$, $\mathbf{A} = \frac17\mathbf{M}^{-1}$. Z $(\mathbf{I}+2\mathbf{A})^{-1} = \mathbf{M}$:
$\mathbf{A} = \frac12(\mathbf{M}^{-1} - \mathbf{I})$.

**Rovnice s maticami:** násobte zľava alebo sprava a **zachovajte poradie**:
$\mathbf{AXB} = \mathbf{C} \Rightarrow \mathbf{X} = \mathbf{A}^{-1}\mathbf{C}\mathbf{B}^{-1}$ (nie $\mathbf{A}^{-1}\mathbf{B}^{-1}\mathbf{C}$!).

::: quiz
Z rovnice $\mathbf{AXB} = \mathbf{C}$ ($\mathbf{A}, \mathbf{B}$ invertibilné) vyplýva
- [ ] $\mathbf{X} = \mathbf{C}\mathbf{A}^{-1}\mathbf{B}^{-1}$
- [x] $\mathbf{X} = \mathbf{A}^{-1}\mathbf{C}\mathbf{B}^{-1}$
- [ ] $\mathbf{X} = \mathbf{A}^{-1}\mathbf{B}^{-1}\mathbf{C}$
> Zľava vynásobíme $\mathbf{A}^{-1}$ a sprava $\mathbf{B}^{-1}$: $\mathbf{A}^{-1}\mathbf{AXB}\mathbf{B}^{-1} = \mathbf{X}$.
:::

## Polynóm matice

Pre $p(x) = a_0 + a_1x + \dots + a_mx^m$ definujeme $p(\mathbf{A}) = a_0\mathbf{I} + a_1\mathbf{A} + \dots + a_m\mathbf{A}^m$
— **konštantu násobíme maticou $\mathbf{I}$**. Lebo mocniny $\mathbf{A}$ navzájom komutujú, platí
$p(x) = p_1(x)p_2(x) \Rightarrow p(\mathbf{A}) = p_1(\mathbf{A})p_2(\mathbf{A})$, napr. $\mathbf{A}^2 - 9\mathbf{I} = (\mathbf{A}+3\mathbf{I})(\mathbf{A}-3\mathbf{I})$.

::: quiz
$p(x) = x^2 - 2x + 3$. Čomu sa rovná $p(\mathbf{A})$?
- [ ] $\mathbf{A}^2 - 2\mathbf{A} + 3$
- [x] $\mathbf{A}^2 - 2\mathbf{A} + 3\mathbf{I}$
- [ ] $(\mathbf{A} - 3\mathbf{I})(\mathbf{A} + \mathbf{I})$
> K matici nemožno pripočítať číslo — konštanta 3 sa zmení na $3\mathbf{I}$.
:::

## Elementárne matice

**Elementárna matica** vznikne z $\mathbf{I}_n$ **jednou** elementárnou riadkovou operáciou. Vynásobenie
$\mathbf{EA}$ (zľava) urobí s $\mathbf{A}$ tú istú operáciu.

| operácia | príklad $\mathbf{E}$ ($3\times3$) | $\mathbf{E}^{-1}$ |
|---|---|---|
| výmena $R_1 \leftrightarrow R_3$ | $\begin{bmatrix}0&0&1\\0&1&0\\1&0&0\end{bmatrix}$ | tá istá výmena |
| $R_2 \to 5R_2$ | $\begin{bmatrix}1&0&0\\0&5&0\\0&0&1\end{bmatrix}$ | $R_2 \to \frac15R_2$ |
| $R_3 \to R_3 - 2R_1$ | $\begin{bmatrix}1&0&0\\0&1&0\\-2&0&1\end{bmatrix}$ | $R_3 \to R_3 + 2R_1$ |

Vynásobenie $\mathbf{EA}$ je veta 1.5.1. Elementárna matica je vždy invertibilná a jej inverzia je tiež elementárna, je to opačná operácia (veta 1.5.2).
Matica, ktorá vznikne **dvoma** operáciami (napr. $-1$ na diagonále a zároveň výmena), elementárna nie je.

::: drill d3-elementarna

::: quiz
Je $\begin{bmatrix}-5&1\\1&0\end{bmatrix}$ elementárna?
- [x] nie — nedá sa získať z $\mathbf{I}_2$ jednou operáciou
- [ ] áno, výmena riadkov
- [ ] áno, pripočítanie násobku
> Výmena dá $\begin{bmatrix}0&1\\1&0\end{bmatrix}$; prvok $-5$ by vyžadoval ešte ďalšiu operáciu.
:::

## Výpočet inverzie elimináciou

Upravujeme $[\mathbf{A}\,|\,\mathbf{I}]$ riadkovými operáciami, kým vľavo nie je $\mathbf{I}$:
$$[\mathbf{A}\,|\,\mathbf{I}] \longrightarrow [\mathbf{I}\,|\,\mathbf{A}^{-1}]$$
Ak sa vľavo objaví **nulový riadok**, $\mathbf{A}$ nie je invertibilná.

Prečo to funguje: ak $\mathbf{E}_k\cdots\mathbf{E}_2\mathbf{E}_1\mathbf{A} = \mathbf{I}$, potom
$\mathbf{A}^{-1} = \mathbf{E}_k\cdots\mathbf{E}_1$ a $\mathbf{A} = \mathbf{E}_1^{-1}\mathbf{E}_2^{-1}\cdots\mathbf{E}_k^{-1}$ —
každá invertibilná matica je **súčin elementárnych matíc**.

::: drill d3-gauss-jordan

**Ekvivalentné tvrdenia** (vety 1.5.3, 1.6.4, 2.3.8) pre štvorcovú $\mathbf{A}$ ($n\times n$):
$\mathbf{A}$ je invertibilná $\iff$ RREF$(\mathbf{A}) = \mathbf{I}$ $\iff$ $\mathbf{Ax} = \mathbf{0}$ má len triviálne riešenie
$\iff$ $\mathbf{Ax} = \mathbf{b}$ má jediné riešenie pre každé $\mathbf{b}$ $\iff$ $\mathbf{A}$ je súčin elementárnych matíc
$\iff$ $\det\mathbf{A} \ne 0$.

**Riadková ekvivalencia:** $\mathbf{A} \sim \mathbf{B}$, ak sa $\mathbf{B}$ dá získať z $\mathbf{A}$ riadkovými operáciami,
t.j. $\mathbf{B} = \mathbf{CA}$ pre nejakú invertibilnú $\mathbf{C}$ (súčin elementárnych matíc). Dve matice sú
riadkovo ekvivalentné práve vtedy, keď majú rovnaký RREF.

::: quiz
Pri úprave $[\mathbf{A}\,|\,\mathbf{I}]$ vyšiel vľavo riadok $[0\;0\;0]$. Čo to znamená?
- [ ] treba vymeniť riadky a pokračovať
- [x] $\mathbf{A}$ nie je invertibilná
- [ ] $\mathbf{A}^{-1}$ má nulový riadok
> Nulový riadok znamená, že RREF$(\mathbf{A}) \ne \mathbf{I}$.
:::

## Sústavy cez inverznú maticu

Ak je $\mathbf{A}$ **štvorcová a invertibilná**, sústava $\mathbf{Ax} = \mathbf{b}$ má jediné riešenie
$$\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}.$$
Výhoda: pre viac pravých strán stačí jedna inverzia. Rovnako dobre môžeme naraz eliminovať $[\mathbf{A}\,|\,\mathbf{b}_1\,|\,\mathbf{b}_2]$ (kapitola 1.6). Ak $\mathbf{A}$ nie je štvorcová alebo je singulárna,
metóda sa použiť nedá — sústava má vtedy žiadne alebo nekonečne veľa riešení (riešime elimináciou).

::: drill d3-sustava

**Vety 1.6.3 a 1.6.5:** pri štvorcových maticiach stačí overiť jednu stranu: ak $\mathbf{BA} = \mathbf{I}$, potom už $\mathbf{B} = \mathbf{A}^{-1}$. Ak je súčin $\mathbf{AB}$ štvorcových matíc invertibilný, sú invertibilné aj $\mathbf{A}$ a $\mathbf{B}$.

::: quiz
Homogénna sústava $\mathbf{Ax} = \mathbf{0}$ s invertibilnou $\mathbf{A}$ má
- [x] len triviálne riešenie $\mathbf{x} = \mathbf{A}^{-1}\mathbf{0} = \mathbf{0}$
- [ ] nekonečne veľa riešení
- [ ] žiadne riešenie
> Netriviálne riešenie by existovalo len pre singulárnu $\mathbf{A}$.
:::

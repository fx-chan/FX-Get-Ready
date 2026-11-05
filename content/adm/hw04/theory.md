## Determinant 2×2 a 3×3

Determinant je **číslo** priradené **štvorcovej** matici. Pre nečtvorcovú maticu nie je definovaný.

$$\det\begin{bmatrix}a&b\\c&d\end{bmatrix} = \begin{vmatrix}a&b\\c&d\end{vmatrix} = ad - bc$$

::: drill d4-2x2

**Sarrusovo pravidlo (len $3\times3$!):** pripíšeme prvé dva stĺpce, sčítame súčiny troch diagonál zľava hore
doprava dole a odčítame súčiny troch diagonál sprava hore doľava dole:

$$\begin{vmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\\a_{31}&a_{32}&a_{33}\end{vmatrix} =
a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32} - a_{13}a_{22}a_{31} - a_{11}a_{23}a_{32} - a_{12}a_{21}a_{33}$$

::: drill d4-sarrus

::: quiz
Dá sa Sarrusovo pravidlo použiť pre maticu $4\times4$?
- [ ] áno, pripíšeme tri stĺpce
- [x] nie, platí len pre $3\times3$ — pre väčšie matice rozvoj alebo redukcia
- [ ] áno, ak má matica veľa núl
> Pre $4\times4$ má determinant 24 členov, Sarrus by dal len 8.
:::

## Minory, kofaktory a rozvoj

- **Minor** $M_{ij}$ = determinant matice, ktorá vznikne vyškrtnutím $i$-teho riadku a $j$-teho stĺpca.
- **Kofaktor** (algebraický doplnok) $C_{ij} = (-1)^{i+j}M_{ij}$ — znamienka podľa šachovnice
  $\begin{smallmatrix}+&-&+\\-&+&-\\+&-&+\end{smallmatrix}$.

::: drill d4-kofaktor

**Laplaceov rozvoj** podľa $i$-teho riadku alebo $j$-teho stĺpca:
$$\det\mathbf{A} = \sum_{j=1}^{n} a_{ij}C_{ij} = \sum_{i=1}^{n} a_{ij}C_{ij}$$
Výsledok nezávisí od výberu riadku/stĺpca → vyberte ten s **najviac nulami** (nulové prvky netreba počítať).

$$\begin{vmatrix}-3&0&7\\2&5&1\\-1&0&5\end{vmatrix} \overset{\text{2. stĺpec}}{=} 5\cdot(-1)^{2+2}\begin{vmatrix}-3&7\\-1&5\end{vmatrix} = 5(-15+7) = -40$$

::: quiz
Pri rozvoji podľa 2. riadku matice $3\times3$ majú kofaktory $C_{21}, C_{22}, C_{23}$ znamienka
- [ ] $+, -, +$
- [x] $-, +, -$
- [ ] $+, +, +$
> $(-1)^{2+1} = -1$, $(-1)^{2+2} = +1$, $(-1)^{2+3} = -1$.
:::

## Špeciálne prípady — spamäti

- **trojuholníková** (aj diagonálna) matica: $\det$ = súčin prvkov na diagonále, $\det\mathbf{I} = 1$,
- **nulový riadok/stĺpec** → $\det = 0$,
- **dva rovnaké alebo úmerné riadky** (stĺpce) → $\det = 0$; všeobecne: lineárne závislé riadky → 0,
- **elementárne matice**: výmena riadkov → $-1$, $kR_i$ → $k$, $R_i + kR_j$ → $1$.

::: drill d4-trojuholnikova

## Riadkové operácie a determinant

| operácia | čo sa stane s $\det$ |
|---|---|
| výmena dvoch riadkov | zmení **znamienko** |
| vynásobenie riadku číslom $k$ | vynásobí sa $k$ (pri vytknutí: $\det$ = $k\cdot$ nový) |
| pripočítanie násobku iného riadku | **nezmení sa** |

Rovnako pre stĺpce. **Metóda riadkovej redukcie:** upravíme na trojuholníkovú maticu, sledujeme výmeny a vytknuté
čísla, determinant = (znamienko) · (vytknuté čísla) · (súčin diagonály).

$$\begin{vmatrix}3&-6&9\\-2&7&-2\\0&1&5\end{vmatrix} = 3\begin{vmatrix}1&-2&3\\-2&7&-2\\0&1&5\end{vmatrix}
= 3\begin{vmatrix}1&-2&3\\0&3&4\\0&1&5\end{vmatrix} = 3\cdot1\cdot(15-4) = 33$$

::: drill d4-operacie

::: quiz
$\det\mathbf{A} = -6$ ($3\times3$). Akú hodnotu má determinant, ak prvý riadok presunieme na koniec (riadky $2, 3, 1$)?
- [ ] 6
- [x] $-6$
- [ ] $-18$
> Presun prvého riadku na koniec = dve výmeny, znamienko sa zmení dvakrát.
:::

## Ďalšie vlastnosti

Pre štvorcové matice $n\times n$:

| | |
|---|---|
| $\det(\mathbf{A}^{\top}) = \det\mathbf{A}$ | riadky a stĺpce sú rovnocenné |
| $\det(\mathbf{AB}) = \det\mathbf{A}\cdot\det\mathbf{B}$ | ale $\det(\mathbf{A}+\mathbf{B}) \ne \det\mathbf{A} + \det\mathbf{B}$ |
| $\det(k\mathbf{A}) = k^n\det\mathbf{A}$ | **každý** z $n$ riadkov sa násobí $k$ |
| $\det(\mathbf{A}^{-1}) = \dfrac{1}{\det\mathbf{A}}$ | |
| $\mathbf{A}$ je invertibilná $\iff \det\mathbf{A} \ne 0$ | |
| blokovo trojuholníková: $\det\begin{bmatrix}\mathbf{A}&\mathbf{C}\\\mathbf{0}&\mathbf{B}\end{bmatrix} = \det\mathbf{A}\det\mathbf{B}$ | $\mathbf{A}, \mathbf{B}$ štvorcové |

::: quiz
$\mathbf{A}$ je $3\times3$ a $\det\mathbf{A} = 4$. Čomu sa rovná $\det(2\mathbf{A})$?
- [ ] 8
- [x] 32
- [ ] 16
> $2^3\cdot 4 = 32$ — násobí sa každý z troch riadkov.
:::

## Determinant s parametrom

Pri $\det(\mathbf{A}) = 0$ s neznámou $\lambda$ alebo $x$ dostaneme **polynomickú rovnicu**. Napr.
$\begin{vmatrix}\lambda-2&1\\-5&\lambda+4\end{vmatrix} = (\lambda-2)(\lambda+4)+5 = \lambda^2+2\lambda-3 = (\lambda+3)(\lambda-1)$,
teda $\lambda \in \{-3, 1\}$. Pri trojuholníkovej matici sú korene priamo prvky diagonály.
(Tento postup sa vráti pri **vlastných číslach** v DÚ 07.)

::: quiz
Pre aké $x$ je $\begin{vmatrix}x-3&5&-19\\0&x-1&6\\0&0&x-2\end{vmatrix} = 0$?
- [ ] len $x = 3$
- [x] $x \in \{1, 2, 3\}$
- [ ] $x \in \{-1, -2, -3\}$
> Matica je horná trojuholníková: $\det = (x-3)(x-1)(x-2)$.
:::

## Adjungovaná matica a Cramerovo pravidlo

**Adjungovaná matica** je transponovaná matica kofaktorov: $\operatorname{adj}(\mathbf{A}) = [C_{ij}]^{\top}$. Platí
$\mathbf{A}\operatorname{adj}(\mathbf{A}) = \det(\mathbf{A})\,\mathbf{I}$, preto
$$\mathbf{A}^{-1} = \frac{1}{\det\mathbf{A}}\operatorname{adj}(\mathbf{A}).$$

**Cramerovo pravidlo:** ak $\det\mathbf{A} \ne 0$, sústava $\mathbf{Ax} = \mathbf{b}$ má riešenie
$x_j = \dfrac{\det\mathbf{A}_j}{\det\mathbf{A}}$, kde $\mathbf{A}_j$ je $\mathbf{A}$ s $j$-tym stĺpcom nahradeným $\mathbf{b}$.

::: quiz
Pri adjungovanej matici sa často zabúda na
- [ ] násobenie determinantom
- [x] transpozíciu matice kofaktorov
- [ ] výmenu riadkov
> $\operatorname{adj}(\mathbf{A})_{ij} = C_{ji}$ — kofaktor z riadku $j$ a stĺpca $i$.
:::

## Vektory / Векторы

**Vektor** v $\mathbb{R}^n$ je usporiadaná $n$-tica čísel. Zapisujeme ho ako **riadkový** vektor
$(v_1, v_2, \dots, v_n)$ alebo ako **stĺpcový** vektor (matica $n\times 1$). Vektor je špeciálny prípad matice.

| operácia | zápis | výsledok |
|---|---|---|
| súčet | $\mathbf{u}+\mathbf{v} = (u_1+v_1, \dots, u_n+v_n)$ | vektor |
| násobok skalárom | $k\mathbf{v} = (kv_1, \dots, kv_n)$ | vektor |
| skalárny súčin | $\mathbf{u}\cdot\mathbf{v} = u_1v_1 + \dots + u_nv_n$ | **číslo** |
| dĺžka (norma) | $\lVert\mathbf{v}\rVert = \sqrt{v_1^2+\dots+v_n^2} = \sqrt{\mathbf{v}\cdot\mathbf{v}}$ | číslo $\ge 0$ |

Ak $\mathbf{u}\cdot\mathbf{v} = 0$, vektory sú **kolmé (ortogonálne)**. Sčítať sa dajú len vektory rovnakej dĺžky.

::: quiz
Aký je skalárny súčin $\mathbf{u} = (2, -1, 3)$ a $\mathbf{v} = (1, 4, 2)$? / Скалярное произведение?
- [ ] $(2, -4, 6)$
- [x] $4$
- [ ] $12$
- [ ] nedá sa vypočítať
> $2\cdot1 + (-1)\cdot4 + 3\cdot2 = 2 - 4 + 6 = 4$. Skalárny súčin je číslo, nie vektor.
:::

## Matica — základné pojmy / Матрица — основные понятия

**Matica rozmeru $m\times n$** má $m$ riadkov a $n$ stĺpcov. Prvok v $i$-tom riadku a $j$-tom stĺpci je $a_{ij}$
(najprv **riadok**, potom **stĺpec**).

$$\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix}\quad (2\times 3)$$

- dve matice sa **rovnajú**, ak majú rovnaký rozmer a rovnaké všetky prvky,
- matica je **štvorcová**, ak $m = n$; prvky $a_{11}, a_{22}, \dots, a_{nn}$ tvoria **hlavnú diagonálu**,
- **nulová matica** $\mathbf{0}$ má všetky prvky 0, **jednotková (identická)** $\mathbf{I}_n$ má na diagonále 1, inde 0.

::: quiz
Matica $\mathbf{A}$ má rozmer $3\times 4$. Koľko má prvkov a ktorý prvok **neexistuje**?
- [ ] 7 prvkov, neexistuje $a_{34}$
- [x] 12 prvkov, neexistuje $a_{43}$
- [ ] 12 prvkov, neexistuje $a_{34}$
> 3 riadky × 4 stĺpce = 12 prvkov. $a_{43}$ by bol 4. riadok — ten matica nemá.
:::

## Špeciálne štvorcové matice / Специальные матрицы

| typ | podmienka | príklad |
|---|---|---|
| diagonálna | $a_{ij} = 0$ pre $i \ne j$ | $\begin{bmatrix}2&0\\0&-1\end{bmatrix}$ |
| horná trojuholníková | $a_{ij} = 0$ pre $i > j$ (pod diagonálou nuly) | $\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix}$ |
| dolná trojuholníková | $a_{ij} = 0$ pre $i < j$ (nad diagonálou nuly) | $\begin{bmatrix}0&0&0\\1&0&0\\1&1&0\end{bmatrix}$ |
| symetrická | $\mathbf{A}^{\top} = \mathbf{A}$, t.j. $a_{ij} = a_{ji}$ | $\begin{bmatrix}1&5\\5&3\end{bmatrix}$ |
| skoseno-symetrická | $\mathbf{A}^{\top} = -\mathbf{A}$, t.j. $a_{ij} = -a_{ji}$, na diagonále 0 | $\begin{bmatrix}0&2\\-2&0\end{bmatrix}$ |

> Diagonálna matica je **zároveň** horná aj dolná trojuholníková a je symetrická. Nulová štvorcová matica
> je jediná, ktorá je symetrická aj skoseno-symetrická. Nečtvorcová matica nemá žiadny z týchto typov.

::: quiz
Je matica $\begin{bmatrix}0&0&6\\0&-6&0\\-6&0&0\end{bmatrix}$ skoseno-symetrická?
- [ ] áno, lebo $a_{13} = -a_{31}$
- [x] nie, lebo na diagonále je $-6 \ne 0$
- [ ] áno, lebo je štvorcová
> Skoseno-symetrická matica musí mať $a_{ii} = -a_{ii}$, teda nuly na diagonále. Prvok $a_{22} = -6$ to porušuje.
:::

::: drill d1-typ

## Sčítanie a násobenie skalárom / Сложение и умножение на число

- $\mathbf{A}+\mathbf{B}$ — sčítame prvky na rovnakých pozíciách. **Iba pre matice rovnakého rozmeru.**
- $k\mathbf{A}$ — každý prvok vynásobíme číslom $k$. Rozdiel: $\mathbf{A}-\mathbf{B} = \mathbf{A}+(-1)\mathbf{B}$.
- **lineárna kombinácia**: $2\mathbf{A} - 3\mathbf{B} + \mathbf{C}$ — najprv násobky, potom súčty.

$$2\begin{bmatrix}1&-2\\3&0\end{bmatrix} - \begin{bmatrix}4&1\\-1&5\end{bmatrix} = \begin{bmatrix}-2&-5\\7&-5\end{bmatrix}$$

Vlastnosti: $\mathbf{A}+\mathbf{B} = \mathbf{B}+\mathbf{A}$, $(\mathbf{A}+\mathbf{B})+\mathbf{C} = \mathbf{A}+(\mathbf{B}+\mathbf{C})$,
$k(\mathbf{A}+\mathbf{B}) = k\mathbf{A}+k\mathbf{B}$, $\mathbf{A}-\mathbf{A} = \mathbf{0}$.

::: drill d1-scitanie

## Transponovaná matica / Транспонирование

$\mathbf{A}^{\top}$ vznikne výmenou riadkov a stĺpcov: $(\mathbf{A}^{\top})_{ij} = a_{ji}$. Matica $m\times n$ sa zmení na $n\times m$.

$$\begin{bmatrix}2&0&-1\\5&3&4\end{bmatrix}^{\top} = \begin{bmatrix}2&5\\0&3\\-1&4\end{bmatrix}$$

| vlastnosť | |
|---|---|
| $(\mathbf{A}^{\top})^{\top} = \mathbf{A}$ | dvakrát transponovať = nič nezmeniť |
| $(\mathbf{A}+\mathbf{B})^{\top} = \mathbf{A}^{\top}+\mathbf{B}^{\top}$ | |
| $(k\mathbf{A})^{\top} = k\mathbf{A}^{\top}$ | |
| $(\mathbf{AB})^{\top} = \mathbf{B}^{\top}\mathbf{A}^{\top}$ | **poradie sa otočí!** |

::: quiz
$\mathbf{C}$ má rozmer $2\times 2$ a $\mathbf{F}$ rozmer $3\times 2$. Dá sa vypočítať $2\mathbf{C}^{\top} - 3\mathbf{F}$?
- [ ] áno, výsledok je $3\times 2$
- [ ] áno, výsledok je $2\times 2$
- [x] nie, $\mathbf{C}^{\top}$ je $2\times2$ a $\mathbf{F}$ je $3\times2$
> Transpozícia štvorcovej matice nezmení rozmer. Odčítať sa dajú len matice rovnakého rozmeru.
:::

::: drill d1-transpozicia

## Stopa matice / След матрицы

**Stopa** štvorcovej matice je súčet prvkov hlavnej diagonály: $\operatorname{tr}(\mathbf{A}) = a_{11} + a_{22} + \dots + a_{nn}$.
Pre nečtvorcovú maticu stopa **nie je definovaná**.

- $\operatorname{tr}(\mathbf{A}+\mathbf{B}) = \operatorname{tr}\mathbf{A} + \operatorname{tr}\mathbf{B}$, $\operatorname{tr}(k\mathbf{A}) = k\operatorname{tr}\mathbf{A}$,
- $\operatorname{tr}(\mathbf{A}^{\top}) = \operatorname{tr}\mathbf{A}$ (diagonála sa transpozíciou nemení),
- $\operatorname{tr}(\mathbf{AB}) = \operatorname{tr}(\mathbf{BA})$, aj keď $\mathbf{AB} \ne \mathbf{BA}$.

> Trik: pri $\operatorname{tr}(\mathbf{DE}^{\top})$ netreba počítať celý súčin — stačia diagonálne prvky:
> $(\mathbf{DE}^{\top})_{ii}$ = skalárny súčin $i$-teho riadku $\mathbf{D}$ a $i$-teho riadku $\mathbf{E}$.

::: drill d1-stopa

## Násobenie matíc / Умножение матриц

Súčin $\mathbf{AB}$ existuje, iba ak **počet stĺpcov $\mathbf{A}$ = počet riadkov $\mathbf{B}$**:

$$\underbrace{\mathbf{A}}_{m\times \color{red}{n}}\;\underbrace{\mathbf{B}}_{\color{red}{n}\times p} = \underbrace{\mathbf{C}}_{m\times p},\qquad
c_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \dots + a_{in}b_{nj}$$

Prvok $c_{ij}$ = skalárny súčin **$i$-teho riadku $\mathbf{A}$** a **$j$-teho stĺpca $\mathbf{B}$**.

$$\begin{bmatrix}1&2\\3&4\end{bmatrix}\begin{bmatrix}0&1\\-1&2\end{bmatrix} =
\begin{bmatrix}1\cdot0+2\cdot(-1) & 1\cdot1+2\cdot2\\ 3\cdot0+4\cdot(-1) & 3\cdot1+4\cdot2\end{bmatrix} =
\begin{bmatrix}-2&5\\-4&11\end{bmatrix}$$

::: drill d1-rozmer
::: drill d1-sucin

**Jeden riadok alebo stĺpec súčinu** — netreba počítať celú maticu:

- $i$-ty riadok $\mathbf{AB}$ = ($i$-ty riadok $\mathbf{A}$) $\cdot\,\mathbf{B}$,
- $j$-ty stĺpec $\mathbf{AB}$ = $\mathbf{A}\,\cdot$ ($j$-ty stĺpec $\mathbf{B}$).

**Mocnina** $\mathbf{A}^k = \mathbf{A}\mathbf{A}\cdots\mathbf{A}$ existuje len pre **štvorcovú** maticu; $\mathbf{A}^0 = \mathbf{I}$.
Súčin riadkového vektora $1\times n$ a stĺpcového $n\times1$ je matica $1\times1$ (číslo), v opačnom poradí $n\times n$.

::: quiz
$\mathbf{R}$ je $1\times3$ a $\mathbf{J}$ je $3\times1$. Aké rozmery majú $\mathbf{RJ}$ a $\mathbf{JR}$?
- [ ] obe $1\times1$
- [x] $\mathbf{RJ}$ je $1\times1$, $\mathbf{JR}$ je $3\times3$
- [ ] $\mathbf{JR}$ sa nedá vypočítať
> $(1\times\underline{3})(\underline{3}\times1) = 1\times1$ a $(3\times\underline{1})(\underline{1}\times3) = 3\times3$ — vnútorné čísla sa rovnajú v oboch prípadoch.
:::

## Vlastnosti násobenia / Свойства умножения

| platí ✓ | neplatí ✗ (vo všeobecnosti) |
|---|---|
| $(\mathbf{AB})\mathbf{C} = \mathbf{A}(\mathbf{BC})$ — asociatívnosť | $\mathbf{AB} = \mathbf{BA}$ — komutatívnosť |
| $\mathbf{A}(\mathbf{B}+\mathbf{C}) = \mathbf{AB}+\mathbf{AC}$ — ľavý distributívny zákon | $\mathbf{AB} = \mathbf{AC} \Rightarrow \mathbf{B} = \mathbf{C}$ — krátenie |
| $(\mathbf{B}+\mathbf{C})\mathbf{A} = \mathbf{BA}+\mathbf{CA}$ — pravý distributívny zákon | $\mathbf{AB} = \mathbf{0} \Rightarrow \mathbf{A}=\mathbf{0}$ alebo $\mathbf{B}=\mathbf{0}$ |
| $k(\mathbf{AB}) = (k\mathbf{A})\mathbf{B} = \mathbf{A}(k\mathbf{B})$ | $(\mathbf{A}+\mathbf{B})^2 = \mathbf{A}^2+2\mathbf{AB}+\mathbf{B}^2$ |
| $\mathbf{AI} = \mathbf{IA} = \mathbf{A}$, $(\mathbf{AB})^{\top} = \mathbf{B}^{\top}\mathbf{A}^{\top}$ | $(\mathbf{AB})^{\top} = \mathbf{A}^{\top}\mathbf{B}^{\top}$ |

Matice sú **komutatívne**, ak $\mathbf{AB} = \mathbf{BA}$ (napr. každá matica s $\mathbf{I}$, s $\mathbf{0}$ alebo so sebou samou).
Ak $\mathbf{AB}$ a $\mathbf{BA}$ majú rôzny rozmer, rovnať sa nemôžu.

::: quiz
Ktorá rovnosť platí pre všetky matice vhodných rozmerov?
- [ ] $\mathbf{L}(\mathbf{ML}) = \mathbf{L}^2\mathbf{M}$
- [x] $\mathbf{E}(\mathbf{FK}) = (\mathbf{EF})\mathbf{K}$
- [ ] $(\mathbf{AK})^{\top} = \mathbf{A}^{\top}\mathbf{K}^{\top}$
> Asociatívnosť platí vždy. $\mathbf{L}(\mathbf{ML}) = \mathbf{LML}$, čo sa rovná $\mathbf{L}^2\mathbf{M}$ len ak $\mathbf{L}$ a $\mathbf{M}$ komutujú. Transpozícia súčinu otáča poradie.
:::

::: quiz
$\mathbf{A} = \begin{bmatrix}0&1\\0&0\end{bmatrix}$. Čomu sa rovná $\mathbf{A}^2$?
- [ ] $\mathbf{A}$
- [x] nulovej matici, hoci $\mathbf{A} \ne \mathbf{0}$
- [ ] $\mathbf{I}$
> $\mathbf{A}^2 = \begin{bmatrix}0\cdot0+1\cdot0 & 0\cdot1+1\cdot0\\0&0\end{bmatrix} = \mathbf{0}$. Súčin nenulových matíc môže byť nulový.
:::

## Na písomke / На контрольной

1. Pred každým výpočtom **skontrolujte rozmery** — časť úloh sa zámerne vypočítať nedá.
2. Transpozíciu súčinu rozpíšte: $(\mathbf{CD})^{\top} = \mathbf{D}^{\top}\mathbf{C}^{\top}$.
3. Pri stope súčinu počítajte len diagonálu.
4. Pri „nájdite len riadok/stĺpec“ násobte iba príslušný riadok/stĺpec.

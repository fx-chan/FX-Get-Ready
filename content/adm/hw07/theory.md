## LU rozklad / LU-разложение

Štvorcovú maticu rozložíme na súčin **dolnej** a **hornej** trojuholníkovej matice $\mathbf{A} = \mathbf{LU}$.
$\mathbf{U}$ je výsledok Gaussovej eliminácie (bez výmen riadkov), $\mathbf{L}$ zaznamenáva použité multiplikátory.

| metóda | $\mathbf{L}$ | $\mathbf{U}$ |
|---|---|---|
| **Doolittle** | jednotky na diagonále, pod ňou multiplikátory $\ell_{ij}$ | výsledok eliminácie |
| **Crout** | na diagonále pivoty | jednotky na diagonále |

Ak pri eliminácii robíme $R_i \to R_i - \ell_{ij}R_j$, potom v Doolittlovej $\mathbf{L}$ je na pozícii $(i, j)$ práve $\ell_{ij}$:

$$\begin{bmatrix}2&1\\6&8\end{bmatrix} \xrightarrow{R_2 - 3R_1} \begin{bmatrix}2&1\\0&5\end{bmatrix}
\;\Rightarrow\; \mathbf{L} = \begin{bmatrix}1&0\\3&1\end{bmatrix},\ \mathbf{U} = \begin{bmatrix}2&1\\0&5\end{bmatrix}$$

Crout dostaneme z Doolittla presunutím diagonály: $\mathbf{L}_C = \mathbf{L}\mathbf{D}$, $\mathbf{U}_C = \mathbf{D}^{-1}\mathbf{U}$,
kde $\mathbf{D}$ je diagonála $\mathbf{U}$.

::: drill d7-lu

> Ak sa počas eliminácie objaví na pozícii pivota **0** (napr. matica s $a_{11} = 0$), LU rozklad bez výmeny riadkov
> neexistuje — treba permutáciu $\mathbf{PA} = \mathbf{LU}$. Sústavu však vyriešite stále.

## Využitie LU rozkladu / Применение

**Sústava** $\mathbf{Ax} = \mathbf{b}$ ↔ $\mathbf{LUx} = \mathbf{b}$:
1. označíme $\mathbf{y} = \mathbf{Ux}$,
2. vyriešime $\mathbf{Ly} = \mathbf{b}$ **dopredným dosadením** (zhora nadol),
3. vyriešime $\mathbf{Ux} = \mathbf{y}$ **spätným dosadením** (zdola nahor).

Výhoda: pri mnohých pravých stranách sa rozklad počíta len raz.

- **Inverzia:** $\mathbf{A}^{-1} = (\mathbf{LU})^{-1} = \mathbf{U}^{-1}\mathbf{L}^{-1}$.
- **Determinant:** $\det\mathbf{A} = \det\mathbf{L}\cdot\det\mathbf{U}$ = súčin diagonál; pri Doolittlovi $\det\mathbf{L} = 1$.

::: quiz
Doolittlov rozklad má $\mathbf{U}$ s diagonálou $2, -3, 4$. Aký je $\det\mathbf{A}$?
- [ ] 3
- [x] $-24$
- [ ] 24
> $\det\mathbf{L} = 1$ (jednotky na diagonále), $\det\mathbf{U} = 2\cdot(-3)\cdot4 = -24$.
:::

## Vlastné čísla a vlastné vektory / Собственные числа и векторы

Nenulový vektor $\mathbf{x}$ je **vlastný vektor** štvorcovej matice $\mathbf{A}$, ak
$$\mathbf{Ax} = \lambda\mathbf{x}$$
pre nejaké číslo $\lambda$ — **vlastné číslo**. Transformácia smer $\mathbf{x}$ nemení, len ho natiahne/skráti
(alebo obráti pri $\lambda < 0$). Nulový vektor vlastným vektorom nie je.

::: drill d7-vlastny-vektor

**Charakteristický polynóm** a rovnica:
$$p(\lambda) = \det(\lambda\mathbf{I} - \mathbf{A}) = 0$$
Korene sú vlastné čísla. Pre $2\times2$: $p(\lambda) = \lambda^2 - \operatorname{tr}(\mathbf{A})\,\lambda + \det\mathbf{A}$.
Všeobecne: **súčet** vlastných čísel = $\operatorname{tr}\mathbf{A}$, **súčin** = $\det\mathbf{A}$.

::: drill d7-charakteristicky

::: quiz
Má matica $\begin{bmatrix}1&2\\-2&-1\end{bmatrix}$ reálne vlastné čísla?
- [ ] áno, $\pm 1$
- [x] nie, $p(\lambda) = \lambda^2 + 3$, vlastné čísla sú $\pm i\sqrt3$
- [ ] áno, $0$ a $0$
> $\operatorname{tr} = 0$, $\det = -1 + 4 = 3$, teda $\lambda^2 + 3 = 0$.
:::

**Vlastný priestor** pre $\lambda$ = všetky riešenia $(\lambda\mathbf{I} - \mathbf{A})\mathbf{x} = \mathbf{0}$ (homogénna sústava, DÚ 02).
Jeho **báza** sú nezávislé vlastné vektory, dimenzia = $n - \operatorname{hodnosť}(\lambda\mathbf{I} - \mathbf{A})$
(**geometrická násobnosť**). **Algebraická násobnosť** = násobnosť koreňa v $p(\lambda)$. Platí
$1 \le$ geometrická $\le$ algebraická.

::: drill d7-vlastny-priestor

**Bez počítania:**
- trojuholníková / diagonálna matica: vlastné čísla sú **prvky diagonály**,
- $\lambda = 0$ je vlastné číslo $\iff$ $\det\mathbf{A} = 0$ ($\mathbf{A}$ singulárna),
- $\mathbf{A}^k$ má vlastné čísla $\lambda^k$, $\mathbf{A}^{-1}$ má $\frac1\lambda$, $\mathbf{A} - s\mathbf{I}$ má $\lambda - s$ (s tými istými vektormi),
- geometrické transformácie: reflexia $\{1, -1\}$, projekcia $\{1, 0\}$, dilatácia $k$ $\{k, k\}$, rotácia o $\theta \ne 0, \pi$ v $\mathbb{R}^2$ nemá reálne vlastné čísla.

::: quiz
Aké vlastné čísla má ortogonálna projekcia na os $x$ v $\mathbb{R}^2$?
- [ ] len 1
- [x] 1 (vektory na osi $x$) a 0 (vektory na osi $y$)
- [ ] $1$ a $-1$
> Vektor na osi $x$ sa nezmení ($\lambda = 1$), vektor na osi $y$ sa zobrazí na nulu ($\lambda = 0$).
:::

## Podobnosť matíc / Подобие матриц

$\mathbf{B}$ je **podobná** $\mathbf{A}$, ak $\mathbf{B} = \mathbf{P}^{-1}\mathbf{AP}$ pre nejakú invertibilnú $\mathbf{P}$.
Podobné matice majú rovnaký **determinant, stopu, hodnosť, charakteristický polynóm a vlastné čísla**
(vlastné vektory sa môžu líšiť). Ak sa niektorý invariant líši, matice podobné nie sú. Rovnosť všetkých invariantov
však podobnosť ešte nezaručuje.

::: quiz
$\det\mathbf{A} = -1$ a $\det\mathbf{B} = -2$. Môžu byť $\mathbf{A}$ a $\mathbf{B}$ podobné?
- [x] nie, podobné matice majú rovnaký determinant
- [ ] áno, ak majú rovnakú stopu
- [ ] nedá sa rozhodnúť
> $\det(\mathbf{P}^{-1}\mathbf{AP}) = \det\mathbf{P}^{-1}\det\mathbf{A}\det\mathbf{P} = \det\mathbf{A}$.
:::

## Diagonalizácia / Диагонализация

$\mathbf{A}$ ($n\times n$) je **diagonalizovateľná**, ak je podobná diagonálnej matici:
$$\mathbf{P}^{-1}\mathbf{AP} = \mathbf{D} = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$$
To platí **práve vtedy**, keď má $\mathbf{A}$ $n$ lineárne nezávislých vlastných vektorov — tie tvoria stĺpce $\mathbf{P}$
(v rovnakom poradí ako vlastné čísla v $\mathbf{D}$).

Postup: 1) vlastné čísla, 2) pre každé $\lambda$ báza vlastného priestoru, 3) ak je spolu $n$ vektorov →
$\mathbf{P}$, inak diagonalizovateľná **nie je**. Stačí: **$n$ rôznych vlastných čísel ⇒ diagonalizovateľná**.

::: drill d7-diagonalizacia

::: quiz
$\mathbf{A} = \begin{bmatrix}5&0&0\\1&5&0\\0&1&5\end{bmatrix}$ má vlastné číslo 5 s algebraickou násobnosťou 3. Hodnosť $5\mathbf{I} - \mathbf{A}$ je 2. Je $\mathbf{A}$ diagonalizovateľná?
- [ ] áno, je trojuholníková
- [x] nie, vlastný priestor má dimenziu $3 - 2 = 1 < 3$
- [ ] áno, má len jedno vlastné číslo
> Potrebovali by sme 3 nezávislé vlastné vektory, máme len 1.
:::

## Mocniny matice / Степени матрицы

Ak $\mathbf{A} = \mathbf{PDP}^{-1}$, potom
$$\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1},\qquad \mathbf{D}^k = \operatorname{diag}(\lambda_1^k, \dots, \lambda_n^k),$$
lebo $\mathbf{P}^{-1}\mathbf{P}$ sa medzi činiteľmi vykráti. Funguje aj pre záporné $k$ (ak $\lambda_i \ne 0$).
Ak $\mathbf{A}^2 = \mathbf{I}$ (vlastné čísla $\pm1$), tak párne mocniny sú $\mathbf{I}$ a nepárne $\mathbf{A}$.

::: quiz
Vlastné čísla $\mathbf{A}$ sú $1, -1, -1$ a $\mathbf{A}$ je diagonalizovateľná. Čomu sa rovná $\mathbf{A}^{100}$?
- [ ] $\mathbf{A}$
- [x] $\mathbf{I}$
- [ ] $-\mathbf{I}$
> $\mathbf{D}^{100} = \operatorname{diag}(1, 1, 1) = \mathbf{I}$, teda $\mathbf{A}^{100} = \mathbf{PIP}^{-1} = \mathbf{I}$.
:::

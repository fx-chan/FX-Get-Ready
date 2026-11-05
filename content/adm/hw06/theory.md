> Zdroj: Anton, Rorres, *Elementary Linear Algebra*, 11. vydanie, kapitoly 1.8, 4.9, 4.10, 4.11 a pri posune 10.9. Čísla viet sú z tejto knihy.

## Maticová (lineárna) transformácia

Matica $\mathbf{A}$ rozmeru $m\times n$ definuje zobrazenie $T_{\mathbf{A}}:\mathbb{R}^n \to \mathbb{R}^m$,
$T_{\mathbf{A}}(\mathbf{x}) = \mathbf{Ax}$. Ak $m = n$, hovoríme o **operátore** na $\mathbb{R}^n$.
Je **lineárna**: platí aditivita $T(\mathbf{u}+\mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ a homogenita $T(k\mathbf{u}) = kT(\mathbf{u})$; vždy $T(\mathbf{0}) = \mathbf{0}$ (veta 1.8.1). Naopak každá lineárna transformácia z $\mathbb{R}^n$ do $\mathbb{R}^m$ je maticová (vety 1.8.2 a 1.8.3).

**Štandardná matica** má v stĺpcoch obrazy bázových vektorov $\mathbf{e}_1 = (1,0,\dots)$, $\mathbf{e}_2 = (0,1,\dots)$, …:
$$[T] = \big[\,T(\mathbf{e}_1)\;\big|\;T(\mathbf{e}_2)\;\big|\;\cdots\;\big|\;T(\mathbf{e}_n)\,\big]$$
Zo zápisu $w_1 = 2x_1 - 3x_2 + x_3,\; w_2 = -x_1 + 2x_2 - 4x_3$ ju prečítame po riadkoch:
$[T] = \begin{bmatrix}2&-3&1\\-1&2&-4\end{bmatrix}$ (rozmer: počet výstupov × počet vstupov).

::: drill d6-standardna

::: quiz
$T(x_1, x_2) = (x_2, -x_1, x_1 + 3x_2, x_1 - x_2)$. Aký rozmer má štandardná matica?
- [ ] $2\times4$
- [x] $4\times2$
- [ ] $4\times4$
> 4 výstupné súradnice (riadky), 2 vstupné (stĺpce): $T:\mathbb{R}^2 \to \mathbb{R}^4$.
:::

## Reflexie a projekcie

| operátor v $\mathbb{R}^2$ | matica | obraz $(x, y)$ |
|---|---|---|
| reflexia podľa osi $x$ | $\begin{bmatrix}1&0\\0&-1\end{bmatrix}$ | $(x, -y)$ |
| reflexia podľa osi $y$ | $\begin{bmatrix}-1&0\\0&1\end{bmatrix}$ | $(-x, y)$ |
| reflexia podľa $y = x$ | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ | $(y, x)$ |
| projekcia na os $x$ | $\begin{bmatrix}1&0\\0&0\end{bmatrix}$ | $(x, 0)$ |
| projekcia na os $y$ | $\begin{bmatrix}0&0\\0&1\end{bmatrix}$ | $(0, y)$ |

**Priamka cez počiatok s uhlom $\theta$ od kladnej osi $x$:** projekcia $\mathbf{P}_\theta$ a reflexia $\mathbf{H}_\theta = 2\mathbf{P}_\theta - \mathbf{I}$:
$$\mathbf{P}_\theta = \begin{bmatrix}\cos^2\theta&\sin\theta\cos\theta\\\sin\theta\cos\theta&\sin^2\theta\end{bmatrix},\qquad \mathbf{H}_\theta = \begin{bmatrix}\cos2\theta&\sin2\theta\\\sin2\theta&-\cos2\theta\end{bmatrix}$$

V $\mathbb{R}^3$: reflexia podľa roviny $xy$ mení znamienko $z$ ($\operatorname{diag}(1,1,-1)$), podľa $xz$ mení $y$,
podľa $yz$ mení $x$. Projekcia na rovinu $xy$ vynuluje $z$ ($\operatorname{diag}(1,1,0)$) atď.

::: drill d6-reflexia

::: quiz
Obraz vektora $(1, -2, 4)$ pri ortogonálnej projekcii na rovinu $xz$ je
- [ ] $(1, -2, 0)$
- [x] $(1, 0, 4)$
- [ ] $(0, -2, 4)$
> Na rovine $xz$ ostávajú súradnice $x$ a $z$, kolmá zložka $y$ sa vynuluje.
:::

## Rotácie

V $\mathbb{R}^2$ o uhol $\theta$ okolo počiatku (kladný uhol = **proti** smeru hodinových ručičiek):
$$\mathbf{R}_\theta = \begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$$

| $\theta$ | $30^\circ$ | $45^\circ$ | $60^\circ$ | $90^\circ$ |
|---|---|---|---|---|
| $\cos\theta$ | $\frac{\sqrt3}{2}$ | $\frac{\sqrt2}{2}$ | $\frac12$ | 0 |
| $\sin\theta$ | $\frac12$ | $\frac{\sqrt2}{2}$ | $\frac{\sqrt3}{2}$ | 1 |

::: drill d6-rotacia

V $\mathbb{R}^3$ určuje znamienko uhla **pravidlo pravej ruky**. Okolo súradnicových osí (kladný uhol: proti smeru hodinových ručičiek pri pohľade **z kladnej
poloosi do počiatku**; „v smere hodinových ručičiek“ = uhol $-\theta$):

$$\mathbf{R}_x = \begin{bmatrix}1&0&0\\0&\cos\theta&-\sin\theta\\0&\sin\theta&\cos\theta\end{bmatrix},\quad
\mathbf{R}_y = \begin{bmatrix}\cos\theta&0&\sin\theta\\0&1&0\\-\sin\theta&0&\cos\theta\end{bmatrix},\quad
\mathbf{R}_z = \begin{bmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}$$

> Pozor na $\mathbf{R}_y$: znamienko $-\sin\theta$ je v **dolnom** riadku (cyklické poradie $z \to x$).
> Súradnica pozdĺž osi rotácie sa nemení.

::: quiz
Rotácia okolo osi $z$ o $90^\circ$ (proti smeru) zobrazí $(2, -3, 1)$ na
- [x] $(3, 2, 1)$
- [ ] $(-3, -2, 1)$
- [ ] $(2, 1, -3)$
> $x' = 0\cdot2 - 1\cdot(-3) = 3$, $y' = 1\cdot2 + 0 = 2$, $z' = 1$.
:::

## Dilatácie, kontrakcie, kompresie

- **kontrakcia** ($0 \le k < 1$) / **dilatácia** ($k > 1$): $\mathbf{x} \mapsto k\mathbf{x}$, matica $k\mathbf{I}$,
- **kompresia** ($0 \le k < 1$) / **expanzia** ($k > 1$) v smere jednej osi: násobí sa len jedna súradnica, napr. v smere osi $x$ $\begin{bmatrix}k&0\\0&1\end{bmatrix}$, v smere $y$ $\begin{bmatrix}1&0\\0&k\end{bmatrix}$,
- **sklz (shear)** v smere osi $x$: $\begin{bmatrix}1&k\\0&1\end{bmatrix}$, $(x, y) \mapsto (x + ky, y)$; v smere osi $y$: $\begin{bmatrix}1&0\\k&1\end{bmatrix}$, $(x, y) \mapsto (x, y + kx)$.

Tieto operátory sa v knihe porovnávajú podľa ich **účinku na jednotkový štvorec** s vrcholmi $(0,0), (1,0), (1,1), (0,1)$: obrazy $\mathbf{e}_1$ a $\mathbf{e}_2$ sú stĺpce matice, preto zo štvorca prečítame maticu aj naopak.

## Posun

Posun patrí do počítačovej grafiky (kapitola 10.9): **posun (translácia)** o vektor $\mathbf{t} = (a, b)$ pripočíta ku každému bodu ten istý vektor. Súradnice $n$ bodov zapíšeme do stĺpcov matice $\mathbf{P}$ a posun je **sčítanie matíc** $\mathbf{P}' = \mathbf{P} + \mathbf{T}$, kde každý stĺpec $\mathbf{T}$ je $\mathbf{t}$:
$$T(\mathbf{x}) = \mathbf{x} + \mathbf{t},\qquad x' = x + a,\quad y' = y + b$$

Posun **nie je lineárny**: pre $\mathbf{t} \ne \mathbf{0}$ je $T(\mathbf{0}) = \mathbf{t} \ne \mathbf{0}$, preto ho nemožno zapísať maticou $2\times2$.
Aby sa dal zapísať násobením matíc, použijeme **homogénne súradnice**: bod $(x, y)$ zapíšeme ako $(x, y, 1)$ a posun je súčin s maticou $3\times3$:
$$\begin{bmatrix}x'\\y'\\1\end{bmatrix} = \begin{bmatrix}1&0&a\\0&1&b\\0&0&1\end{bmatrix}\begin{bmatrix}x\\y\\1\end{bmatrix} = \begin{bmatrix}x+a\\y+b\\1\end{bmatrix}$$

Napríklad posun o $(3, -1)$ zobrazí bod $(2, 5)$ na $(5, 4)$.

- spätný posun: $\mathbf{T}(a, b)^{-1} = \mathbf{T}(-a, -b)$,
- dva posuny sa sčítajú a komutujú: $\mathbf{T}(a, b)\,\mathbf{T}(c, d) = \mathbf{T}(a + c, b + d)$,
- posun a rotácia vo všeobecnosti nekomutujú, záleží na poradí,
- v $\mathbb{R}^3$ je to rovnaké s maticou $4\times4$: $x' = x + a$, $y' = y + b$, $z' = z + c$.

::: quiz
Bod $(1, 2)$ sa posunie o $(4, -3)$ a výsledok ešte o $(-1, 1)$. Kde skončí?
- [x] $(4, 0)$
- [ ] $(5, -1)$
- [ ] $(3, 0)$
> Posuny sa sčítajú: celkový posun je $(3, -2)$ a $(1, 2) + (3, -2) = (4, 0)$.
:::

## Skladanie a komutatívnosť

Ak sa najprv vykoná $T_1$ a potom $T_2$, je to $T_2 \circ T_1$ a
$$[T_2 \circ T_1] = [T_2]\,[T_1]$$
— matica **neskoršej** transformácie stojí **vľavo**. Skladanie vo všeobecnosti **nie je komutatívne**
(rovnako ako násobenie matíc): napr. reflexia podľa $y = x$ a projekcia na os $x$ nekomutujú. Komutujú napr.
dve rotácie v rovine, ľubovoľný operátor s $k\mathbf{I}$, projekcie na osi $x$ a $y$ (súčin je nulový).

::: drill d6-skladanie

Z kapitoly 4.10: $T_B \circ T_A = T_{BA}$. Dve rotácie v rovine komutujú a sčítajú sa uhly: $\mathbf{R}_{\theta_2}\mathbf{R}_{\theta_1} = \mathbf{R}_{\theta_1 + \theta_2}$. Zloženie dvoch reflexií je rotácia: $\mathbf{H}_{\theta_2}\mathbf{H}_{\theta_1} = \mathbf{R}_{2(\theta_2 - \theta_1)}$.

::: quiz
Najprv rotácia o $15^\circ$, potom o $105^\circ$ a nakoniec o $60^\circ$ v smere hodinových ručičiek. Výsledok je
- [x] rotácia o $60^\circ$ proti smeru hodinových ručičiek
- [ ] rotácia o $180^\circ$
- [ ] rotácia o $-60^\circ$
> $15^\circ + 105^\circ - 60^\circ = 60^\circ$.
:::

## Jadro, obor hodnôt a inverzný operátor

- **jadro** $\ker(T_{\mathbf{A}})$ sú vektory, ktoré sa zobrazia na $\mathbf{0}$ (nulový priestor $\mathbf{A}$),
- **obor hodnôt** $R(T_{\mathbf{A}})$ sú všetky obrazy (stĺpcový priestor $\mathbf{A}$),
- $T_{\mathbf{A}}$ je **prostá (one-to-one)**, ak rôzne vektory majú rôzne obrazy.

Pre štvorcovú $\mathbf{A}$ sú ekvivalentné (veta 4.10.1): $\mathbf{A}$ je invertibilná, $\ker(T_{\mathbf{A}}) = \{\mathbf{0}\}$, obor hodnôt je $\mathbb{R}^n$, $T_{\mathbf{A}}$ je prostá. Inverzný operátor je $T_{\mathbf{A}}^{-1} = T_{\mathbf{A}^{-1}}$.

::: quiz
Je ortogonálna projekcia invertibilný operátor?
- [ ] áno, inverzia je tá istá projekcia
- [x] nie — rôzne vektory majú rovnaký obraz, $\det = 0$
- [ ] áno, ak je to projekcia na rovinu
> Napr. $(1, 5)$ aj $(1, -2)$ sa premietnu na $(1, 0)$; informácia o $y$ sa stratí.
:::

## Geometria operátorov v rovine

Operátor s invertibilnou maticou zobrazí priamku na priamku, priamku cez počiatok na priamku cez počiatok, rovnobežky na rovnobežky a úsečku na úsečku (veta 4.11.1).

Každá elementárna matica $2\times2$ je sklz, reflexia podľa $y = x$, kompresia alebo expanzia pozdĺž osi, reflexia podľa osi, alebo kompresia či expanzia nasledovaná reflexiou (veta 4.11.2).
Keďže invertibilná matica je súčinom elementárnych matíc, **každý invertibilný operátor v rovine je postupnosťou sklzov, kompresií, expanzií a reflexií** (veta 4.11.3).

Postup: maticu upravíte na $\mathbf{I}$, zapíšete ako súčin elementárnych matíc a každú pomenujete. Matica vpravo sa vykoná prvá.

::: quiz
Čo robí matica $\begin{bmatrix}1&0\\3&1\end{bmatrix}$?
- [x] sklz v smere osi $y$ s faktorom 3
- [ ] sklz v smere osi $x$ s faktorom 3
- [ ] expanziu v smere osi $y$
> $(x, y) \mapsto (x, y + 3x)$: mení sa len druhá súradnica, úmerne prvej.
:::

### Príklad 1

Matice krokov: $\mathbf{M}_1$ je reflexia podľa $y = 2x$ s lineárnou časťou $\frac15\begin{bmatrix}-3&4\\4&3\end{bmatrix}$,
$\mathbf{M}_2$ je posunutie, $\mathbf{M}_3 = \mathbf{T}(1,2)\,\mathbf{R}_{90}\,\mathbf{T}(-1,-2)$. Poradie súčinu je $\mathbf{M} = \mathbf{M}_3\mathbf{M}_2\mathbf{M}_1$:
$$\mathbf{M} = \begin{bmatrix}- \frac{4}{5} & - \frac{3}{5} & 4 \\ - \frac{3}{5} & \frac{4}{5} & 4 \\ 0 & 0 & 1\end{bmatrix}$$
Obraz $P$ je $(3, 2)$. Bod idúci do počiatku dostaneme z $\mathbf{M}^{-1}$: $\left(\frac{28}{5}, -\frac45\right)$.

Lineárna časť má $\det = -1$, takže ide o reflexiu alebo kĺzavú reflexiu. Výpočet dáva
$\mathbf{M}^2 = \mathbf{T}\left(-\frac85, \frac{24}{5}\right) \ne \mathbf{I}$, teda **kĺzavá reflexia** s vektorom $\left(-\frac45, \frac{12}{5}\right)$.
Stred úsečky medzi bodom a jeho obrazom leží na osi: pre $P$ je to $\left(\frac52, \frac12\right)$. Smer osi je $(-1, 3)$, preto $3x + y = 8$.

### Príklad 2

$\mathbf{A} - 2\mathbf{I} = \mathbf{u}\mathbf{u}^{\top}$ s $\mathbf{u} = (1,1,1)$ má hodnosť 1 (každý prvok je 1).
Preto je $\lambda = 2$ dvojnásobné a tretie číslo je $2 + \mathbf{u}^{\top}\mathbf{u} = 5$. Báza pre 2: riešenia $x_1 + x_2 + x_3 = 0$, napr. $(1,-1,0)$, $(1,0,-1)$. Pre 5: $(1,1,1)$.
Matica je symetrická, preto diagonalizovateľná, napr. $\mathbf{P} = \begin{bmatrix}1&1&1\\1&-1&0\\1&0&-1\end{bmatrix}$.

Označme $\mathbf{N} = \mathbf{A} - 2\mathbf{I}$. Platí $\mathbf{N}^2 = 3\mathbf{N}$, a preto $\mathbf{A}^n = 2^n\mathbf{I} + \frac{5^n - 2^n}{3}\mathbf{N}$. Keďže $\mathbf{N}_{13} = 1$, je $(\mathbf{A}^n)_{13} = \frac{5^n - 2^n}{3}$.

Iterácie: $\mathbf{A}\mathbf{x}_0 = (3,1,1)$, $\mathbf{x}_1 = \left(1, \frac13, \frac13\right)$; $\mathbf{A}\mathbf{x}_1 = \left(\frac{11}{3}, \frac73, \frac73\right)$, $\mathbf{x}_2 = \left(1, \frac{7}{11}, \frac{7}{11}\right)$.
Rayleighov podiel z $\mathbf{x}_2$ je $\frac{1063}{219} \approx 4.854$. Pri euklidovskom škálovaní je $\mathbf{x}_1 = \frac{1}{\sqrt{11}}(3,1,1)$ a $\lambda^{(1)} = \frac{47}{11}$.
Vektor $(1,-1,0)$ je kolmý na $(1,1,1)$ a je vlastný k číslu 2, takže metóda nikdy nepríde k číslu 5.

### Príklad 3

$\mathbf{B}$: po preusporiadaní rovnakých indexov riadkov a stĺpcov (znamienko sa nezmení) sa rozpadne na bloky s indexmi $\{1,4,7\}$, $\{2,6\}$, $\{3,5\}$ s determinantmi $2$, $-5$, $1$. Teda $\det\mathbf{B} = -10$.
Posledný riadok má jediný prvok $b_{77} = 2$, preto $\det\mathbf{B} = 2C_{77}$ a $C_{77} = -5$.
$\det(2\mathbf{B}^{-1}\mathbf{B}^{\top}) = 2^7\cdot\frac{\det\mathbf{B}}{\det\mathbf{B}} = 128$. Pre $n = 7$ platí $\det(\operatorname{adj}\mathbf{B}) = (\det\mathbf{B})^{6} = 10^6$.

$\mathbf{C}(x)$: 5. stĺpec po rozvoji cez riadok 5 dá faktor 3, riadky a stĺpce $\{1,3\}$ dajú $x^2 - 1$, zvyšok $\{2,4,6,7\}$ dá $-(1 - x^2)$. Spolu $3(x^2-1)^2$, korene $x = \pm 1$.

### Príklad 4

Postup z knihy: $\frac12 R_1$, $R_2 - 4R_1$, $R_3 + 2R_1$, $\frac13 R_2$, $R_3 - 4R_2$, $\frac12 R_3$. Prevrátené hodnoty násobiteľov idú na diagonálu $\mathbf{L}$, opačné čísla pod ňu:
$$\mathbf{L} = \begin{bmatrix}2 & 0 & 0 \\ 4 & 3 & 0 \\ -2 & 4 & 2\end{bmatrix},\quad \mathbf{U} = \begin{bmatrix}1 & \frac{1}{2} & - \frac{1}{2} \\ 0 & 1 & 1 \\ 0 & 0 & 1\end{bmatrix}$$
Dopredne $\mathbf{y} = \begin{bmatrix}\frac{3}{2} & \frac{7}{3} & \frac{7}{3}\end{bmatrix}^{\top}$, spätne $\mathbf{x} = \left(\frac83, 0, \frac73\right)$. Pravá strana $\mathbf{e}_3$ dá 3. stĺpec inverzie $\left(\frac12, -\frac12, \frac12\right)$.
Doolittle: diagonálu presunieme do hornej matice, $\mathbf{L}' = \begin{bmatrix}1 & 0 & 0 \\ 2 & 1 & 0 \\ -1 & \frac{4}{3} & 1\end{bmatrix}$.

Pre $\mathbf{D}(t)$ po prvom kroku vznikne druhý pivot $t - 2$, preto pri $t = 2$ rozklad bez výmeny neexistuje, hoci $\det\mathbf{D}(2) = -24 \ne 0$.
$\det\mathbf{D}(t) = 2(t-5)(t+2)$, singulárna je pre $t \in \{5, -2\}$. Sústavu pre $t = 2$ vyriešime výmenou riadkov 2 a 3.

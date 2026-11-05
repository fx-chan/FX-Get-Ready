> Zdroj: Anton, Rorres, *Elementary Linear Algebra*, 11. vydanie, kapitoly 4.9–4.11, 5.1, 5.2, 2.1–2.3, 9.1, 9.2 a 10.9.

## Čo bude na písomke

**4 príklady, 1 h 40 min.** Plán na 100 minút: približne 25 minút na príklad a 5 minút na záverečnú kontrolu.

| príklad | téma | kľúčová zručnosť |
|---|---|---|
| 1 | 2D transformácie, zloženie troch | matice $3\times3$, správne poradie súčinu |
| 2 | vlastné čísla, diagonalizácia, mocninová metóda | $\det(\lambda\mathbf{I} - \mathbf{A}) = 0$, dve iterácie |
| 3 | determinant $7\times7$ s veľa nulami | rozvoj podľa riedkych riadkov, bloky |
| 4 | LU rozklad, pravdepodobne $3\times3$ | $\mathbf{Ly} = \mathbf{b}$, potom $\mathbf{Ux} = \mathbf{y}$ |

## Homogénne súradnice

Rotácia, reflexia a škálovanie sú lineárne: $\mathbf{x} \mapsto \mathbf{Lx}$. **Posun (posunutie) o $(a, b)$** je $x' = x + a$, $y' = y + b$ a lineárny nie je, lebo posúva aj počiatok.
Riešenie: bod $(x, y)$ zapíšeme ako $(x, y, 1)$ a každé zobrazenie $\mathbf{x} \mapsto \mathbf{Lx} + \mathbf{t}$ ako maticu $3\times3$:

$$\begin{bmatrix}\mathbf{L}&\mathbf{t}\\\mathbf{0}&1\end{bmatrix},\qquad
\mathbf{T}(a, b) = \begin{bmatrix}1&0&a\\0&1&b\\0&0&1\end{bmatrix},\qquad
\mathbf{R}_\theta = \begin{bmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{bmatrix}$$

Teraz je posunutie obyčajný súčin matíc, a preto sa dá skladať s ostatnými zobrazeniami. Kniha v kapitole 10.9 zapisuje posun aj ako sčítanie $\mathbf{P}' = \mathbf{P} + \mathbf{T}$; násobením je to jej cvičenie 7.

::: drill d8-homogenne

**Poradie:** najprv $T_1$, potom $T_2$, potom $T_3$ znamená $\mathbf{M} = \mathbf{M}_3\mathbf{M}_2\mathbf{M}_1$. Matica, ktorá sa vykoná **prvá, stojí vpravo**.

::: quiz
Bod sa najprv posunie a potom otočí. Ktorý súčin je správny?
- [ ] $\mathbf{T}\mathbf{R}$
- [x] $\mathbf{R}\mathbf{T}$
- [ ] je to jedno
> Na vektor pôsobí najprv matica najbližšie k nemu: $\mathbf{R}(\mathbf{T}\mathbf{x})$. Posunutie a rotácia vo všeobecnosti nekomutujú.
:::

### Transformácie okolo iného bodu a podľa inej priamky

Vzor je vždy rovnaký: **presuň do počiatku, urob to, vráť späť.**

- rotácia okolo bodu $\mathbf{c}$: $\mathbf{T}(\mathbf{c})\,\mathbf{R}_\theta\,\mathbf{T}(-\mathbf{c})$,
- škálovanie so stredom v $\mathbf{c}$: $\mathbf{T}(\mathbf{c})\,\mathbf{S}\,\mathbf{T}(-\mathbf{c})$,
- reflexia podľa priamky, ktorá neprechádza počiatkom: posuňte ľubovoľný jej bod do počiatku, zrkadlite, posuňte späť.

Reflexia podľa priamky cez počiatok s uhlom $\theta$ je $\mathbf{H}_\theta$ z kapitoly 4.9; so smerovým vektorom $(a, b)$:
$$\mathbf{H} = \frac{1}{a^2 + b^2}\begin{bmatrix}a^2 - b^2&2ab\\2ab&b^2 - a^2\end{bmatrix}$$
Pre priamku $y = 2x$ je smer $(1, 2)$ a $\mathbf{H} = \frac15\begin{bmatrix}-3&4\\4&3\end{bmatrix}$.

::: drill d8-rotacia-bod

### Čo zložené zobrazenie naozaj robí

Pre izometriu $\mathbf{x} \mapsto \mathbf{Lx} + \mathbf{t}$ stačí pozrieť na $\det\mathbf{L}$:

| $\det\mathbf{L}$ | zobrazenie | test |
|---|---|---|
| $1$, $\mathbf{L} = \mathbf{I}$ | posunutie | žiadny pevný bod |
| $1$, $\mathbf{L} \ne \mathbf{I}$ | rotácia | jediný pevný bod: $(\mathbf{I} - \mathbf{L})\mathbf{p} = \mathbf{t}$ |
| $-1$ | reflexia | $\mathbf{M}^2 = \mathbf{I}$ |
| $-1$ | kĺzavá reflexia | $\mathbf{M}^2$ je posunutie o dvojnásobok kĺzavého vektora |

Stred úsečky medzi bodom a jeho obrazom leží pri reflexii aj kĺzavej reflexii **na osi**. Obsah útvaru sa násobí číslom $|\det\mathbf{L}|$.

::: quiz
Dve reflexie podľa rovnobežných priamok vo vzdialenosti $d$ dajú
- [ ] rotáciu o $180^\circ$
- [x] posunutie o $2d$
- [ ] reflexiu
> $\det\mathbf{L} = (-1)(-1) = 1$ a lineárna časť je $\mathbf{I}$, takže ide o posunutie.
:::

## Vlastné čísla: skratky

Postup z DÚ 07 platí: $p(\lambda) = \det(\lambda\mathbf{I} - \mathbf{A})$, vlastné čísla, báza pre každé $\lambda$, potom $\mathbf{P}$. Na ťažkých zadaniach pomôžu skratky:

- **kontrola:** súčet vlastných čísel $= \operatorname{tr}\mathbf{A}$, súčin $= \det\mathbf{A}$,
- **rovnaké súčty v riadkoch:** ak má každý riadok súčet $s$, tak $(1, 1, \dots, 1)$ je vlastný vektor k číslu $s$,
- **hodnosť 1:** ak $\mathbf{A} - c\mathbf{I} = \mathbf{u}\mathbf{w}^{\top}$, vlastné čísla sú $c$ ($n-1$ krát) a $c + \mathbf{w}^{\top}\mathbf{u}$,
- **mocniny:** $\mathbf{A}^k = \mathbf{P}\mathbf{D}^k\mathbf{P}^{-1}$; pri $\mathbf{N} = \mathbf{u}\mathbf{w}^{\top}$ platí $\mathbf{N}^2 = (\mathbf{w}^{\top}\mathbf{u})\mathbf{N}$.

::: quiz
Každý riadok matice $3\times3$ má súčet 7. Čo vieme bez počítania?
- [x] 7 je vlastné číslo s vektorom $(1, 1, 1)$
- [ ] $\det\mathbf{A} = 7$
- [ ] $\operatorname{tr}\mathbf{A} = 7$
> $\mathbf{A}(1,1,1)^{\top}$ je vektor súčtov riadkov, teda $7\cdot(1,1,1)^{\top}$.
:::

## Mocninová metóda

Hľadá **dominantné** vlastné číslo, teda číslo s najväčšou absolútnou hodnotou, bez riešenia charakteristickej rovnice.

Prečo funguje: ak $\mathbf{x}_0 = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \dots$, potom
$$\mathbf{A}^k\mathbf{x}_0 = \lambda_1^k\left(c_1\mathbf{v}_1 + c_2\left(\frac{\lambda_2}{\lambda_1}\right)^k\mathbf{v}_2 + \dots\right)$$
a členy s $|\lambda_i / \lambda_1| < 1$ zmiznú. Rýchlosť určuje podiel $|\lambda_2 / \lambda_1|$.

Kniha (kapitola 9.2) opisuje dve varianty. Vety 9.2.1 a 9.2.2 hovoria o **symetrickej** matici s kladným dominantným číslom a štarte, ktorý nie je kolmý na príslušný vlastný priestor.

**S euklidovským škálovaním:** $\mathbf{x}_0$ je jednotkový vektor,
$$\mathbf{x}_k = \frac{\mathbf{A}\mathbf{x}_{k-1}}{\lVert\mathbf{A}\mathbf{x}_{k-1}\rVert},\qquad \lambda^{(k)} = \mathbf{A}\mathbf{x}_k\cdot\mathbf{x}_k$$

**S maximálnym škálovaním:** $\max(\mathbf{x})$ je najväčšia **absolútna hodnota** zložky (bez znamienka), $\mathbf{x}_0$ je ľubovoľný nenulový vektor,
$$\mathbf{x}_k = \frac{\mathbf{A}\mathbf{x}_{k-1}}{\max(\mathbf{A}\mathbf{x}_{k-1})},\qquad \lambda^{(k)} = \frac{\mathbf{A}\mathbf{x}_k\cdot\mathbf{x}_k}{\mathbf{x}_k\cdot\mathbf{x}_k}$$

Výraz $\frac{\mathbf{Ax}\cdot\mathbf{x}}{\mathbf{x}\cdot\mathbf{x}}$ je **Rayleighov podiel**. Nezávisí od násobku vektora, preto obe varianty dávajú rovnaké odhady $\lambda^{(k)}$, ak štartujú z rovnakého smeru. Prvá vedie k jednotkovému vlastnému vektoru, druhá k vektoru s najväčšou zložkou 1.

$$\mathbf{A} = \begin{bmatrix}4&1\\1&4\end{bmatrix},\ \mathbf{x}_0 = \begin{bmatrix}1\\0\end{bmatrix}:\quad
\mathbf{A}\mathbf{x}_0 = \begin{bmatrix}4\\1\end{bmatrix},\ \mathbf{x}_1 = \begin{bmatrix}1\\\frac14\end{bmatrix},\quad
\mathbf{A}\mathbf{x}_1 = \begin{bmatrix}\frac{17}{4}\\2\end{bmatrix},\ \mathbf{x}_2 = \begin{bmatrix}1\\\frac{8}{17}\end{bmatrix}$$

::: drill d8-mocninova

**Kedy metóda zlyhá:** dve čísla s rovnakou absolútnou hodnotou ($1$ a $-1$), komplexná dvojica, alebo $\mathbf{x}_0$ bez zložky v smere $\mathbf{v}_1$. Pri zápornom dominantnom čísle vektor v každom kroku mení znamienko, ale $\lambda^{(k)}$ konverguje správne (poznámka k vete 9.2.1).

::: quiz
Vlastné čísla sú $6$, $-3$, $1$. Približne koľkokrát sa zmenší chyba v jednej iterácii?
- [x] 2-krát
- [ ] 6-krát
- [ ] 3-krát
> $|\lambda_2/\lambda_1| = 3/6 = 1/2$. Druhé najväčšie číslo v absolútnej hodnote je $-3$.
:::

## Determinant 7×7

Rozpisovať $7! = 5040$ členov sa nedá. Stratégia:

1. **Hľadajte riadok alebo stĺpec s jediným nenulovým prvkom** a rozvíjajte. Rozmer klesne o 1, pozor na znamienko $(-1)^{i+j}$.
2. **Hľadajte skryté bloky:** ktoré riadky používajú len tie isté stĺpce? Ak pre skupinu indexov riadky aj stĺpce tvoria uzavretý blok, determinant je súčin determinantov blokov.
3. **Rovnaké preusporiadanie riadkov aj stĺpcov** znamienko nemení. Rôzne preusporiadanie: znamienko je súčin znamienok oboch permutácií.
4. **Vlastnosti:** $\det(k\mathbf{A}) = k^7\det\mathbf{A}$, $\det(\mathbf{A}^{\top}) = \det\mathbf{A}$, $\det(\operatorname{adj}\mathbf{A}) = (\det\mathbf{A})^{n-1}$.

$$\det\begin{bmatrix}1&0&2\\0&5&0\\3&0&4\end{bmatrix} = 5\cdot\begin{vmatrix}1&2\\3&4\end{vmatrix} = -10$$
Prostredný riadok a stĺpec tvoria blok, zvyšok druhý blok.

::: drill d8-det7

::: quiz
Aké znamienko má člen s prvkom na pozícii $(3, 6)$ pri rozvoji?
- [x] $-$
- [ ] $+$
> $(-1)^{3+6} = (-1)^9 = -1$.
:::

::: quiz
Matica $7\times7$ má jednotky len na vedľajšej diagonále. Aký je jej determinant?
- [ ] $1$
- [x] $-1$
- [ ] $0$
> Riadky treba preusporiadať $3$ výmenami (1↔7, 2↔6, 3↔5), znamienko je $(-1)^3$.
:::

## LU rozklad bez chýb

1. Upravte $\mathbf{A}$ na REF **bez výmeny riadkov**. Vedúce jednotky robia z $\mathbf{U}$ maticu s jednotkami na diagonále.
2. Do $\mathbf{L}$ zapisujte: na diagonálu prevrátenú hodnotu násobiteľa vedúcej jednotky, pod diagonálu opačné číslo k násobiteľu, ktorý vytvoril nulu.
3. $\mathbf{Ly} = \mathbf{b}$ zhora nadol, $\mathbf{Ux} = \mathbf{y}$ zdola nahor.
4. **Skúška:** $\mathbf{LU}$ dá $\mathbf{A}$, $\det\mathbf{A}$ = súčin diagonály $\mathbf{L}$.

V domácej úlohe sa tento tvar volá Crout. Doolittle má jednotky na diagonále $\mathbf{L}$ a dostanete ho presunutím diagonály do $\mathbf{U}$.

Jeden rozklad poslúži pre viac pravých strán: stĺpec $\mathbf{A}^{-1}$ dostanete z pravej strany $\mathbf{e}_j$.

**Nulový pivot neznamená singulárnu maticu.** Ak druhý pivot vyjde $t - 2$, rozklad bez výmeny pri $t = 2$ neexistuje, ale matica môže byť regulárna: stačí rozklad PLU, $\mathbf{PA} = \mathbf{LU}$. Singulárna je až vtedy, keď nulový ostane pivot po všetkých možných výmenách.

::: drill d8-lu

::: quiz
Pri $R_3 \to R_3 + 2R_1$, ktorá robí nulu na pozícii $(3, 1)$, je prvok $\mathbf{L}$ na tej pozícii
- [ ] $2$
- [x] $-2$
- [ ] $\frac12$
> Do $\mathbf{L}$ ide opačné číslo k násobiteľu 2. Znamienko je najčastejšia chyba.
:::

## Pred písomkou

Prejdite úlohy tohto bloku, potom si nastavte ticho a spustite písomku. Zadanie je zámerne ťažšie než ukážkové úlohy: niektoré časti treba odhaliť, nie len vypočítať. Po odovzdaní uvidíte body aj riešenie krok za krokom.

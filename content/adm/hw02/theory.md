## Lineárna rovnica a systém

**Lineárna rovnica** v neznámych $x_1, \dots, x_n$ má tvar $a_1x_1 + a_2x_2 + \dots + a_nx_n = b$, kde $a_i, b$ sú
konštanty. Neznáme sú len v **prvej mocnine**, nenásobia sa navzájom a nie sú v argumentoch funkcií.

| lineárne ✓ | nelineárne ✗ |
|---|---|
| $\pi x_1 - \sqrt2\,x_2 = 3^{1/3}$ — koeficienty môžu byť iracionálne | $x_1x_2 = 3$ — súčin neznámych |
| $\cos\frac{\pi}{7}\,x - 4y = \log 3$ — $\cos\frac{\pi}{7}$ je číslo | $\cos x - 4y = 0$ — neznáma vo funkcii |
| $y + 5 = 2x + 4^2$ — $4^2$ je konštanta | $x^{2/3}$, $x^{-2}$, $\sqrt{y}$, $\sqrt{x^2} = \lvert x\rvert$ |

::: drill d2-linearna

**Systém** $m$ lineárnych rovníc s $n$ neznámymi. **Riešenie** je $n$-tica čísel, ktorá spĺňa **všetky** rovnice naraz.
Systém je **konzistentný**, ak má aspoň jedno riešenie, inak **nekonzistentný**. Každý systém má buď

1. **žiadne** riešenie, 2. **práve jedno** riešenie, alebo 3. **nekonečne veľa** riešení — nič iné nie je možné.

::: quiz
Môže mať lineárny systém práve dve riešenia?
- [ ] áno, napr. kvadratická rovnica
- [x] nie — s dvoma riešeniami má nekonečne veľa
- [ ] áno, ak má dve rovnice
> Ak $\mathbf{X}_1, \mathbf{X}_2$ sú riešenia, tak aj $\mathbf{X}_1 + c(\mathbf{X}_2 - \mathbf{X}_1)$ pre každé $c$ (dôkaz je v A++ úlohe).
:::

## Augmentovaná matica

Systém zapíšeme maticovo $\mathbf{A}\mathbf{x} = \mathbf{b}$, kde $\mathbf{A}$ je **matica koeficientov** a $\mathbf{b}$
**stĺpec pravých strán**. **Augmentovaná (rozšírená) matica** je $[\mathbf{A}\,|\,\mathbf{b}]$:

$$\begin{aligned} 2x_1 + 2x_3 &= 1 \\ 3x_1 - x_2 + 4x_3 &= 7 \\ 6x_1 - x_2 - x_3 &= 0 \end{aligned}
\quad\longrightarrow\quad \left[\begin{array}{ccc|c} 2&0&2&1\\ 3&-1&4&7\\ 6&-1&-1&0 \end{array}\right]$$

Chýbajúca neznáma = koeficient **0**. Každý riadok je jedna rovnica, každý stĺpec (okrem posledného) jedna neznáma.

::: drill d2-augmentovana

## Elementárne riadkové operácie

Tieto operácie **nemenia množinu riešení**:

1. výmena dvoch riadkov $R_i \leftrightarrow R_j$,
2. vynásobenie riadku **nenulovým** číslom $R_i \to kR_i$, $k \ne 0$,
3. pripočítanie násobku iného riadku $R_i \to R_i + kR_j$.

> Tip na písomku: 1 v ľavom hornom rohu bez zlomkov často získate operáciou 3, napr. pre prvý stĺpec
> $-3, 2, 0$ dá $R_1 + 2R_2$ hodnotu $-3 + 4 = 1$.

::: quiz
Ktorá operácia **nie je** elementárna riadková operácia?
- [ ] $R_2 \to R_2 - 5R_1$
- [ ] $R_1 \leftrightarrow R_3$
- [x] $R_2 \to 0\cdot R_2$
- [ ] $R_3 \to \frac{1}{2}R_3$
> Násobiť riadok smieme len **nenulovým** číslom — násobenie nulou by stratilo rovnicu.
:::

## REF a RREF

**Riadkový echelonový tvar (REF):**
- nulové riadky sú na spodku,
- prvý nenulový prvok každého nenulového riadku je **1** (vedúca jednotka, pivot),
- vedúca jednotka nižšieho riadku je **vpravo** od vedúcej jednotky riadku nad ním.

**Redukovaný riadkový echelonový tvar (RREF):** REF a navyše každý stĺpec s vedúcou jednotkou má **všade inde nuly**.

$$\underbrace{\begin{bmatrix}1&5&-3\\0&1&1\\0&0&0\end{bmatrix}}_{\text{REF}}\qquad
\underbrace{\begin{bmatrix}1&0&3&1\\0&1&2&4\end{bmatrix}}_{\text{RREF}}\qquad
\underbrace{\begin{bmatrix}1&2&3\\0&0&0\\0&0&1\end{bmatrix}}_{\text{ani jedno: nulový riadok nie je dole}}$$

RREF danej matice je **jednoznačný**, REF nie.

::: quiz
Je $\begin{bmatrix}1&2&0\\0&1&0\\0&0&0\end{bmatrix}$ v RREF?
- [ ] áno
- [x] nie, len v REF — nad vedúcou jednotkou v 2. stĺpci je 2
- [ ] nie je ani v REF
> Na RREF treba $R_1 \to R_1 - 2R_2$.
:::

## Čítanie riešenia z RREF

- **Vedúce premenné** — stĺpce s vedúcou jednotkou; **voľné premenné** — ostatné stĺpce.
- Voľné premenné položíme rovné parametrom $t, s, \dots$ a vedúce z nich vyjadríme.
- Riadok $[0\;0\;\dots\;0 \,|\, c]$ s $c \ne 0$ znamená $0 = c$ → systém je **nekonzistentný**.

$$\left[\begin{array}{ccc|c}1&0&2&3\\0&1&-1&1\\0&0&0&0\end{array}\right] \Rightarrow
\begin{cases} x_1 = 3 - 2t \\ x_2 = 1 + t \\ x_3 = t \end{cases},\quad t \in \mathbb{R}$$

Počet parametrov = počet neznámych − počet vedúcich jednotiek (= hodnosť).

::: drill d2-rref

## Gaussova a Gauss-Jordanova eliminácia

1. **Priamy chod (Gauss):** stĺpec po stĺpci vytvoríme vedúcu jednotku a pod ňou nuly → **REF**.
2. Potom buď **spätné dosadenie** (od poslednej rovnice nahor), alebo
3. **spätný chod (Gauss-Jordan):** nuly aj **nad** vedúcimi jednotkami → **RREF**, riešenie sa len prečíta.

$$\left[\begin{array}{cc|c}1&1&1\\4&3&2\end{array}\right] \xrightarrow{R_2 - 4R_1}
\left[\begin{array}{cc|c}1&1&1\\0&-1&-2\end{array}\right] \xrightarrow{-R_2}
\left[\begin{array}{cc|c}1&1&1\\0&1&2\end{array}\right] \xrightarrow{R_1 - R_2}
\left[\begin{array}{cc|c}1&0&-1\\0&1&2\end{array}\right]$$

Riešenie: $x = -1$, $y = 2$.

::: drill d2-gauss

**Kritérium počtu riešení** (Frobeniova veta): nech $r = h(\mathbf{A})$ je hodnosť matice systému a $n$ počet neznámych.

| situácia | výsledok |
|---|---|
| $h(\mathbf{A}) < h([\mathbf{A}\,|\,\mathbf{b}])$ | žiadne riešenie |
| $h(\mathbf{A}) = h([\mathbf{A}\,|\,\mathbf{b}]) = n$ | práve jedno riešenie |
| $h(\mathbf{A}) = h([\mathbf{A}\,|\,\mathbf{b}]) < n$ | nekonečne veľa, $n - r$ parametrov |

::: quiz
Systém 3 rovníc s 5 neznámymi je konzistentný. Koľko má riešení?
- [ ] práve jedno
- [x] nekonečne veľa
- [ ] nedá sa povedať, môže mať aj jedno
> Hodnosť je najviac 3 < 5, preto zostanú aspoň 2 voľné premenné.
:::

## Homogénne systémy

Systém $\mathbf{A}\mathbf{x} = \mathbf{0}$ je **vždy konzistentný** — má **triviálne riešenie** $\mathbf{x} = \mathbf{0}$.
**Netriviálne** riešenie má práve vtedy, keď existuje voľná premenná, napr. vždy, keď je **viac neznámych než rovníc**.
Pre štvorcovú $\mathbf{A}$: netriviálne riešenie existuje práve vtedy, keď $\det\mathbf{A} = 0$.

::: drill d2-homogenny

::: quiz
Homogénny systém 4 rovníc so 4 neznámymi má po eliminácii 3 vedúce jednotky. Potom
- [ ] má len triviálne riešenie
- [x] má nekonečne veľa riešení (1 parameter)
- [ ] je nekonzistentný
> Homogénny systém nemôže byť nekonzistentný. 4 − 3 = 1 voľná premenná.
:::

## Systémy s parametrom a konštantami

- Pri parametri ($\alpha$) robíme elimináciu normálne; problém je, keď **pivot obsahuje parameter** a môže byť 0.
  Rozoberieme prípady: pivot $\ne 0$ → jedno riešenie; pivot $= 0$ → pozrieme pravú stranu (0 = 0 → nekonečne veľa,
  0 = nenulové → žiadne).
- Pri pravých stranách $a, b, c$ dostaneme po eliminácii riadok $[0\;0\;0 \,|\, \text{výraz v } a,b,c]$;
  **podmienka konzistentnosti** je výraz $= 0$.

$$\begin{aligned}x+3y-z&=a\\x+y+2z&=b\\2y-3z&=c\end{aligned}
\xrightarrow{R_2-R_1}\ -2y+3z = b-a \xrightarrow{+R_3}\ 0 = b - a + c \;\Rightarrow\; c = a - b$$

::: quiz
Po eliminácii dostaneme posledný riadok $[\,0\;\;0\;\;(\alpha-2)(\alpha+2) \,|\, \alpha - 2\,]$. Pre $\alpha = 2$ systém
- [ ] nemá riešenie
- [x] má nekonečne veľa riešení
- [ ] má práve jedno riešenie
> Pre $\alpha = 2$ je riadok $[0\;0\;0\,|\,0]$, rovnica zmizne a pribudne voľná premenná. Pre $\alpha = -2$ je $[0\;0\;0\,|\,-4]$ — žiadne riešenie.
:::

## Nelineárne systémy cez substitúciu

Ak sa neznáme vyskytujú len vo **výrazoch rovnakého tvaru** ($\sin\alpha$, $x^2$, $\frac1x$, …), zavedieme nové
neznáme ($u = \sin\alpha$, $X = x^2$, $u = \frac1x$), vyriešime lineárny systém a vrátime sa späť.
Pozor na počet riešení: $x^2 = 1$ dáva $x = \pm1$, $\sin\alpha = 0$ dáva na $[0, 2\pi]$ tri uhly $0, \pi, 2\pi$.

::: quiz
Po substitúcii $X = x^2, Y = y^2, Z = z^2$ vyjde $X = 1, Y = 3, Z = 2$. Koľko riešení $(x, y, z)$ má pôvodný systém?
- [ ] 1
- [ ] 3
- [x] 8
- [ ] 6
> Každá neznáma má 2 znamienka: $2\cdot2\cdot2 = 8$.
:::

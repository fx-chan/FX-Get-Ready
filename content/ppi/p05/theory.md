> Podľa 4. a 5. prednášky PPI: sekvenčné obvody, konečné automaty Mealy a Moore, synchrónne preklápacie obvody D, T, JK a SR.

## Sekvenčný obvod

Výstup **kombinačného** obvodu závisí len od aktuálneho vstupu. Výstup **sekvenčného** obvodu závisí aj od toho, čo sa na vstupe dialo predtým — od **stavu**. Preto musí mať sekvenčný obvod **pamäť**, ktorá stav uchováva.

Sekvenčné obvody sú **synchrónne** (stav sa mení len v okamihu hodinového impulzu, hrany signálu $C$) alebo **asynchrónne** (stav sa mení hneď, ako sa zmení vstup). Môžu mať pevnú alebo programovateľnú funkciu.

## Konečný automat

Správanie sekvenčného obvodu opisuje **konečný deterministický automat**
$$A = (X, S, Y, p, v, S_0)$$

- $X$ — množina vstupov (vstupných vektorov), $Y$ — množina výstupov, $S$ — konečná množina stavov, $S_0$ — začiatočný stav;
- $p: S \times X \to S$ — **prechodová funkcia** (do ktorého stavu sa automat dostane);
- $v$ — **výstupná funkcia**, podľa ktorej rozlišujeme dva typy:
  - **Mealy**: $v: S \times X \to Y$ — výstup závisí od stavu **aj vstupu**;
  - **Moore**: $v: S \to Y$ — výstup závisí **iba od stavu**.

### Zápis automatu

**Prechodová tabuľka** — riadky sú stavy, stĺpce vstupy. V Mealyho automate je v políčku nasledujúci stav **a** výstup, v Moorovom je výstup samostatný stĺpec pri stave.

Mealy, vstup $x$:

| stav | $x = 0$ | $x = 1$ |
|---|---|---|
| $s_1$ | $s_1$ / 0 | $s_2$ / 0 |
| $s_2$ | $s_1$ / 0 | $s_2$ / 1 |

Tento automat dá $y = 1$, keď prišli dve jednotky za sebou (pri každej ďalšej jednotke tiež).

**Prechodový graf** — stavy sú vrcholy, prechody orientované hrany. Na hrane Mealyho automatu je „vstup / výstup“, v Moorovom automate je výstup napísaný pri vrchole.

### Ako simulovať automat

Začnite v začiatočnom stave. Pre každý vstupný symbol si zapíšte výstup (Mealy: z políčka; Moore: zo stavu) a prejdite do nasledujúceho stavu. V Moorovom automate sa výstup v takte $t$ vzťahuje na stav, v ktorom automat **je**, teda na históriu **bez** aktuálneho vstupu.

**Moorov automat oneskoruje výstupné slovo o jeden takt** oproti Mealyho automatu, ktorý reaguje okamžite. Za to má Moore stabilnejší výstup (nemení sa so zmenou vstupu uprostred taktu) a zvyčajne viac stavov.

::: drill d5-simulacia

::: quiz
V automate typu Moore závisí výstup od
- [ ] stavu a vstupu
- [x] iba od stavu
- [ ] iba od vstupu
> $v: S \to Y$. Ak by závisel aj od vstupu, išlo by o Mealyho automat.
:::

## Preklápacie obvody

Pamäťová časť synchrónneho obvodu sa skladá z **preklápacích obvodov** (PO, flip-flop). PO má dva stavy (0 a 1) a dva výstupy $Q$ a $\overline{Q}$. Zmenu stavu spôsobí hodinový impulz $C$; vstupy určujú, akou zmenou.

Označme $Q$ súčasný stav a $Q^+$ stav po hodinovom impulze. Pri JK sa správanie opisuje štyrmi písmenami: **P** = pamätaj (stav sa nemení), **1** = nastav, **0** = nuluj, **K** = komplement (preklop).

| PO | vstupy | správanie | charakteristická rovnica |
|---|---|---|---|
| **D** (data, delay) | $D$ | $Q^+ = D$ | $Q^+ = D$ |
| **T** (toggle) | $T$ | $T = 0$: P, $T = 1$: K | $Q^+ = T \oplus Q$ |
| **JK** | $J, K$ | $00$: P, $10$: 1, $01$: 0, $11$: K | $Q^+ = J\overline{Q} + \overline{K}Q$ |
| **SR** (set, reset) | $S, R$ | $00$: P, $10$: 1, $01$: 0, $11$: **zakázané** | $Q^+ = S + \overline{R}Q$, $SR = 0$ |

PO-JK je **univerzálny**: obsahuje všetky typy správania (pamätanie, nastavenie, nulovanie aj preklopenie). Prakticky sa vyrába ako dvojčinný **master-slave** z dvoch asynchrónnych SR a logických členov. Synchrónny D sa dá postaviť z asynchrónneho SR obvodu.

Asynchrónny **SR** sa skladá z dvoch krížovo zapojených členov NOR (vstupy aktívne v 1). Z dvoch NAND vznikne $\overline{S}\,\overline{R}$ obvod, ktorého vstupy sú aktívne v 0.

::: drill d5-preklapacie

::: quiz
PO-JK je v stave $Q = 1$ a na vstupoch je $J = 1, K = 1$. Po hodinovom impulze je $Q^+ =$
- [x] 0
- [ ] 1
- [ ] nedefinované
> $JK = 11$ znamená komplement (K): stav sa preklopí.
:::

::: quiz
Ktorá kombinácia je zakázaná pri PO-SR?
- [ ] $S = 0, R = 0$
- [ ] $S = 1, R = 0$
- [x] $S = 1, R = 1$
> Obvod by mal naraz nastaviť aj nulovať; po uvoľnení vstupov nie je jasné, kde skončí.
:::

## Inverzná prechodová funkcia

Pri návrhu (lekcia 6) sa pýtame opačne: **aké vstupy treba dať PO, aby prešiel zo stavu $r$ do stavu $u$?** Odpoveď je **inverzná prechodová funkcia** $p^{-1}$. Znak **x** znamená, že na hodnote nezáleží.

| prechod $r \to u$ | D | T | J K | S R |
|---|---|---|---|---|
| $0 \to 0$ | 0 | 0 | 0 x | 0 x |
| $0 \to 1$ | 1 | 1 | 1 x | 1 0 |
| $1 \to 0$ | 0 | 1 | x 1 | 0 1 |
| $1 \to 1$ | 1 | 0 | x 0 | x 0 |

Prečo je pri JK prechode $0 \to 1$ hodnota $K$ ľubovoľná? Prechod zabezpečí aj „nastav“ ($JK = 10$), aj „preklop“ ($JK = 11$). Práve tieto x robia budiace funkcie JK obvodu často jednoduchšími.

::: drill d5-inverzna

::: quiz
PO-T má prejsť zo stavu 1 do stavu 1. Vstup $T$ musí byť
- [x] 0
- [ ] 1
- [ ] x
> Pri $T = 1$ by sa preklopil do 0.
:::

::: quiz
Pri PO-JK a prechode $1 \to 0$ je
- [ ] $J = 0, K = 1$
- [x] $J = $ x, $K = 1$
- [ ] $J = 1, K = $ x
> Prechod zabezpečí nulovanie ($JK = 01$) aj preklopenie ($JK = 11$), $J$ je ľubovoľné.
:::

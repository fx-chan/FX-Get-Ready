> Podľa 4.–6. prednášky PPI: syntéza synchrónnych sekvenčných obvodov (abstraktná a štruktúrna), kódovanie stavov, budiace funkcie pre PO-D a PO-JK, podmienky synchronizácie a asynchrónne sekvenčné obvody.

## Model synchrónneho sekvenčného obvodu

Synchrónny sekvenčný obvod (SSO) má dve časti:

- **pamäťovú P** — synchrónne preklápacie obvody, ich výstupy $Q_i$ tvoria zakódovaný stav;
- **kombinačnú K** — zo vstupov $x$ a stavu $Q$ počíta **budiace funkcie** (vstupy PO, napr. $D_i$ alebo $J_i, K_i$) a **výstupné funkcie** $y$.

Všetky PO dostávajú ten istý hodinový signál. Úlohou návrhu je navrhnúť K tak, aby spolu s P realizovala prechodovú aj výstupnú funkciu automatu. Kritériom optimálnosti môže byť najmenší počet PO, najmenší počet členov v K alebo najvyššia rýchlosť.

Návrh má dve etapy: **abstraktnú syntézu** (zo slovného opisu automat) a **štruktúrnu syntézu** (z automatu obvod).

## Abstraktná syntéza

Zo slovného opisu treba vytvoriť presný automat: navrhnúť **stavy**, **prechodovú funkciu** a **výstupnú funkciu**. Vstupy a výstupy sú zvyčajne dané. Je to tvorivá etapa — stav si treba predstaviť ako „čo si obvod musí pamätať o minulosti“.

**Príklad: detektor postupnosti 101** (Mealy, s prekrývaním — posledná 1 môže byť začiatkom ďalšej trojice). Obvod si pamätá, akú časť hľadanej postupnosti už videl:

| stav | význam | $x = 0$ | $x = 1$ |
|---|---|---|---|
| $A$ | nič užitočné | $A$ / 0 | $B$ / 0 |
| $B$ | videl som „1“ | $C$ / 0 | $B$ / 0 |
| $C$ | videl som „10“ | $A$ / 0 | $B$ / **1** |

**Príklad: kontrolór kódu** číslic 0 – 5 v trojbitovom kóde, ktorý prichádza sériovo od najvyššieho rádu. Platné slová sú 000 – 101, neplatné 110 a 111. Po každej trojici sa obvod vráti na začiatok. Stavy: začiatok, „prvý bit 0“, „prvý bit 1“, „prečítal som 0x“, „prečítal som 10“, „prečítal som 11“. Výstup $y = 1$ dá pri treťom bite, ak je trojica neplatná (po „11“ hocičo). Niektoré stavy sa dajú zlúčiť — po „0“ je už jasné, že slovo bude platné.

**Príklad: predajný automat**. Berie mince 1 € a 2 €, tovar stojí 3 €. Stavy podľa vhodenej sumy: 0 €, 1 €, 2 €, 3 €, 4 €. Zo stavov 3 € a 4 € automat vydá tovar (zo 4 € aj 1 € späť) a vráti sa do stavu 0 €.

::: drill d6-abstraktna

## Štruktúrna syntéza

1. **Kódovanie stavov** — každému stavu priradíme vektor stavových premenných. Pri $|S|$ stavoch potrebujeme aspoň
$$k = \lceil \log_2 |S| \rceil$$
preklápacích obvodov. Nepoužité kódy sú neurčené body (x) všetkých funkcií.
2. **Prechodová tabuľka v kódoch**: pre každý kód a vstup nasledujúci kód a výstup.
3. **Budiace funkcie**: pre každý PO zistíme z inverznej prechodovej funkcie (lekcia 5), aké vstupy potrebuje pri danom prechode, a zapíšeme ich do mapy.
4. **Výstupné funkcie**.
5. **Minimalizácia** (MDNF/MKNF, prípadne prevod na NAND alebo NOR) a nakreslenie obvodu.

### Zásady dobrého kódovania

Kód sa dá zvoliť ľubovoľne a obvod bude správny. Dobré kódovanie však vytvorí v mapách väčšie konfigurácie:

- **pravidlo 1**: stavy, ktoré majú pri **rovnakom vstupe rovnaký nasledujúci stav**, kódujeme **susedne** (kódy sa líšia v jednom bite);
- **pravidlo 2**: stavy, ktoré sú **nasledujúcimi stavmi toho istého stavu** (pri susedných vstupoch), kódujeme susedne.

### Príklad: detektor 101 s PO-D

Kódy $A = 00$, $B = 01$, $C = 10$ ($Q_1Q_0$), kód $11$ je nepoužitý. $A$ a $C$ majú pri $x = 0$ rovnaký nasledujúci stav $A$, preto sú susedné (pravidlo 1).

| $Q_1Q_0$ | $x = 0$ | $x = 1$ |
|---|---|---|
| 00 ($A$) | 00 / 0 | 01 / 0 |
| 01 ($B$) | 10 / 0 | 01 / 0 |
| 10 ($C$) | 00 / 0 | 01 / 1 |
| 11 | x | x |

Pri **PO-D** je budiaca funkcia rovno nasledujúci stav: $D_i = Q_i^+$. Z máp premenných $Q_1, Q_0, x$ (s využitím x):
$$D_1 = Q_0\overline{x}, \qquad D_0 = x, \qquad y = Q_1x$$

S **PO-JK** zapíšeme pre každý prechod hodnoty $J_i, K_i$ podľa inverznej tabuľky (0→0: 0x, 0→1: 1x, 1→0: x1, 1→1: x0). Vyjde
$$J_1 = Q_0\overline{x},\; K_1 = 1, \qquad J_0 = x,\; K_0 = \overline{x}$$
Vďaka mnohým x sú budiace funkcie JK často jednoduché, za cenu dvoch vstupov na každý PO.

::: drill d6-budenie

::: quiz
Automat má 6 stavov. Koľko PO potrebujeme aspoň?
- [ ] 2
- [x] 3
- [ ] 6
> $2^2 = 4 < 6 \le 8 = 2^3$.
:::

::: quiz
Pri PO-D je budiaca funkcia $D_i$ rovná
- [x] nasledujúcej hodnote stavovej premennej $Q_i^+$
- [ ] súčasnej hodnote $Q_i$
- [ ] negácii $Q_i^+$
> PO-D si v takte zapamätá to, čo je na vstupe: $Q^+ = D$.
:::

::: quiz
Stavy $s_1$ a $s_2$ prejdú pri $x = 1$ oba do $s_4$. Podľa pravidla 1 by mali mať kódy
- [x] susedné
- [ ] rovnaké
- [ ] negované
> Rovnaké kódy mať nesmú (sú to rôzne stavy); susedné kódy zväčšia konfigurácie v mapách.
:::

## Podmienky správnej synchronizácie

Synchrónny obvod funguje, len ak sa všetko stihne medzi dvoma hodinovými impulzmi:

- po hrane sa zmenia výstupy PO (oneskorenie $t_{PO}$), signál prejde kombinačnou časťou ($t_K$) a pred ďalšou hranou musí byť na vstupoch PO ustálený ešte aspoň predstih $t_{s}$. Preto perióda hodín $T \ge t_{PO} + t_K + t_{s}$;
- vonkajšie vstupy sa smú meniť len tak, aby boli pred hranou ustálené;
- PO musia reagovať na **hranu** (alebo byť dvojčinné master-slave), aby zmena stavu v tom istom takte nepreletela kombinačnou časťou znova do PO;
- všetky PO dostávajú hodiny v tom istom okamihu.

::: quiz
$t_{PO} = 4$ ns, $t_K = 11$ ns, $t_s = 5$ ns. Najvyššia frekvencia hodín je
- [ ] 100 MHz
- [x] 50 MHz
- [ ] 25 MHz
> $T \ge 20$ ns, teda $f \le 1/(20\text{ ns}) = 50$ MHz.
:::

## Asynchrónne sekvenčné obvody

Asynchrónny obvod nemá hodiny; stav sa mení hneď, ako sa zmení vstup. Pamäť tvoria spätné väzby (prípadne asynchrónne PO-SR). Správanie opisuje **fundamentálny automat**:

- stav $s$ je pri vstupe $x$ **stabilný**, ak $p(s, x) = s$ — obvod v ňom zotrvá ľubovoľne dlho;
- každý prechod **začína a končí v stabilnom stave** (cez prípadné nestabilné stavy);
- pracuje sa vo **fundamentálnom režime**: vstup sa smie zmeniť, len keď je obvod v stabilnom stave, a vždy sa mení **len jedna** vstupná premenná.

**Rád** fundamentálneho automatu je $r = k_{max} + 1$, kde $k_{max}$ je dĺžka najdlhšieho reťazca nestabilných stavov, cez ktoré prechod ide. Ak pri niektorom vstupe vznikne cyklus nestabilných stavov (automat by kmital, napr. $1 \to 2 \to 3 \to 1$), automat **nie je** fundamentálny.

### Kódovanie stavov — najdôležitejšia časť

Ak sa pri prechode musia zmeniť **dve stavové premenné naraz**, nikdy sa nezmenia presne v tej istej chvíli — vzniká **súbeh**. Súbeh je **kritický**, ak výsledný stabilný stav závisí od toho, ktorá premenná sa zmení skôr. Kritické súbehy treba odstrániť:

- **priamy kód** — kódy volíme tak, aby každý prechod menil len jednu stavovú premennú (stavy, medzi ktorými sa prechádza, sú susedné);
- **nepriamy kód** — ak to nejde, prechod vedieme cez **medzistavy** (nestabilné), pričom každý krok mení jednu premennú.

Ak sú tieto predpoklady splnené (fundamentálny automat, zmena jednej premennej naraz, kód bez kritických súbehov), postupy zo synchrónnych obvodov sa dajú použiť aj tu.

### Hazardy

- **statický hazard** — rôzne oneskorenie ciest v kombinačnej časti, výstup krátko „blikne“ (riešenie: bezhazardná NF z lekcie 4);
- **dynamický hazard** — pri jednej zmene výstup zmení hodnotu viackrát;
- **podstatný hazard** — zmena vnútorného stavu (spätná väzba) sa dostane k niektorému členu skôr než samotná zmena vstupu, ktorá ju spôsobila. Člen tak vidí nový stav so starým vstupom a obvod môže skončiť v nesprávnom stave. Nedá sa odstrániť úpravou výrazu, len oneskorením spätnej väzby.

::: drill d6-asynchronne

::: quiz
Pri prechode sa majú zmeniť stavové premenné $00 \to 11$ a podľa toho, ktorá sa zmení skôr, skončí obvod v rôznych stabilných stavoch. Ide o
- [ ] nekritický súbeh
- [x] kritický súbeh
- [ ] statický hazard
> Výsledok závisí od poradia zmien — súbeh je kritický. Pomôže priamy alebo nepriamy kód.
:::

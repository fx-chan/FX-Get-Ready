> Podľa prednášky PPI „Od sčítačky k procesoru“ (M. Janeba): z hradiel postavíme sčítačku, ALU, registre, zbernicu, riadiacu jednotku a nakoniec celý 4-bitový procesor.

## Multiplexor — obvod, ktorý sa rozhoduje

Z 4. lekcie: multiplexor pustí na výstup jeden zo vstupov podľa výberového signálu. MUX 2 → 1 sú dve brány AND, jeden OR a jeden invertor. Odteraz rozlišujeme dva druhy signálov:

- **údaje** — čísla, s ktorými sa počíta;
- **riadenie** — signály, ktoré hovoria, čo sa má s údajmi stať (výber v multiplexore, zápis do registra, operácia ALU).

Multiplexor nájdeme v ALU, na zbernici aj v riadení procesora. Demultiplexor je jeho zrkadlo: rovnaká kostra bez záverečného OR — multiplexor zlučuje, demultiplexor rozvetvuje.

## Sčítačka

**Polovičná sčítačka** sčíta dva bity $A$, $B$ a dá súčet $S$ a prenos $C$:
$$S = A \oplus B, \qquad C = AB$$

| $A$ | $B$ | $C$ | $S$ |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 0 |

„Polovičná“ preto, že nevie prijať prenos z nižšieho rádu.

**Úplná sčítačka** má tri vstupy $A$, $B$, $C_{in}$:
$$S = A \oplus B \oplus C_{in}, \qquad C_{out} = AB + C_{in}(A \oplus B)$$
$S$ je 1, keď je na vstupe **nepárny** počet jednotiek; $C_{out}$ je 1, keď sú na vstupe **aspoň dve** jednotky (je to funkcia majority, ako MDNF: $AB + AC_{in} + BC_{in}$). Postaví sa z dvoch polovičných sčítačiek a jedného OR: päť hradiel (2 × XOR, 2 × AND, OR).

::: drill d7-scitacka

::: quiz
Úplná sčítačka dostane $A = 1$, $B = 1$, $C_{in} = 1$. Výstupy $C_{out}$, $S$ sú
- [ ] 1, 0
- [x] 1, 1
- [ ] 0, 1
> $1 + 1 + 1 = 3 = 11_2$: tri jednotky sú nepárny počet ($S = 1$) aj aspoň dve ($C_{out} = 1$).
:::

### Viac bitov: sčítačka s postupným prenosom

$n$-bitovú sčítačku dostaneme z $n$ úplných sčítačiek reťazením: $C_{out}$ bitu $i$ ide do $C_{in}$ bitu $i + 1$. Najnižší bit dostane prenos 0, prenos z najvyššieho bitu vyjde von ako príznak **C**. Návrh sa s počtom bitov nemení, mení sa len počet kópií.

Cena: najvyšší bit nemôže dopočítať, kým k nemu nedorazí prenos zdola. Pri 64 bitoch musí prenos prejsť cez 64 stupňov za sebou — sčítačka je pomalá. (Rýchlejšie sčítačky predpovedajú prenos dopredu.)

### Odčítačka je skoro sčítačka

Záporné čísla sú v **dvojkovom doplnku**: $-B = \overline{B} + 1$ (invertujeme všetky bity a pripočítame 1). Preto
$$A - B = A + \overline{B} + 1$$
Žiaden nový obvod: pred vstup $B$ dáme invertory (XOR s riadiacim bitom „odčítaj“) a jednotku privedieme ako vstupný prenos najnižšieho bitu.

Na 4 bitoch je rozsah čísel bez znamienka 0 až 15, so znamienkom −8 až 7. Napríklad $-3 = \overline{0011} + 1 = 1100 + 1 = 1101$.

::: quiz
Dvojkový doplnok čísla 5 na 4 bitoch ($-5$) je
- [ ] 1010
- [x] 1011
- [ ] 0101
> $\overline{0101} = 1010$, plus 1 je $1011$.
:::

## ALU, príznaky a registre

**ALU** (aritmeticko-logická jednotka) v jednoduchom procesore počíta **všetky** svoje operácie naraz (súčet, prenesenie operandu, logické operácie …) a multiplexor na výstupe vyberie tú, ktorú chce riadiaca jednotka.

Okrem výsledku ALU hlási, **aký** výsledok je — **príznaky (flags)**:

| príznak | názov | nastaví sa na 1, keď |
|---|---|---|
| **Z** | zero | všetky bity výsledku sú 0 |
| **C** | carry | vznikol prenos z najvyššieho bitu (výsledok bez znamienka je mimo rozsahu) |
| **N** | negative | najvyšší bit výsledku je 1 (v doplnkovom kóde záporné číslo) |
| **V** | overflow | znamienko výsledku vyšlo nesprávne — pretečenie čísel so znamienkom |

Pretečenie **V** nastane pri sčítaní, keď majú oba sčítance rovnaké znamienko a výsledok opačné (napr. $0111 + 0001 = 1000$: $7 + 1$ „dá“ $-8$). Pri sčítaní čísel s rôznym znamienkom k pretečeniu nikdy nedôjde.

Bez príznakov by procesor nevedel **vetviť** (podmienený skok). Práve tu sa z kalkulačky stáva procesor.

::: drill d7-priznaky

::: quiz
Prečo môže ALU počítať všetky operácie naraz a nič sa nepokazí?
- [x] výsledky idú len do multiplexora, ktorý pustí ďalej jediný — ten, čo vybrala riadiaca jednotka
- [ ] každá operácia má vlastný akumulátor
- [ ] operácie sa striedajú po taktoch
> Ostatné výsledky sa jednoducho zahodia; výber je riadiaci signál pre multiplexor.
:::

**Register** je $n$ preklápacích obvodov D vedľa seba so spoločnými signálmi **CLK** a **WRITE**: pri hodinovom impulze s WRITE = 1 sa naraz zapíše celé slovo, pri WRITE = 0 si register drží starú hodnotu. CLK a WRITE sú riadiace signály, nie údaje.

**Pole registrov**: viac registrov a adresa. Multiplexor podľa adresy vyberá, ktorý register sa **číta**; demultiplexor podľa tej istej adresy, do ktorého sa **zapisuje**.

**Akumulátor** (ACC) je register, ktorého obsah ide na vstup ALU a výsledok ALU sa doň vracia. ALU sama nič nepamätá; dvojica ALU + akumulátor počíta v čase. Príklad $3 + 4 + 2$ s jednou sčítačkou za tri takty: ACC = 0 → 3 → 7 → 9; vo štvrtom takte je WRITE = 0, takže ACC ostane 9.

**Zbernica** je spoločná cesta medzi blokmi (prepojiť každý s každým sa nedá). Pravidlo: v jednom okamihu smie **vysielať len jeden** zdroj; kto, určuje riadenie.

**Riadiaca jednotka** je **stavový automat** ako z 5. a 6. lekcie: vstupy sú operačný kód z registra inštrukcie IR a príznaky z ALU, výstupy sú riadiace signály (kto vysiela na zbernicu, čo robí ALU, ktorý register zapisuje).

## 4-bitový procesor

Inštrukcia má 4 bity: **dva bity operačného kódu** (OC — čo robiť) a **dva bity adresy** (ADR — s čím). Rozdelenie je rozhodnutie návrhára: s 3 bitmi OC by bolo 8 operácií, ale len 2 adresy.

| OC | inštrukcia | význam | trieda |
|---|---|---|---|
| 00 | LDA adr | ACC ← M[adr] | prenos údajov |
| 01 | ADD adr | ACC ← ACC + M[adr] | aritmetika |
| 10 | STA adr | M[adr] ← ACC | prenos údajov |
| 11 | JMP adr | PC ← adr | riadenie toku |

Procesor má oddelenú pamäť programu (4 slová, adresuje ich počítadlo inštrukcií **PC**) a pamäť údajov (4 slová M[0] … M[3]). Všetko ide cez akumulátor — najstarší a najlacnejší spôsob, ako sa vyhnúť inštrukciám s dvoma operandmi.

Každá inštrukcia prejde tromi stavmi riadiaceho automatu:

1. **výber** (fetch) — PC ide do pamäte programu, inštrukcia sa uloží do IR;
2. **dekódovanie** — riadiaca jednotka rozloží OC a ADR a pripraví signály (nič sa nezapisuje);
3. **vykonanie** — napr. pre ADD: z pamäte príde M[adr], ALU sčíta, výsledok ide do ACC, nastavia sa príznaky, PC + 1.

Program $M[2] = M[0] + M[1]$, ak $M[0] = 3$, $M[1] = 4$:

| adresa | inštrukcia | kód | čo sa stane | ACC |
|---|---|---|---|---|
| 0 | LDA 0 | 0000 | ACC ← M[0] | 3 |
| 1 | ADD 1 | 0101 | ACC ← ACC + M[1] | 7 |
| 2 | STA 2 | 1010 | M[2] ← ACC | 7 |
| 3 | JMP 3 | 1111 | skok sám na seba — stop | 7 |

Štyri inštrukcie × 3 fázy = 12 taktov, potom procesor donekonečna opakuje JMP 3.

V úlohách píšete program po riadkoch (`LDA 0`, alebo binárne `0000`); stránka ho odsimuluje. Prázdne slovo pamäte programu sa správa ako skok sám na seba.

::: drill d7-program

::: quiz
Inštrukcia s kódom 1001 je
- [ ] LDA 1
- [x] STA 1
- [ ] ADD 2
> OC = 10 je STA, ADR = 01 je adresa 1.
:::

::: quiz
Čo nášmu procesoru chýba, aby sa v ňom dal napísať cyklus s podmienkou?
- [x] podmienený skok (podľa príznakov)
- [ ] akumulátor
- [ ] pamäť údajov
> JMP skáče vždy. Podmienený skok by sa rozhodoval podľa Z, C, N alebo V — na to treba širší formát inštrukcie.
:::

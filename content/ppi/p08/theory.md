> Podľa prednášky PPI „Ako procesor skutočne vykonáva inštrukciu“ (M. Janeba): trojstavové hradlo a zbernica, registre MAR a MBR, mikrooperácie v zápise RTL, mikroinštrukcie, riadiaca jednotka s pevnou logikou a mikroprogramom, CISC a RISC.

## Technický dlh

Pri stavbe 4-bitového procesora sme si dovolili tri zjednodušenia. Takéto vedomé skratky sa volajú **technický dlh**: umožnia pohnúť sa dopredu, ale každý ďalší krok s nimi stojí trochu viac („úrok“) a raz ich treba splatiť. Chybou nie je dlh, ale zabudnúť naň.

| zjednodušenie | čo nás stojí | ako ho splatíme |
|---|---|---|
| pamäť je vnútri procesora | inštrukčný cyklus vyzerá kratší, než je | registre MAR a MBR |
| na zbernici vysiela len jeden „lebo sme sa dohodli“ | nevieme postaviť reálnu zbernicu | trojstavové hradlo |
| 4-bitová inštrukcia bez podmieneného skoku | nedá sa napísať cyklus ani vetvenie | širší formát inštrukcie (neskôr) |

## Trojstavové hradlo a zbernica

Ak by na jeden vodič boli pripojené dva bežné výstupy a jeden by dával 0 a druhý 1, vznikol by skrat. Riešením nie je tretia logická hodnota, ale možnosť výstup **úplne odpojiť**. **Trojstavové hradlo** má vstup povolenia **EN**:

- EN = 1: výstup = vstup (0 alebo 1);
- EN = 0: výstup je v stave **vysokej impedancie (Z)** — správa sa, akoby hradlo vôbec nebolo pripojené.

Na zbernici má každý zdroj vlastné trojstavové hradlo a **dekodér** (vlastne demultiplexor) povolí práve jedno z nich. Pravidlo „vysiela len jeden“ je teraz vynútené obvodom, nie dohodou.

::: drill d8-zbernica

::: quiz
Trojstavové hradlo má EN = 0 a na vstupe 1. Na výstupe je
- [ ] 1
- [ ] 0
- [x] vysoká impedancia (odpojený výstup)
> Pri EN = 0 hradlo na vodič nič nevysiela, iné zdroje môžu vodič ovládať.
:::

## Pamäť je vonku: MAR a MBR

Skutočný procesor má **jednu spoločnú zbernicu von** a pamäť je na nej ako ktorékoľvek iné zariadenie. Z toho plynú tri obmedzenia:

- adresa a údaje nejdú naraz — procesor najprv pošle adresu, až potom prídu údaje;
- pamäť odpovedá s oneskorením a procesor zbernicu medzitým nikomu inému nepustí;
- adresu aj odpoveď treba počas prenosu **podržať**.

Preto sú na rozhraní procesora dva registre:

- **MAR** (Memory Address Register) drží adresu a vysiela ju na adresovú zbernicu;
- **MBR** (Memory Buffer Register) drží slovo, ktoré ide do pamäte alebo z nej — je **obojsmerný**.

Riadiaca jednotka k nim pridáva signály čítania a zápisu pamäte (MEMRD#, MEMWR#; znak # značí aktívnu nulu). To, čo sme minule kreslili ako jednu šípku „inštrukcia z pamäte do IR“, trvá v skutočnosti **tri takty**.

## Mikrooperácie a RTL

**Mikrooperácia** je jeden medziregistrový prenos, ktorý sa dá vyvolať **jedným riadiacim signálom**. Zapisuje sa v **RTL** (Register Transfer Language) — nie je to programovací jazyk, ale spôsob zápisu: šípka znamená „dostane hodnotu“.

| RTL | čo sa stane | riadiaci signál |
|---|---|---|
| MAR ← PC | adresa inštrukcie ide do MAR | PC_TO_MAR |
| MBR ← Pamäť[MAR] | pamäť dá slovo na údajovú zbernicu | MEM_RD |
| IR ← MBR | inštrukcia sa uloží do IR | MBR_TO_IR |
| PC ← PC + 1 | ukazovateľ na ďalšiu inštrukciu | INC_PC |
| ACC ← ACC + MBR | ALU sčíta, výsledok do ACC | ADD_TO_ACC |

**Mikroinštrukcia** je skupina mikrooperácií vykonaných v **jednom takte**. Mikrooperácie môžu bežať naraz, ak nesúperia o tú istú zbernicu ani o ten istý cieľový register a ak jedna nepotrebuje výsledok druhej.

| dvojica | naraz? | prečo |
|---|---|---|
| MBR ← Pamäť[MAR] a IR ← MBR | nie | druhá potrebuje výsledok prvej |
| MAR ← PC a MAR ← IR.ADR | nie | dva zdroje pre jeden register |
| MAR ← PC a PC ← PC + 1 | áno | rôzne cieľové registre; MAR dostane starú hodnotu PC |

Tieto závislosti určujú, koľko taktov inštrukcia trvá.

::: drill d8-paralelne

::: quiz
Ktorá dvojica mikrooperácií **nemôže** byť v jednom takte?
- [ ] MAR ← PC a PC ← PC + 1
- [x] MBR ← Pamäť[MAR] a IR ← MBR
- [ ] MAR ← IR.ADR a MBR ← ACC
> IR potrebuje slovo, ktoré MBR ešte len dostane — druhá závisí od výsledku prvej.
:::

## Celý inštrukčný cyklus v RTL

Výber je spoločný pre všetky inštrukcie, potom sa cesta rozvetví podľa operačného kódu:

| fáza | takt | mikrooperácie |
|---|---|---|
| výber | 1 | MAR ← PC, PC ← PC + 1 |
| výber | 2 | MBR ← Pamäť[MAR] |
| výber | 3 | IR ← MBR |
| LDA | 4 | MAR ← IR.ADR |
| LDA | 5 | MBR ← Pamäť[MAR] |
| LDA | 6 | ACC ← MBR |
| ADD | 4 – 5 | ako LDA |
| ADD | 6 | ACC ← ACC + MBR, príznaky |
| STA | 4 | MAR ← IR.ADR, MBR ← ACC |
| STA | 5 | Pamäť[MAR] ← MBR |
| JMP | 4 | PC ← IR.ADR |

Spolu teda LDA a ADD trvajú 6 taktov, STA 5 a JMP 4.

::: quiz
Koľko taktov trvá inštrukcia STA v tomto procesore?
- [ ] 4
- [x] 5
- [ ] 6
> 3 takty výberu + 2 takty vykonania (MAR ← IR.ADR s MBR ← ACC naraz, potom zápis do pamäte).
:::

## Riadiaca jednotka: pevná logika alebo mikroprogram

Zoznam mikrooperácií a taktov už máme. Obvod, ktorý ich v správnom poradí zapína, sa dá postaviť dvoma spôsobmi.

**Pevná logika (hardwired)** — sekvenčný obvod (stavový automat + kombinačná logika), aký sme navrhovali v 6. lekcii. Vstupy: operačný kód a príznaky; stavový register drží, v ktorom takte inštrukcie sme; výstupy: riadiace signály.

- rýchla — signály vznikajú priamo v hradlách, bez čítania pamäte;
- drahá na návrh — každá zmena inštrukčnej sady znamená prekresliť obvod;
- chyba v riadení sa po výrobe nedá opraviť (nová revízia čipu);
- typická pre **RISC**: jednoduchú a stabilnú sadu sa oplatí „zadrátovať“.

**Mikroprogram** — každý riadok tabuľky riadiacich signálov uložíme ako slovo do **pamäte mikroprogramov**; malý vnútorný obvod ich vykonáva ako program (počítadlo MPC). Typy mikroinštrukcií:

| typ | čo robí | ako pokračuje |
|---|---|---|
| výkonná | zapne riadiace signály | MPC + 1 |
| skoková | nepodmienený skok v mikroprograme | MPC ← adresové pole |
| testovacia | pozrie sa na príznak | MPC + 1 alebo skok |
| dekódovacia | pozrie sa na operačný kód | MPC ← výstup mapovacej logiky |

Celá fáza dekódovania je teda **jediná** dekódovacia mikroinštrukcia. **Mapovacia logika** prekladá operačný kód na adresu jeho mikrorutiny v pamäti mikroprogramov. Ak sú operačné kódy zvolené vhodne, stačí posun bitov — napr. mikrorutina inštrukcie s kódom OC začína na adrese $4 \cdot \text{OC} + \text{základ}$ — a nepotrebujeme žiadnu tabuľku.

::: drill d8-riadenie

## CISC a RISC

| | pevná logika | mikroprogram |
|---|---|---|
| rýchlosť | vyššia | nižšia (každý takt sa číta z pamäte) |
| zmena inštrukcie | nový obvod | prepísanie pamäte |
| zložité inštrukcie | ťažko realizovateľné | prirodzené |
| návrh | náročný | prehľadný a systematický |
| kde | RISC | CISC |

Z voľby riadenia vyplývajú dve rodiny procesorov:

| | CISC | RISC |
|---|---|---|
| riadiaca časť | mikroprogram | pevná logika |
| inštrukčná sada | veľká, zložité operácie | malá, jednoduché operácie |
| dĺžka inštrukcie | premenlivá | pevná |
| spôsobov adresovania | veľa | málo |
| taktov na inštrukciu | viac | jeden alebo dva |
| inštrukcií na program | menej | viac |

Pri mikroprograme stojí nová zložitá inštrukcia len pár riadkov v pamäti — preto ich CISC pridáva. Pri pevnej logike je každá inštrukcia nový obvod — preto RISC má málo jednoduchých. Voľba riadenia a návrh inštrukčnej sady nie sú nezávislé rozhodnutia.

::: quiz
Ktorá vlastnosť patrí RISC?
- [ ] premenlivá dĺžka inštrukcie
- [x] pevná dĺžka inštrukcie a pevná logika riadenia
- [ ] mikroprogramové riadenie
> RISC má malú sadu jednoduchých inštrukcií rovnakej dĺžky, ktoré sa oplatí zadrátovať.
:::

::: quiz
Chybu v riadení procesora výrobca opravil aktualizáciou bez výmeny čipu. Riadenie je pravdepodobne
- [x] mikroprogramové
- [ ] s pevnou logikou
> Pamäť mikroprogramov sa dá prepísať; pevná logika by vyžadovala novú revíziu čipu.
:::

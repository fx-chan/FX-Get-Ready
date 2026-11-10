> Podľa 1. prednášky PPI (J. Hudec): základná koncepcia počítačových systémov a úvod do výrokovej logiky a Booleovej algebry.

## Čo je počítačové inžinierstvo

**Informatika** sa zaoberá informáciou v celom jej živote: od zberu a prenosu cez triedenie, ukladanie a aktualizáciu až po spracovanie, vyhodnotenie a využitie. Ako technická disciplína skúma výpočty po stránke hardvéru aj softvéru.

**Počítačové inžinierstvo** je jej časť, ktorá počítače a počítačom riadené zariadenia **navrhuje, konštruuje, implementuje a udržiava**. Stojí na pomedzí dvoch svetov:

- elektrotechnika: elektronika, siete, návrh čipov;
- informatika: algoritmy, dátové štruktúry, operačné systémy;
- a priestor, kde sa stretávajú: **digitálna logika** a návrh počítača. Práve ten je náplňou tohto predmetu.

Základné pojmy: **počítač**, **výpočtový proces**, **hardvér**, **softvér**. **Program** je postupnosť inštrukcií a údajov. **Počítačový systém** = počítač + doplnkový hardvér + softvér.

## Von Neumannova (princetonská) architektúra

John von Neumann (1946, Princeton) opísal počítač riadený **postupnosťou inštrukcií**. Má päť jednotiek:

| jednotka | úloha |
|---|---|
| pamäť | uchováva **inštrukcie aj údaje** |
| riadiaca jednotka | vyberá inštrukcie z pamäte a riadi ostatné jednotky |
| aritmetická (aritmeticko-logická) jednotka | vykonáva operácie nad údajmi |
| vstupná jednotka | prijíma údaje zvonka |
| výstupná jednotka | odovzdáva výsledky |

Typické črty:

- program aj spracúvané údaje ležia v **tej istej pamäti**;
- spracovanie určuje **postupnosť inštrukcií**;
- k inštrukciám aj údajom sa pristupuje **rovnako**, po tých istých adresových, údajových a riadiacich signáloch;
- čísla sú v **dvojkovej** sústave.

Dôsledok: inštrukcia a údaj nemôžu ísť z pamäte naraz, lebo cesta k pamäti je jediná. Toto úzke miesto sa nazýva *von Neumannovo hrdlo*.

## Harvardská architektúra

Howard Aiken, počítač **MARK I** (1944): **oddelené** pamäte (a adresové priestory) pre program a pre údaje, každá s vlastnou cestou. Procesor tak môže v jednom kroku čítať inštrukciu aj údaj. Dnes ju nájdeme v mikrokontroléroch a signálových procesoroch; bežné procesory ju používajú vo vnútri (oddelené vyrovnávacie pamäte pre inštrukcie a údaje).

::: drill d1-architektura

::: quiz
Ktorá vlastnosť patrí **harvardskej** architektúre?
- [ ] program a údaje sú v jednej spoločnej pamäti
- [x] program a údaje majú oddelené pamäte a oddelené cesty k nim
- [ ] inštrukcie sa vyberajú z pamäte náhodne
> Oddelenie pamäte programu a pamäte údajov je jej definujúca črta; spoločná pamäť je znak von Neumannovej architektúry.
:::

## Počítačový systém dnes

Procesor, pamäť (**hlavná** a **sekundárna**) a vstupno-výstupný podsystém. Ten tvoria vstupné zariadenia (klávesnica, myš, dotyková obrazovka), výstupné zariadenia (displej, tlačiareň, zvuk) a komunikačné zariadenia (sieť, Wi-Fi, NFC, IR).

## Klasifikácia počítačov

Podľa **aplikačného určenia**: univerzálne, problémovo orientované, špecializované. Ďalšie kritériá: technické parametre, spôsob prístupu používateľa, druh spracúvanej informácie, kapacita pamäte…

Základná klasifikácia podľa **spôsobu pamätania údajov**: princetonská a harvardská architektúra (pozri vyššie).

### Flynnova klasifikácia (1966)

Kritérium: koľko **tokov inštrukcií** (I) a koľko **tokov údajov** (D) počítač spracúva súčasne.

| trieda | inštrukcie | údaje | príklad |
|---|---|---|---|
| **SISD** | jeden | jeden | klasický sériový jednoprocesorový počítač von Neumannovho typu |
| **SIMD** | jeden | veľa | maticový počítač, výpočty na grafickej karte (ten istý príkaz nad mnohými číslami) |
| **MISD** | veľa | jeden | prúdové spracovanie; viac jednotiek počíta nad tými istými údajmi kvôli spoľahlivosti (vesmírna technika) |
| **MIMD** | veľa | veľa | viacprocesorové a distribuované systémy, viacjadrové procesory |

::: drill d1-flynn

::: quiz
Grafická karta vynásobí naraz 1000 dvojíc čísel jednou inštrukciou. Ktorá trieda?
- [ ] SISD
- [x] SIMD
- [ ] MISD
- [ ] MIMD
> Jedna inštrukcia, veľa údajov: SIMD.
:::

### Podľa spôsobu riadenia a typu procesora

- **riadenie tokom inštrukcií** (control flow) — von Neumannov typ, poradie určuje program;
- **riadenie tokom údajov** (data flow) — operácia sa vykoná, keď sú pripravené jej operandy;
- **riadenie tokom požiadaviek** (demand flow) — počíta sa až to, čo si niekto vyžiada.

Typ procesora: **CISC** (Complex Instruction Set Computer — veľa zložitých inštrukcií), **RISC** (Reduced — málo jednoduchých inštrukcií), **NISC** (No Instruction Set — bez pevnej inštrukčnej sady, riadenie generuje prekladač priamo). K CISC a RISC sa vrátime v poslednej lekcii.

## Od tranzistora k čipu

Logickú hodnotu v počítači reprezentuje **spínač**. Pôvodne mechanický, dnes **tranzistor** (vynález 1947, Nobelova cena 1956 pre Bardeena, Brattaina a Shockleyho). V tranzistore MOS riadi napätie na hradlovej elektróde G, či medzi elektródami S a D vznikne vodivý kanál: tranzistor je „zopnutý“ alebo „rozopnutý“. Medzi hradlom a substrátom je tenká izolačná vrstva.

Výroba **integrovaného obvodu** v skratke:

1. z kremičitého piesku sa chemicky vyčistí monokryštál — **kremíková tyč (ingot)**;
2. tyč sa rozreže na tenké **plátky (wafer)**, ktoré sa brúsia a leštia;
3. pomocou **masiek**, oxidácie, implantácie a difúzie sa na plátku vytvoria vrstvy tranzistorov a spojov;
4. ryhy oddelia jednotlivé obvody, plátok sa **otestuje**, rozláme na čipy a chybné sa vyradia;
5. pripoja sa vývody a čip sa **zapuzdrí** do plastového či keramického puzdra.

Trendy: menší výrobný proces (nm), viac jadier, **hybridná architektúra** (výkonné P-jadrá a úsporné E-jadrá) a **čiplety** — namiesto jedného veľkého kusu kremíka (system-on-chip) sa skladá viac menších čipov v jednom puzdre (system-on-package), pokojne z rôznych výrobných procesov.

::: drill d1-cip

## Výroky

**Výrok** je oznamovacia veta, pri ktorej má zmysel pýtať sa, či je pravdivá. Má práve jednu pravdivostnú hodnotu: **1** (pravda) alebo **0** (nepravda). Výrokmi **nie sú** otázky, rozkazy, zvolania, pozdravy ani neúplné vety. Výrok môže byť aj nepravdivý — „Streda je prvý deň týždňa“ je výrok s hodnotou 0.

::: quiz
Ktorá veta **je** výrok?
- [ ] Zatvor dvere!
- [ ] Koľko je hodín?
- [x] Číslo 7 je párne.
- [ ] Dobrý večer.
> Je to oznamovacia veta s jednoznačnou pravdivostnou hodnotou (0). Ostatné sú rozkaz, otázka a pozdrav.
:::

## Booleova algebra

George Boole (1815–1864) prepísal výrokovú logiku do podoby **algebry**. Základné operácie: logický **súčet** (OR, $a + b$), logický **súčin** (AND, $a \cdot b$ alebo $ab$) a **negácia** (NOT, $\overline{a}$).

V odpovediach na tejto stránke píšete negáciu ako `a'` alebo `!a`, súčin ako `ab` alebo `a*b`, súčet `a+b`.

| pravidlo | pre súčet | pre súčin |
|---|---|---|
| komutatívnosť | $a + b = b + a$ | $ab = ba$ |
| asociatívnosť | $a + (b + c) = (a + b) + c$ | $a(bc) = (ab)c$ |
| distributívnosť | $a + bc = (a + b)(a + c)$ | $a(b + c) = ab + ac$ |
| idempotencia | $a + a + \dots + a = a$ | $a \cdot a \cdots a = a$ |
| komplement | $a + \overline{a} = 1$ | $a\overline{a} = 0$ |
| agresívna hodnota | $a + 1 = 1$ | $a \cdot 0 = 0$ |
| neutrálna hodnota | $a + 0 = a$ | $a \cdot 1 = a$ |
| De Morgan | $\overline{a + b} = \overline{a}\,\overline{b}$ | $\overline{ab} = \overline{a} + \overline{b}$ |
| absorpcia | $a + ab = a$ | $a(a + b) = a$ |
| absorpcia negácie | $a + \overline{a}b = a + b$ | $a(\overline{a} + b) = ab$ |
| spojovanie | $ab + \overline{a}b = b$ | $(a + b)(\overline{a} + b) = b$ |
| konsenzus | $ab + \overline{a}c + bc = ab + \overline{a}c$ | $(a + b)(\overline{a} + c)(b + c) = (a + b)(\overline{a} + c)$ |

Dvojitá negácia: $\overline{\overline{a}} = a$. Pozor: distributívnosť súčtu cez súčin ($a + bc = (a+b)(a+c)$) v bežnej aritmetike neplatí, v Booleovej algebre áno.

**Princíp duality**: ak vo vzťahu vymeníme $+ \leftrightarrow \cdot$ a $0 \leftrightarrow 1$, dostaneme opäť platný vzťah. Preto má tabuľka dva stĺpce.

Ako sa dokazuje pravidlo? Buď úpravou cez iné pravidlá, alebo **pravdivostnou tabuľkou**: dve funkcie sú rovnaké, ak majú rovnakú hodnotu vo všetkých kombináciách premenných. Napríklad absorpcia negácie: $a + \overline{a}b = (a + \overline{a})(a + b) = 1 \cdot (a + b) = a + b$ (distributívnosť, komplement, neutrálna hodnota).

::: drill d1-zakony

::: quiz
Čomu sa rovná $\overline{\overline{a} + b}$?
- [ ] $a + \overline{b}$
- [x] $a\overline{b}$
- [ ] $\overline{a}b$
> De Morgan: $\overline{\overline{a} + b} = \overline{\overline{a}}\cdot\overline{b} = a\overline{b}$.
:::

::: quiz
Ktorá rovnosť v Booleovej algebre **neplatí**?
- [ ] $a + bc = (a + b)(a + c)$
- [ ] $a + \overline{a}b = a + b$
- [x] $a + b = a\,b$
- [ ] $ab + \overline{a}b = b$
> Pre $a = 1, b = 0$ je vľavo 1 a vpravo 0. Ostatné sú distributívnosť, absorpcia negácie a spojovanie.
:::

::: quiz
Výraz $xy + \overline{x}z + yz$ sa dá zjednodušiť na
- [x] $xy + \overline{x}z$
- [ ] $xy + z$
- [ ] $y + z$
> Konsenzus: člen $yz$ je nadbytočný, lebo keď $y = z = 1$, je pravdivý už $xy$ (pre $x = 1$) alebo $\overline{x}z$ (pre $x = 0$).
:::

## Postup pri zjednodušovaní

1. Odstráňte dvojité negácie a negácie zložených výrazov (De Morgan) — negácia má nakoniec stáť len nad premennými.
2. Roznásobte (distributívnosť) do tvaru súčtu súčinov.
3. Hľadajte dvojice $ab + a\overline{b} = a$ (spojovanie), pohltené členy $a + ab = a$ (absorpcia) a konsenzy.

Príklad: $\overline{\overline{a}b} \cdot (a + b) = (a + \overline{b})(a + b) = a + \overline{b}b = a$.

V ďalšej lekcii uvidíte, že to isté sa dá robiť mechanicky cez **mapy**, bez hľadania vhodného pravidla.

> Zdroj: poznámky z prednášky a cvičení. Učebnica Anton–Rorres teóriu grafov nepokrýva, preto sa tu držíme pojmov z prednášky.

## Sedem mostov

Teória grafov **nie je** kreslenie grafov funkcií $y = f(x)$. Je to časť diskrétnej matematiky o objektoch (vrcholoch) a väzbách medzi nimi (hranách).

Začala sa v roku 1736 úlohou, ktorú riešil Leonhard Euler. Mesto Königsberg delila rieka s dvoma ostrovmi a štyri časti mesta spájalo sedem mostov. Dá sa prejsť každý most práve raz a vrátiť sa na štart? Euler si všimol, že na tvare mesta nezáleží: časti mesta sú vrcholy, mosty sú hrany a dôležité je len to, čo s čím súvisí.

<div class="graph"><svg viewBox="0 0 330 240" width="330" role="img" aria-label="graf"><defs><marker id="ga1" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M108,114.9 Q156.6,95.9 151.4,43.9"/><path class="ed" d="M93.6,106.1 Q88.4,54.1 137,35.1"/><path class="ed" d="M93.6,133.9 Q88.4,185.9 137,204.9"/><path class="ed" d="M108,125.1 Q156.6,144.1 151.4,196.1"/><path class="ed" d="M109,120 Q192.5,120 276,120"/><path class="ed" d="M161.8,37.6 Q220,75 278.2,112.4"/><path class="ed" d="M161.8,202.4 Q220,165 278.2,127.6"/><g class="nd"><circle cx="150" cy="30" r="14"/><text x="150" y="30">C</text></g><text class="dg" x="172" y="14">3</text><g class="nd"><circle cx="95" cy="120" r="14"/><text x="95" y="120">A</text></g><text class="dg" x="69" y="120">5</text><g class="nd"><circle cx="150" cy="210" r="14"/><text x="150" y="210">B</text></g><text class="dg" x="172" y="230">3</text><g class="nd"><circle cx="290" cy="120" r="14"/><text x="290" y="120">D</text></g><text class="dg" x="314" y="104">3</text></svg></div>

Čísla pri vrcholoch sú stupne. Na konci lekcie uvidíte, prečo odpoveď znie **nie**: všetky štyri vrcholy majú nepárny stupeň.

## Graf, rád a veľkosť

**Graf** je dvojica $G = (V, E)$: $V$ je množina vrcholov, $E$ množina hrán. Píšeme aj $V(G)$, $E(G)$. V neorientovanom grafe hranu označíme jej koncami a na poradí nezáleží: $AD = DA$.

<div class="graph"><svg viewBox="0 0 340 220" width="340" role="img" aria-label="graf"><defs><marker id="ga2" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M181.9,37.3 Q235,70 288.1,102.7"/><path class="ed" d="M181.9,182.7 Q235,150 288.1,117.3"/><path class="ed" d="M170,44 Q170,110 170,176"/><path class="ed" d="M158.1,37.3 Q105,70 51.9,102.7"/><path class="ed" d="M51.9,117.3 Q105,150 158.1,182.7"/><g class="nd"><circle cx="170" cy="30" r="14"/><text x="170" y="30">A</text></g><g class="nd"><circle cx="40" cy="110" r="14"/><text x="40" y="110">B</text></g><g class="nd"><circle cx="300" cy="110" r="14"/><text x="300" y="110">D</text></g><g class="nd"><circle cx="170" cy="190" r="14"/><text x="170" y="190">C</text></g><text class="el" x="229.2" y="79.4">h₁</text><text class="el" x="229.2" y="140.6">h₂</text><text class="el" x="159" y="110">h₃</text><text class="el" x="110.8" y="79.4">h₄</text><text class="el" x="99.2" y="159.4">h₅</text></svg></div>

Tu $V = \{A, B, C, D\}$ a $E = \{AD, CD, AC, AB, BC\}$.

- **rád** $\operatorname{order}(G) = |V|$ je počet vrcholov (tu 4),
- **veľkosť** $\operatorname{size}(G) = |E|$ je počet hrán (tu 5).

Čo je ešte graf: jeden vrchol bez hrán $(\{A\}, \emptyset)$ áno, podľa prednášky aj $(\emptyset, \emptyset)$. Hrana s voľným koncom nie: hrana vždy spája dva vrcholy (pri slučke ten istý dvakrát). Ten istý graf môžeme nakresliť rovno aj „zamotane“, stále je to ten istý graf.

::: drill dg-rad-velkost

## Vrcholy a hrany

- **Incidencia:** hrana $h = \{u, v\}$ je incidentná s vrcholmi $u$ a $v$ (a naopak).
- **Susedné vrcholy** sú vrcholy spojené hranou.
- **Násobné hrany:** dva vrcholy spája viac ako jedna hrana.
- **Slučka:** hrana, ktorá začína aj končí v tom istom vrchole.
- **Izolovaný vrchol** nie je incidentný so žiadnou hranou. Vrchol, ktorý má iba slučku, izolovaný **nie je**.

<div class="graph"><svg viewBox="0 0 290 260" width="290" role="img" aria-label="graf"><defs><marker id="ga3" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M49.6,99.8 Q122.8,22.5 226.4,46.8"/><path class="ed" d="M53.4,106 Q140,80 226.6,54"/><path class="ed" d="M53.6,113.2 Q157.2,137.5 230.4,60.2"/><path class="ed" d="M235.7,63.3 Q220,112.5 204.3,161.7"/><path class="ed c3" d="M206.1,187.6 C234.8,212.3 165.2,212.3 193.9,187.6"/><g class="nd"><circle cx="40" cy="110" r="14"/><text x="40" y="110">A</text></g><g class="nd"><circle cx="240" cy="50" r="14"/><text x="240" y="50">B</text></g><g class="nd"><circle cx="200" cy="175" r="14"/><text x="200" y="175">C</text></g><text class="el" x="128.2" y="40.7">h₁</text><text class="el" x="113.2" y="99.5">h₂</text><text class="el" x="151.8" y="119.3">h₃</text><text class="el" x="209.5" y="109.1">h₄</text><text class="el" x="200" y="225.5">h₅</text></svg><svg viewBox="0 0 330 190" width="330" role="img" aria-label="graf"><defs><marker id="ga4" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M53.9,108.5 Q119.2,101.4 161.1,50.8"/><path class="ed" d="M48.9,99.2 Q90.8,48.6 156.1,41.5"/><path class="ed" d="M262.6,103.9 C287.3,75.2 287.3,144.8 262.6,116.1"/><g class="nd"><circle cx="40" cy="110" r="14"/><text x="40" y="110">A</text></g><g class="nd"><circle cx="170" cy="40" r="14"/><text x="170" y="40">B</text></g><g class="nd iso"><circle cx="110" cy="160" r="14"/><text x="110" y="160">C</text></g><g class="nd"><circle cx="250" cy="110" r="14"/><text x="250" y="110">D</text></g></svg></div>

Vľavo: $h_1$ až $h_3$ sú násobné hrany, $h_5$ je slučka, rád 3 a veľkosť 5. Vpravo je $C$ izolovaný, $D$ so slučkou nie.

::: quiz
Vrchol má iba slučku a žiadnu inú hranu. Je izolovaný?
- [ ] áno
- [x] nie
> Izolovaný vrchol nemá žiadnu incidentnú hranu. Slučka je incidentná a dáva stupeň 2.
:::

## Typy grafov

| typ | slučky | násobné hrany |
|---|---|---|
| pseudograf | môžu byť | môžu byť |
| multigraf | nie | môžu byť |
| jednoduchý (obyčajný) graf | nie | nie |
| triviálny graf | nemá ani hrany | nemá ani hrany |

Niektoré učebnice volajú triviálnym len graf s jedným vrcholom a graf bez hrán nazývajú prázdny. Na skúške používajte definíciu z prednášky.

**Orientovaný graf (digraf):** každá hrana má smer. Hrana $AB$ ide z $A$ do $B$, preto tu $AB \ne BA$.

<div class="graph"><svg viewBox="0 0 240 180" width="240" role="img" aria-label="graf"><defs><marker id="ga5" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M50.7,86 Q109.5,36.6 184,31.2" marker-end="url(#ga5)"/><path class="ed" d="M189.3,39 Q130.5,88.4 56,93.8" marker-end="url(#ga5)"/><path class="ed" d="M53.2,99.6 Q120,122.5 184.9,144.8" marker-end="url(#ga5)"/><g class="nd"><circle cx="40" cy="95" r="14"/><text x="40" y="95">A</text></g><g class="nd"><circle cx="200" cy="30" r="14"/><text x="200" y="30">B</text></g><g class="nd"><circle cx="200" cy="150" r="14"/><text x="200" y="150">C</text></g><text class="el" x="110.6" y="39.3">h₁</text><text class="el" x="129.4" y="85.7">h₂</text><text class="el" x="116.4" y="132.9">h₃</text></svg></div>

## Stupeň vrchola

**Stupeň** $\deg v$ je počet hrán incidentných s $v$, pričom **slučka sa počíta dvakrát**.

**Veta o súčte stupňov:**
$$\sum_{v \in V} \deg v = 2|E|$$
Každá hrana prispeje jednotkou každému zo svojich dvoch koncov.

**Dôsledok:** vrcholov nepárneho stupňa je vždy párny počet. Ak je súčet zadaných stupňov nepárny, graf neexistuje.

<div class="graph"><svg viewBox="0 0 340 230" width="340" role="img" aria-label="graf"><defs><marker id="ga31" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M46.4,187.5 Q68,145 46.4,102.5"/><path class="ed" d="M33.6,187.5 Q12,145 33.6,102.5"/><path class="ed" d="M54,90 Q105,90 156,90"/><path class="ed" d="M163.9,77.4 C135.2,52.7 204.8,52.7 176.1,77.4"/><path class="ed" d="M170,104 Q170,145 170,186"/><path class="ed" d="M54,200 Q105,200 156,200"/><path class="ed" d="M184,200 Q235,200 286,200"/><g class="nd"><circle cx="40" cy="90" r="14"/><text x="40" y="90">B</text></g><text class="dg" x="60" y="73">3</text><g class="nd"><circle cx="170" cy="90" r="14"/><text x="170" y="90">C</text></g><text class="dg" x="190" y="73">4</text><g class="nd iso"><circle cx="300" cy="90" r="14"/><text x="300" y="90">F</text></g><text class="dg" x="320" y="73">0</text><g class="nd"><circle cx="40" cy="200" r="14"/><text x="40" y="200">A</text></g><text class="dg" x="60" y="183">3</text><g class="nd"><circle cx="170" cy="200" r="14"/><text x="170" y="200">D</text></g><text class="dg" x="190" y="183">3</text><g class="nd"><circle cx="300" cy="200" r="14"/><text x="300" y="200">E</text></g><text class="dg" x="320" y="183">1</text></svg></div>

Súčet $3 + 3 + 4 + 3 + 1 + 0 = 14 = 2\cdot 7$.

**Pravidelný ($k$-pravidelný) graf:** všetky vrcholy majú stupeň $k$, a teda $|E| = \frac{nk}{2}$.

::: drill dg-stupne

::: drill dg-existencia

**Pozor:** párny súčet nestačí. V jednoduchom grafe s $n$ vrcholmi je stupeň najviac $n - 1$. Napríklad stupne $3, 3, 3, 1$ majú súčet 10, ale v jednoduchom grafe so 4 vrcholmi znamená stupeň 3 hranu ku všetkým ostatným, takže štvrtý vrchol by mal stupeň aspoň 3.

::: quiz
Graf má 7 hrán. Aký je súčet stupňov jeho vrcholov?
- [ ] 7
- [x] 14
- [ ] závisí od počtu vrcholov
> $\sum\deg v = 2|E| = 14$ bez ohľadu na počet vrcholov.
:::

::: quiz
Existuje jednoduchý graf s 5 vrcholmi, v ktorom má každý vrchol stupeň 3?
- [ ] áno
- [x] nie
> Súčet $5\cdot3 = 15$ je nepárny, takže by malo byť $|E| = 7{,}5$.
:::

## Špeciálne grafy

**Úplný graf** $K_n$: každé dva vrcholy spája práve jedna hrana. Každý vrchol má stupeň $n - 1$ a
$$|E(K_n)| = \frac{n(n-1)}{2}$$

<div class="graph"><svg viewBox="0 0 60 60" width="60" role="img" aria-label="graf"><defs><marker id="ga6" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><g class="nd"><circle cx="30" cy="30" r="14"/><text x="30" y="30">A</text></g></svg><svg viewBox="0 0 130 110" width="130" role="img" aria-label="graf"><defs><marker id="ga7" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M41.4,71.9 Q65,55 88.6,38.1"/><g class="nd"><circle cx="30" cy="80" r="14"/><text x="30" y="80">A</text></g><g class="nd"><circle cx="100" cy="30" r="14"/><text x="100" y="30">B</text></g></svg><svg viewBox="0 0 160 150" width="160" role="img" aria-label="graf"><defs><marker id="ga8" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M73.2,42.2 Q55,75 36.8,107.8"/><path class="ed" d="M86.8,42.2 Q105,75 123.2,107.8"/><path class="ed" d="M44,120 Q80,120 116,120"/><g class="nd"><circle cx="80" cy="30" r="14"/><text x="80" y="30">A</text></g><g class="nd"><circle cx="30" cy="120" r="14"/><text x="30" y="120">B</text></g><g class="nd"><circle cx="130" cy="120" r="14"/><text x="130" y="120">C</text></g></svg><svg viewBox="0 0 170 170" width="170" role="img" aria-label="graf"><defs><marker id="ga9" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M44,30 Q80,30 116,30"/><path class="ed" d="M39.9,39.9 Q80,80 120.1,120.1"/><path class="ed" d="M30,44 Q30,80 30,116"/><path class="ed" d="M130,44 Q130,80 130,116"/><path class="ed" d="M120.1,39.9 Q80,80 39.9,120.1"/><path class="ed" d="M116,130 Q80,130 44,130"/><g class="nd"><circle cx="30" cy="30" r="14"/><text x="30" y="30">A</text></g><g class="nd"><circle cx="130" cy="30" r="14"/><text x="130" y="30">B</text></g><g class="nd"><circle cx="130" cy="130" r="14"/><text x="130" y="130">C</text></g><g class="nd"><circle cx="30" cy="130" r="14"/><text x="30" y="130">D</text></g></svg><svg viewBox="0 0 206 196" width="206" role="img" aria-label="graf"><defs><marker id="ga10" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M111.3,38.2 Q133,54 154.7,69.8"/><path class="ed" d="M104.3,43.3 Q120.5,93 136.7,142.7"/><path class="ed" d="M95.7,43.3 Q79.5,93 63.3,142.7"/><path class="ed" d="M88.7,38.2 Q67,54 45.3,69.8"/><path class="ed" d="M161.7,91.3 Q153.5,117 145.3,142.7"/><path class="ed" d="M154.7,86.2 Q112.5,117 70.3,147.8"/><path class="ed" d="M152,78 Q100,78 48,78"/><path class="ed" d="M127,156 Q100,156 73,156"/><path class="ed" d="M129.7,147.8 Q87.5,117 45.3,86.2"/><path class="ed" d="M54.7,142.7 Q46.5,117 38.3,91.3"/><g class="nd"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g></svg></div>

**Doplnok** $\bar G$ má tie isté vrcholy a práve tie hrany, ktoré v $G$ chýbajú. Spolu dávajú $K_n$, takže $|E(\bar G)| = \frac{n(n-1)}{2} - |E(G)|$.

<div class="graph"><svg viewBox="0 0 170 150" width="170" role="img" aria-label="graf"><defs><marker id="ga14" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c3" d="M37.3,108.1 Q57.5,75 77.7,41.9"/><g class="nd"><circle cx="30" cy="120" r="14"/><text x="30" y="120">A</text></g><g class="nd iso"><circle cx="140" cy="120" r="14"/><text x="140" y="120">B</text></g><g class="nd"><circle cx="85" cy="30" r="14"/><text x="85" y="30">C</text></g></svg><svg viewBox="0 0 170 150" width="170" role="img" aria-label="graf"><defs><marker id="ga15" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c2" d="M44,120 Q85,120 126,120"/><path class="ed c2" d="M132.7,108.1 Q112.5,75 92.3,41.9"/><g class="nd"><circle cx="30" cy="120" r="14"/><text x="30" y="120">A</text></g><g class="nd"><circle cx="140" cy="120" r="14"/><text x="140" y="120">B</text></g><g class="nd"><circle cx="85" cy="30" r="14"/><text x="85" y="30">C</text></g></svg></div>

Tieto dva grafy na troch vrcholoch sú navzájom doplnkami: dokopy tvoria $K_3$.

**Bipartitný graf:** vrcholy sa dajú rozdeliť do dvoch skupín $V_1$, $V_2$ tak, že každá hrana vedie medzi skupinami. **Úplný bipartitný** $K_{m,n}$ spája každý vrchol z $V_1$ s každým z $V_2$, má $mn$ hrán. Užitočné kritérium: graf je bipartitný práve vtedy, keď nemá cyklus nepárnej dĺžky. Graf so slučkou bipartitný nikdy nie je.

<div class="graph"><svg viewBox="0 0 220 170" width="220" role="img" aria-label="graf"><defs><marker id="ga16" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M56.3,43.5 Q45,85 33.7,126.5"/><path class="ed" d="M65.8,42.7 Q85,85 104.2,127.3"/><path class="ed" d="M70.7,39 Q125,85 179.3,131"/><path class="ed" d="M149.3,39 Q95,85 40.7,131"/><path class="ed" d="M154.2,42.7 Q135,85 115.8,127.3"/><path class="ed" d="M163.7,43.5 Q175,85 186.3,126.5"/><g class="nd"><circle cx="60" cy="30" r="14"/><text x="60" y="30">A₁</text></g><g class="nd"><circle cx="160" cy="30" r="14"/><text x="160" y="30">A₂</text></g><g class="nd"><circle cx="30" cy="140" r="14"/><text x="30" y="140">B₁</text></g><g class="nd"><circle cx="110" cy="140" r="14"/><text x="110" y="140">B₂</text></g><g class="nd"><circle cx="190" cy="140" r="14"/><text x="190" y="140">B₃</text></g></svg></div>

**Planárny graf** sa dá nakresliť do roviny bez kríženia hrán. Úloha o troch domoch a troch zdrojoch, kde treba každý dom spojiť s každým zdrojom, je graf $K_{3,3}$ a ten planárny nie je. Ani $K_5$ nie je planárny. $K_4$ planárny je, len ho treba nakresliť inak:

<div class="graph"><svg viewBox="0 0 170 170" width="170" role="img" aria-label="graf"><defs><marker id="ga11" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M44,30 Q80,30 116,30"/><path class="ed" d="M39.9,39.9 Q80,80 120.1,120.1"/><path class="ed" d="M30,44 Q30,80 30,116"/><path class="ed" d="M130,44 Q130,80 130,116"/><path class="ed" d="M120.1,39.9 Q80,80 39.9,120.1"/><path class="ed" d="M116,130 Q80,130 44,130"/><g class="nd"><circle cx="30" cy="30" r="14"/><text x="30" y="30">A</text></g><g class="nd"><circle cx="130" cy="30" r="14"/><text x="130" y="30">B</text></g><g class="nd"><circle cx="130" cy="130" r="14"/><text x="130" y="130">C</text></g><g class="nd"><circle cx="30" cy="130" r="14"/><text x="30" y="130">D</text></g></svg><svg viewBox="0 0 160 155" width="160" role="img" aria-label="graf"><defs><marker id="ga12" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M73.5,37.4 Q52.5,77.5 31.5,117.6"/><path class="ed" d="M86.5,37.4 Q107.5,77.5 128.5,117.6"/><path class="ed" d="M80,39 Q80,58.5 80,78"/><path class="ed" d="M39,130 Q80,130 121,130"/><path class="ed" d="M36.5,122 Q52.5,111 68.5,100"/><path class="ed" d="M123.5,122 Q107.5,111 91.5,100"/><g class="nd"><circle cx="80" cy="25" r="14"/><text x="80" y="25">A</text></g><g class="nd"><circle cx="25" cy="130" r="14"/><text x="25" y="130">B</text></g><g class="nd"><circle cx="135" cy="130" r="14"/><text x="135" y="130">C</text></g><g class="nd"><circle cx="80" cy="92" r="14"/><text x="80" y="92">D</text></g></svg></div>

<div class="graph"><svg viewBox="0 0 280 180" width="280" role="img" aria-label="graf"><defs><marker id="ga13" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M40,44 Q40,90 40,136"/><path class="ed" d="M49,40.8 Q90,90 131,139.2"/><path class="ed" d="M52,37.2 Q140,90 228,142.8"/><path class="ed" d="M131,40.8 Q90,90 49,139.2"/><path class="ed" d="M140,44 Q140,90 140,136"/><path class="ed" d="M149,40.8 Q190,90 231,139.2"/><path class="ed" d="M228,37.2 Q140,90 52,142.8"/><path class="ed" d="M231,40.8 Q190,90 149,139.2"/><path class="ed" d="M240,44 Q240,90 240,136"/><g class="nd"><circle cx="40" cy="30" r="14"/><text x="40" y="30">D₁</text></g><g class="nd"><circle cx="140" cy="30" r="14"/><text x="140" y="30">D₂</text></g><g class="nd"><circle cx="240" cy="30" r="14"/><text x="240" y="30">D₃</text></g><g class="nd"><circle cx="40" cy="150" r="14"/><text x="40" y="150">S₁</text></g><g class="nd"><circle cx="140" cy="150" r="14"/><text x="140" y="150">S₂</text></g><g class="nd"><circle cx="240" cy="150" r="14"/><text x="240" y="150">S₃</text></g></svg></div>

::: drill dg-specialne

::: quiz
Ktorý graf je bipartitný?
- [ ] $K_3$
- [ ] $C_5$
- [x] $C_4$
> V $C_4$ dáme protiľahlé vrcholy do tej istej skupiny. $K_3$ aj $C_5$ obsahujú nepárny cyklus.
:::

## Prechádzky, cesty a ťahy

**Prechádzka** (sled, walk) je postupnosť vrchol, hrana, vrchol, hrana, … v ktorej každá hrana spája susedné vrcholy postupnosti. Z prechádzky sa ďalšími podmienkami stávajú:

| názov | podmienka | uzavretá verzia |
|---|---|---|
| **cesta** (path) | neopakuje sa žiadny vrchol | **cyklus** (cycle) |
| **ťah** (trail) | neopakuje sa žiadna hrana | **okruh** (circuit) |

Uzavretá znamená, že prvý vrchol je zároveň posledný. Každá cesta je aj ťah (bez opakovaného vrchola sa nemôže zopakovať ani hrana), opačne to neplatí. Názvy sa v knihách líšia, preto sa oplatí pamätať si anglické termíny z prednášky.

<div class="graph"><svg viewBox="0 0 200 185" width="200" role="img" aria-label="graf"><defs><marker id="ga19" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M161.7,91.3 Q153.5,117 145.9,140.8" marker-end="url(#ga19)"/><path class="ed c1" d="M136.7,142.7 Q120.5,93 105,45.2" marker-end="url(#ga19)"/><path class="ed c1" d="M95.7,43.3 Q79.5,93 64,140.8" marker-end="url(#ga19)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga19)"/><path class="ed dim" d="M111.3,38.2 Q133,54 154.7,69.8"/><path class="ed dim" d="M45.3,69.8 Q67,54 88.7,38.2"/><g class="nd"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd on"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="145.5" y="105.8">1</text><text class="el" x="135.1" y="102.2">2</text><text class="el" x="73.1" y="77">3</text><text class="el" x="59.5" y="121.4">4</text></svg><svg viewBox="0 0 200 185" width="200" role="img" aria-label="graf"><defs><marker id="ga20" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M161.7,91.3 Q153.5,117 145.9,140.8" marker-end="url(#ga20)"/><path class="ed c1" d="M136.7,142.7 Q120.5,93 105,45.2" marker-end="url(#ga20)"/><path class="ed c1" d="M95.7,43.3 Q79.5,93 64,140.8" marker-end="url(#ga20)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga20)"/><path class="ed c1" d="M45.3,69.8 Q67,54 87.1,39.4" marker-end="url(#ga20)"/><path class="ed dim" d="M111.3,38.2 Q133,54 154.7,69.8"/><g class="nd"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd on"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="145.5" y="105.8">1</text><text class="el" x="135.1" y="102.2">2</text><text class="el" x="73.1" y="77">3</text><text class="el" x="59.5" y="121.4">4</text><text class="el" x="66.9" y="67.7">5</text></svg><svg viewBox="0 0 200 185" width="200" role="img" aria-label="graf"><defs><marker id="ga21" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M95.7,43.3 Q79.5,93 64,140.8" marker-end="url(#ga21)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga21)"/><path class="ed c1" d="M45.3,69.8 Q67,54 87.1,39.4" marker-end="url(#ga21)"/><path class="ed dim" d="M111.3,38.2 Q133,54 154.7,69.8"/><path class="ed dim" d="M161.7,91.3 Q153.5,117 145.3,142.7"/><path class="ed dim" d="M136.7,142.7 Q120.5,93 104.3,43.3"/><g class="nd on"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="73.1" y="77">1</text><text class="el" x="59.5" y="121.4">2</text><text class="el" x="66.9" y="67.7">3</text></svg><svg viewBox="0 0 200 185" width="200" role="img" aria-label="graf"><defs><marker id="ga22" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M111.3,38.2 Q133,54 153.1,68.6" marker-end="url(#ga22)"/><path class="ed c1" d="M161.7,91.3 Q153.5,117 145.9,140.8" marker-end="url(#ga22)"/><path class="ed c1" d="M136.7,142.7 Q120.5,93 105,45.2" marker-end="url(#ga22)"/><path class="ed c1" d="M95.7,43.3 Q79.5,93 64,140.8" marker-end="url(#ga22)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga22)"/><path class="ed c1" d="M45.3,69.8 Q67,54 87.1,39.4" marker-end="url(#ga22)"/><g class="nd on"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="119.9" y="58.1">1</text><text class="el" x="145.5" y="105.8">2</text><text class="el" x="135.1" y="102.2">3</text><text class="el" x="73.1" y="77">4</text><text class="el" x="59.5" y="121.4">5</text><text class="el" x="66.9" y="67.7">6</text></svg></div>

Na „motýliku“ zľava: cesta $B, C, A, D, E$; ťah $B, C, A, D, E, A$ (vrchol $A$ dvakrát); cyklus $A, D, E, A$; okruh $A, B, C, A, D, E, A$, ktorý nie je cyklom, lebo $A$ sa zopakuje aj vnútri.

**Súvislý graf:** z každého vrchola vedie prechádzka do každého iného.

::: drill dg-prechadzky

::: quiz
Postupnosť $A, B, C, A, D$ s hranami $AB$, $BC$, $CA$, $AD$ je
- [ ] cesta
- [x] ťah, ale nie cesta
- [ ] okruh
> Hrany sa neopakujú, vrchol $A$ áno. Prvý a posledný vrchol sa líšia, takže nie je uzavretá.
:::

## Eulerovské grafy

Úloha siedmich mostov hľadá **okruh, ktorý prejde každú hranu práve raz**: eulerovský okruh.

**Veta.** Graf je **eulerovský** (má eulerovský okruh) práve vtedy, keď je súvislý a **všetky** vrcholy majú párny stupeň.

**Veta.** Graf je **semieulerovský** (má otvorený ťah cez všetky hrany) práve vtedy, keď je súvislý a **presne dva** vrcholy majú nepárny stupeň. Ťah začína v jednom z nich a končí v druhom.

| súvislý graf, vrcholov nepárneho stupňa | typ | čo existuje |
|---|---|---|
| 0 | eulerovský | okruh, štart kdekoľvek |
| 2 | semieulerovský | ťah z jedného nepárneho vrchola do druhého |
| 4, 6, … | ani jedno | jedným ťahom sa graf nakresliť nedá |

Königsberg má stupne $5, 3, 3, 3$, teda štyri nepárne vrcholy: nedá sa. Rovnako $K_4$ (všetky stupne 3).

::: drill dg-euler

::: quiz
Súvislý graf má stupne $3, 2, 2, 3, 4$. Čo platí?
- [ ] je eulerovský
- [ ] je semieulerovský a ťah môže začať kdekoľvek
- [x] je semieulerovský a ťah začína vo vrchole stupňa 3
> Nepárne sú presne dva vrcholy, ťah musí začať v jednom z nich.
:::

## Fleuryho algoritmus

Vstup: súvislý graf s 0 alebo 2 nepárnymi vrcholmi.

1. Začnite v ľubovoľnom vrchole (eulerovský graf) alebo v jednom z nepárnych vrcholov (semieulerovský graf).
2. Vyberte nepoužitú hranu z aktuálneho vrchola tak, aby zvyšok nepoužitých hrán ostal súvislý.
3. Prejdite po nej a vymažte ju.
4. Opakujte, kým neminiete všetky hrany.

Pravidlo **„nespáľ si most“**: hranu, po ktorej odstránení by sa zvyšok rozpadol, vyberte len vtedy, keď iná možnosť nie je.

Príklad: domček má stupne $\deg A = \deg B = 3$, $\deg C = \deg D = 4$, $\deg E = 2$. Nepárne sú $A$ a $B$, takže graf je semieulerovský a ťah začneme v $A$:

<div class="graph"><svg viewBox="0 0 200 215" width="200" role="img" aria-label="graf"><defs><marker id="ga24" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M54,190 Q100,190 144,190" marker-end="url(#ga24)"/><path class="ed c1" d="M149.2,181 Q100,140 52.3,100.2" marker-end="url(#ga24)"/><path class="ed c1" d="M40,104 Q40,140 40,174" marker-end="url(#ga24)"/><path class="ed c1" d="M50.8,181 Q100,140 147.7,100.2" marker-end="url(#ga24)"/><path class="ed c1" d="M146,90 Q100,90 56,90" marker-end="url(#ga24)"/><path class="ed c1" d="M49.5,79.7 Q70,57.5 89.1,36.8" marker-end="url(#ga24)"/><path class="ed c1" d="M109.5,35.3 Q130,57.5 149.1,78.2" marker-end="url(#ga24)"/><path class="ed c1" d="M160,104 Q160,140 160,174" marker-end="url(#ga24)"/><g class="nd on"><circle cx="40" cy="190" r="14"/><text x="40" y="190">A</text></g><g class="nd"><circle cx="160" cy="190" r="14"/><text x="160" y="190">B</text></g><g class="nd"><circle cx="40" cy="90" r="14"/><text x="40" y="90">C</text></g><g class="nd"><circle cx="160" cy="90" r="14"/><text x="160" y="90">D</text></g><g class="nd"><circle cx="100" cy="25" r="14"/><text x="100" y="25">E</text></g><text class="el" x="88" y="201">1</text><text class="el" x="119" y="141.5">2</text><text class="el" x="29" y="130">3</text><text class="el" x="95" y="158.5">4</text><text class="el" x="112" y="79">5</text><text class="el" x="72.1" y="71.5">6</text><text class="el" x="115.9" y="58.5">7</text><text class="el" x="149" y="130">8</text></svg></div>

Výsledok: $A, B, C, A, D, C, E, D, B$, všetkých 8 hrán. Iné rozhodnutia v kroku 2 dajú iný, rovnako správny ťah.

::: quiz
Fleuryho algoritmus vyberie most
- [ ] vždy, keď je to možné
- [x] len vtedy, keď z aktuálneho vrchola nevedie iná nepoužitá hrana
- [ ] nikdy
> Prejdenie mosta zbytočne skôr by odrezalo hrany, ku ktorým sa už nevrátime.
:::

## Hierholzerov algoritmus

Vstup: súvislý eulerovský graf. Netreba v každom kroku hľadať mosty, preto je rýchlejší.

1. Z ľubovoľného vrchola nájdite nejaký okruh (stačí ísť, kým sa nezaseknete, v eulerovskom grafe sa zaseknete len v štarte).
2. Ak má niektorý vrchol $X$ okruhu ešte nepoužité hrany, nájdite z $X$ ďalší okruh z nepoužitých hrán.
3. Vložte nový okruh do starého na miesto vrchola $X$.
4. Opakujte, kým nie sú použité všetky hrany.

Príklad: $K_5$ je súvislý a všetky stupne sú 4, takže je eulerovský (10 hrán). Prvý okruh je obvod $A, B, C, D, E, A$ (hrany 1–5). Vrchol $A$ má ešte nepoužité hrany, druhý okruh je „hviezda“ $A, C, E, B, D, A$ (hrany 6–10). Po vložení na miesto $A$:
$$A, B, C, D, E, A, C, E, B, D, A$$

<div class="graph"><svg viewBox="0 0 206 196" width="206" role="img" aria-label="graf"><defs><marker id="ga27" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M111.3,38.2 Q133,54 153.1,68.6" marker-end="url(#ga27)"/><path class="ed c1" d="M161.7,91.3 Q153.5,117 145.9,140.8" marker-end="url(#ga27)"/><path class="ed c1" d="M127,156 Q100,156 75,156" marker-end="url(#ga27)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga27)"/><path class="ed c1" d="M45.3,69.8 Q67,54 87.1,39.4" marker-end="url(#ga27)"/><path class="ed c2" d="M104.3,43.3 Q120.5,93 136,140.8" marker-end="url(#ga27)"/><path class="ed c2" d="M129.7,147.8 Q87.5,117 46.9,87.4" marker-end="url(#ga27)"/><path class="ed c2" d="M48,78 Q100,78 150,78" marker-end="url(#ga27)"/><path class="ed c2" d="M154.7,86.2 Q112.5,117 71.9,146.6" marker-end="url(#ga27)"/><path class="ed c2" d="M63.3,142.7 Q79.5,93 95,45.2" marker-end="url(#ga27)"/><g class="nd on"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="119.9" y="58.1">1</text><text class="el" x="145.5" y="105.8">2</text><text class="el" x="108.2" y="145">3</text><text class="el" x="59.5" y="121.4">4</text><text class="el" x="66.9" y="67.7">5</text><text class="el" x="105.9" y="83.8">6</text><text class="el" x="104.7" y="115.9">7</text><text class="el" x="86.8" y="89">8</text><text class="el" x="116.7" y="100.3">9</text><text class="el" x="85.9" y="109">10</text></svg></div>

Na cvičení: v grafe nižšie začneme v $A$ okruhom $A, B, C, A$, potom pridáme $A, G, F, A$, z $G$ okruh $G, C, D, G$ a z $D$ okruh $D, F, E, D$. Výsledok: $A, B, C, A, G, C, D, F, E, D, G, F, A$.

<div class="graph"><svg viewBox="0 0 430 235" width="430" role="img" aria-label="graf"><defs><marker id="ga26" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M139.1,48.7 Q100,80 60.9,111.3"/><path class="ed" d="M58.4,131.2 Q80,160 101.6,188.8"/><path class="ed" d="M113.4,186.4 Q130,120 146.6,53.6"/><path class="ed" d="M164,40 Q220,40 276,40"/><path class="ed" d="M300.9,48.7 Q340,80 379.1,111.3"/><path class="ed" d="M376.7,115.6 Q270,80 163.3,44.4"/><path class="ed" d="M279.5,49.3 Q200,120 120.5,190.7"/><path class="ed" d="M124,200 Q175,200 226,200"/><path class="ed" d="M244.2,186.6 Q265,120 285.8,53.4"/><path class="ed" d="M252.4,193.4 Q315,160 377.6,126.6"/><path class="ed" d="M383.7,132.5 Q370,160 356.3,187.5"/><path class="ed" d="M336,200 Q295,200 254,200"/><g class="nd"><circle cx="150" cy="40" r="14"/><text x="150" y="40">A</text></g><g class="nd"><circle cx="290" cy="40" r="14"/><text x="290" y="40">G</text></g><g class="nd"><circle cx="50" cy="120" r="14"/><text x="50" y="120">B</text></g><g class="nd"><circle cx="390" cy="120" r="14"/><text x="390" y="120">F</text></g><g class="nd"><circle cx="110" cy="200" r="14"/><text x="110" y="200">C</text></g><g class="nd"><circle cx="240" cy="200" r="14"/><text x="240" y="200">D</text></g><g class="nd"><circle cx="350" cy="200" r="14"/><text x="350" y="200">E</text></g></svg></div>

::: quiz
Koľko hrán má eulerovský okruh grafu $K_7$?
- [ ] 7
- [ ] 14
- [x] 21
> Eulerovský okruh prejde každú hranu raz: $\frac{7\cdot6}{2} = 21$. $K_7$ je eulerovský, všetky stupne sú 6.
:::

## Slovník

| slovensky | anglicky |
|---|---|
| vrchol, hrana | vertex, edge |
| susedné vrcholy | adjacent vertices |
| násobné hrany, slučka | multiple edges, loop |
| stupeň, rád, veľkosť | degree, order, size |
| úplný, bipartitný, planárny graf | complete, bipartite, planar graph |
| doplnok | complement |
| prechádzka, cesta, ťah | walk, path, trail |
| okruh, cyklus | circuit, cycle |
| súvislý graf, most | connected graph, bridge |

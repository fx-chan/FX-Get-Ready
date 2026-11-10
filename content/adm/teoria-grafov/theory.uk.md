> Джерело: конспект лекції та практичних занять. Підручник Антона–Рорреса теорію графів не охоплює, тому тут тримаємося понять із лекції.

## Сім мостів

Теорія графів — **не** малювання графіків функцій $y = f(x)$. Це розділ дискретної математики про об'єкти (вершини) та зв'язки між ними (ребра).

Вона почалася 1736 року задачею, яку розв'язував Леонард Ейлер. Місто Кенігсберг ділила річка з двома островами, а чотири частини міста з'єднували сім мостів. Чи можна пройти кожен міст рівно один раз і повернутися на старт? Ейлер помітив, що форма міста не має значення: частини міста — це вершини, мости — ребра, і важливо лише те, що з чим пов'язане.

<div class="graph"><svg viewBox="0 0 330 240" width="330" role="img" aria-label="graf"><defs><marker id="ga1" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M108,114.9 Q156.6,95.9 151.4,43.9"/><path class="ed" d="M93.6,106.1 Q88.4,54.1 137,35.1"/><path class="ed" d="M93.6,133.9 Q88.4,185.9 137,204.9"/><path class="ed" d="M108,125.1 Q156.6,144.1 151.4,196.1"/><path class="ed" d="M109,120 Q192.5,120 276,120"/><path class="ed" d="M161.8,37.6 Q220,75 278.2,112.4"/><path class="ed" d="M161.8,202.4 Q220,165 278.2,127.6"/><g class="nd"><circle cx="150" cy="30" r="14"/><text x="150" y="30">C</text></g><text class="dg" x="172" y="14">3</text><g class="nd"><circle cx="95" cy="120" r="14"/><text x="95" y="120">A</text></g><text class="dg" x="69" y="120">5</text><g class="nd"><circle cx="150" cy="210" r="14"/><text x="150" y="210">B</text></g><text class="dg" x="172" y="230">3</text><g class="nd"><circle cx="290" cy="120" r="14"/><text x="290" y="120">D</text></g><text class="dg" x="314" y="104">3</text></svg></div>

Числа біля вершин — це степені. Наприкінці уроку побачите, чому відповідь **ні**: усі чотири вершини мають непарний степінь.

## Граф, порядок і розмір

**Граф** — це пара $G = (V, E)$: $V$ — множина вершин, $E$ — множина ребер. Пишемо також $V(G)$, $E(G)$. У неорієнтованому графі ребро позначаємо його кінцями, і порядок не важливий: $AD = DA$.

<div class="graph"><svg viewBox="0 0 340 220" width="340" role="img" aria-label="graf"><defs><marker id="ga2" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M181.9,37.3 Q235,70 288.1,102.7"/><path class="ed" d="M181.9,182.7 Q235,150 288.1,117.3"/><path class="ed" d="M170,44 Q170,110 170,176"/><path class="ed" d="M158.1,37.3 Q105,70 51.9,102.7"/><path class="ed" d="M51.9,117.3 Q105,150 158.1,182.7"/><g class="nd"><circle cx="170" cy="30" r="14"/><text x="170" y="30">A</text></g><g class="nd"><circle cx="40" cy="110" r="14"/><text x="40" y="110">B</text></g><g class="nd"><circle cx="300" cy="110" r="14"/><text x="300" y="110">D</text></g><g class="nd"><circle cx="170" cy="190" r="14"/><text x="170" y="190">C</text></g><text class="el" x="229.2" y="79.4">h₁</text><text class="el" x="229.2" y="140.6">h₂</text><text class="el" x="159" y="110">h₃</text><text class="el" x="110.8" y="79.4">h₄</text><text class="el" x="99.2" y="159.4">h₅</text></svg></div>

Тут $V = \{A, B, C, D\}$ і $E = \{AD, CD, AC, AB, BC\}$.

- **порядок** $\operatorname{order}(G) = |V|$ — кількість вершин (тут 4),
- **розмір** $\operatorname{size}(G) = |E|$ — кількість ребер (тут 5).

Що ще є графом: одна вершина без ребер $(\{A\}, \emptyset)$ — так, за лекцією також $(\emptyset, \emptyset)$. Ребро з вільним кінцем — ні: ребро завжди з'єднує дві вершини (петля — ту саму двічі). Той самий граф можна намалювати рівно або «заплутано», це все одно той самий граф.

::: drill dg-rad-velkost

## Вершини й ребра

- **Інцидентність:** ребро $h = \{u, v\}$ інцидентне вершинам $u$ і $v$ (і навпаки).
- **Суміжні вершини** — вершини, з'єднані ребром.
- **Кратні ребра:** дві вершини з'єднує більше ніж одне ребро.
- **Петля:** ребро, яке починається й закінчується в тій самій вершині.
- **Ізольована вершина** не інцидентна жодному ребру. Вершина, яка має лише петлю, **не** ізольована.

<div class="graph"><svg viewBox="0 0 290 260" width="290" role="img" aria-label="graf"><defs><marker id="ga3" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M49.6,99.8 Q122.8,22.5 226.4,46.8"/><path class="ed" d="M53.4,106 Q140,80 226.6,54"/><path class="ed" d="M53.6,113.2 Q157.2,137.5 230.4,60.2"/><path class="ed" d="M235.7,63.3 Q220,112.5 204.3,161.7"/><path class="ed c3" d="M206.1,187.6 C234.8,212.3 165.2,212.3 193.9,187.6"/><g class="nd"><circle cx="40" cy="110" r="14"/><text x="40" y="110">A</text></g><g class="nd"><circle cx="240" cy="50" r="14"/><text x="240" y="50">B</text></g><g class="nd"><circle cx="200" cy="175" r="14"/><text x="200" y="175">C</text></g><text class="el" x="128.2" y="40.7">h₁</text><text class="el" x="113.2" y="99.5">h₂</text><text class="el" x="151.8" y="119.3">h₃</text><text class="el" x="209.5" y="109.1">h₄</text><text class="el" x="200" y="225.5">h₅</text></svg><svg viewBox="0 0 330 190" width="330" role="img" aria-label="graf"><defs><marker id="ga4" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M53.9,108.5 Q119.2,101.4 161.1,50.8"/><path class="ed" d="M48.9,99.2 Q90.8,48.6 156.1,41.5"/><path class="ed" d="M262.6,103.9 C287.3,75.2 287.3,144.8 262.6,116.1"/><g class="nd"><circle cx="40" cy="110" r="14"/><text x="40" y="110">A</text></g><g class="nd"><circle cx="170" cy="40" r="14"/><text x="170" y="40">B</text></g><g class="nd iso"><circle cx="110" cy="160" r="14"/><text x="110" y="160">C</text></g><g class="nd"><circle cx="250" cy="110" r="14"/><text x="250" y="110">D</text></g></svg></div>

Ліворуч: від $h_1$ до $h_3$ — кратні ребра, $h_5$ — петля, порядок 3 і розмір 5. Праворуч $C$ ізольована, $D$ з петлею — ні.

::: quiz
Вершина має лише петлю й жодного іншого ребра. Вона ізольована?
- [ ] так
- [x] ні
> Ізольована вершина не має жодного інцидентного ребра. Петля інцидентна й дає степінь 2.
:::

## Типи графів

| тип | петлі | кратні ребра |
|---|---|---|
| псевдограф | можуть бути | можуть бути |
| мультиграф | ні | можуть бути |
| простий (звичайний) граф | ні | ні |
| тривіальний граф | немає навіть ребер | немає навіть ребер |

Деякі підручники називають тривіальним лише граф з однією вершиною, а граф без ребер — порожнім. На іспиті використовуйте означення з лекції.

**Орієнтований граф (орграф):** кожне ребро має напрям. Ребро $AB$ іде з $A$ до $B$, тому тут $AB \ne BA$.

<div class="graph"><svg viewBox="0 0 240 180" width="240" role="img" aria-label="graf"><defs><marker id="ga5" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M50.7,86 Q109.5,36.6 184,31.2" marker-end="url(#ga5)"/><path class="ed" d="M189.3,39 Q130.5,88.4 56,93.8" marker-end="url(#ga5)"/><path class="ed" d="M53.2,99.6 Q120,122.5 184.9,144.8" marker-end="url(#ga5)"/><g class="nd"><circle cx="40" cy="95" r="14"/><text x="40" y="95">A</text></g><g class="nd"><circle cx="200" cy="30" r="14"/><text x="200" y="30">B</text></g><g class="nd"><circle cx="200" cy="150" r="14"/><text x="200" y="150">C</text></g><text class="el" x="110.6" y="39.3">h₁</text><text class="el" x="129.4" y="85.7">h₂</text><text class="el" x="116.4" y="132.9">h₃</text></svg></div>

## Степінь вершини

**Степінь** $\deg v$ — кількість ребер, інцидентних $v$, причому **петля рахується двічі**.

**Теорема про суму степенів:** $$\sum_{v \in V} \deg v = 2|E|$$ Кожне ребро додає одиницю кожному зі своїх двох кінців.

**Наслідок:** вершин непарного степеня завжди парна кількість. Якщо сума заданих степенів непарна, графа не існує.

<div class="graph"><svg viewBox="0 0 340 230" width="340" role="img" aria-label="graf"><defs><marker id="ga31" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M46.4,187.5 Q68,145 46.4,102.5"/><path class="ed" d="M33.6,187.5 Q12,145 33.6,102.5"/><path class="ed" d="M54,90 Q105,90 156,90"/><path class="ed" d="M163.9,77.4 C135.2,52.7 204.8,52.7 176.1,77.4"/><path class="ed" d="M170,104 Q170,145 170,186"/><path class="ed" d="M54,200 Q105,200 156,200"/><path class="ed" d="M184,200 Q235,200 286,200"/><g class="nd"><circle cx="40" cy="90" r="14"/><text x="40" y="90">B</text></g><text class="dg" x="60" y="73">3</text><g class="nd"><circle cx="170" cy="90" r="14"/><text x="170" y="90">C</text></g><text class="dg" x="190" y="73">4</text><g class="nd iso"><circle cx="300" cy="90" r="14"/><text x="300" y="90">F</text></g><text class="dg" x="320" y="73">0</text><g class="nd"><circle cx="40" cy="200" r="14"/><text x="40" y="200">A</text></g><text class="dg" x="60" y="183">3</text><g class="nd"><circle cx="170" cy="200" r="14"/><text x="170" y="200">D</text></g><text class="dg" x="190" y="183">3</text><g class="nd"><circle cx="300" cy="200" r="14"/><text x="300" y="200">E</text></g><text class="dg" x="320" y="183">1</text></svg></div>

Сума $3 + 3 + 4 + 3 + 1 + 0 = 14 = 2\cdot 7$.

**Регулярний ($k$-регулярний) граф:** усі вершини мають степінь $k$, отже $|E| = \frac{nk}{2}$.

::: drill dg-stupne

::: drill dg-existencia

**Увага:** парної суми замало. У простому графі з $n$ вершинами степінь щонайбільше $n - 1$. Наприклад, степені $3, 3, 3, 1$ мають суму 10, але в простому графі з 4 вершинами степінь 3 означає ребро до всіх інших, тож четверта вершина мала б степінь щонайменше 3.

::: quiz
Граф має 7 ребер. Чому дорівнює сума степенів його вершин?
- [ ] 7
- [x] 14
- [ ] залежить від кількості вершин
> $\sum\deg v = 2|E| = 14$ незалежно від кількості вершин.
:::

::: quiz
Чи існує простий граф з 5 вершинами, у якому кожна вершина має степінь 3?
- [ ] так
- [x] ні
> Сума $5\cdot3 = 15$ непарна, тож мало б бути $|E| = 7{,}5$.
:::

## Особливі графи

**Повний граф** $K_n$: кожні дві вершини з'єднує рівно одне ребро. Кожна вершина має степінь $n - 1$ і $$|E(K_n)| = \frac{n(n-1)}{2}$$

<div class="graph"><svg viewBox="0 0 60 60" width="60" role="img" aria-label="graf"><defs><marker id="ga6" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><g class="nd"><circle cx="30" cy="30" r="14"/><text x="30" y="30">A</text></g></svg><svg viewBox="0 0 130 110" width="130" role="img" aria-label="graf"><defs><marker id="ga7" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M41.4,71.9 Q65,55 88.6,38.1"/><g class="nd"><circle cx="30" cy="80" r="14"/><text x="30" y="80">A</text></g><g class="nd"><circle cx="100" cy="30" r="14"/><text x="100" y="30">B</text></g></svg><svg viewBox="0 0 160 150" width="160" role="img" aria-label="graf"><defs><marker id="ga8" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M73.2,42.2 Q55,75 36.8,107.8"/><path class="ed" d="M86.8,42.2 Q105,75 123.2,107.8"/><path class="ed" d="M44,120 Q80,120 116,120"/><g class="nd"><circle cx="80" cy="30" r="14"/><text x="80" y="30">A</text></g><g class="nd"><circle cx="30" cy="120" r="14"/><text x="30" y="120">B</text></g><g class="nd"><circle cx="130" cy="120" r="14"/><text x="130" y="120">C</text></g></svg><svg viewBox="0 0 170 170" width="170" role="img" aria-label="graf"><defs><marker id="ga9" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M44,30 Q80,30 116,30"/><path class="ed" d="M39.9,39.9 Q80,80 120.1,120.1"/><path class="ed" d="M30,44 Q30,80 30,116"/><path class="ed" d="M130,44 Q130,80 130,116"/><path class="ed" d="M120.1,39.9 Q80,80 39.9,120.1"/><path class="ed" d="M116,130 Q80,130 44,130"/><g class="nd"><circle cx="30" cy="30" r="14"/><text x="30" y="30">A</text></g><g class="nd"><circle cx="130" cy="30" r="14"/><text x="130" y="30">B</text></g><g class="nd"><circle cx="130" cy="130" r="14"/><text x="130" y="130">C</text></g><g class="nd"><circle cx="30" cy="130" r="14"/><text x="30" y="130">D</text></g></svg><svg viewBox="0 0 206 196" width="206" role="img" aria-label="graf"><defs><marker id="ga10" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M111.3,38.2 Q133,54 154.7,69.8"/><path class="ed" d="M104.3,43.3 Q120.5,93 136.7,142.7"/><path class="ed" d="M95.7,43.3 Q79.5,93 63.3,142.7"/><path class="ed" d="M88.7,38.2 Q67,54 45.3,69.8"/><path class="ed" d="M161.7,91.3 Q153.5,117 145.3,142.7"/><path class="ed" d="M154.7,86.2 Q112.5,117 70.3,147.8"/><path class="ed" d="M152,78 Q100,78 48,78"/><path class="ed" d="M127,156 Q100,156 73,156"/><path class="ed" d="M129.7,147.8 Q87.5,117 45.3,86.2"/><path class="ed" d="M54.7,142.7 Q46.5,117 38.3,91.3"/><g class="nd"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g></svg></div>

**Доповнення** $\bar G$ має ті самі вершини й саме ті ребра, яких бракує в $G$. Разом вони дають $K_n$, тож $|E(\bar G)| = \frac{n(n-1)}{2} - |E(G)|$.

<div class="graph"><svg viewBox="0 0 170 150" width="170" role="img" aria-label="graf"><defs><marker id="ga14" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c3" d="M37.3,108.1 Q57.5,75 77.7,41.9"/><g class="nd"><circle cx="30" cy="120" r="14"/><text x="30" y="120">A</text></g><g class="nd iso"><circle cx="140" cy="120" r="14"/><text x="140" y="120">B</text></g><g class="nd"><circle cx="85" cy="30" r="14"/><text x="85" y="30">C</text></g></svg><svg viewBox="0 0 170 150" width="170" role="img" aria-label="graf"><defs><marker id="ga15" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c2" d="M44,120 Q85,120 126,120"/><path class="ed c2" d="M132.7,108.1 Q112.5,75 92.3,41.9"/><g class="nd"><circle cx="30" cy="120" r="14"/><text x="30" y="120">A</text></g><g class="nd"><circle cx="140" cy="120" r="14"/><text x="140" y="120">B</text></g><g class="nd"><circle cx="85" cy="30" r="14"/><text x="85" y="30">C</text></g></svg></div>

Ці два графи на трьох вершинах є доповненнями один одного: разом утворюють $K_3$.

**Дводольний граф:** вершини можна розбити на дві групи $V_1$, $V_2$ так, що кожне ребро йде між групами. **Повний дводольний** $K_{m,n}$ з'єднує кожну вершину з $V_1$ з кожною з $V_2$, має $mn$ ребер. Корисний критерій: граф дводольний тоді й лише тоді, коли не має циклу непарної довжини. Граф із петлею ніколи не буває дводольним.

<div class="graph"><svg viewBox="0 0 220 170" width="220" role="img" aria-label="graf"><defs><marker id="ga16" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M56.3,43.5 Q45,85 33.7,126.5"/><path class="ed" d="M65.8,42.7 Q85,85 104.2,127.3"/><path class="ed" d="M70.7,39 Q125,85 179.3,131"/><path class="ed" d="M149.3,39 Q95,85 40.7,131"/><path class="ed" d="M154.2,42.7 Q135,85 115.8,127.3"/><path class="ed" d="M163.7,43.5 Q175,85 186.3,126.5"/><g class="nd"><circle cx="60" cy="30" r="14"/><text x="60" y="30">A₁</text></g><g class="nd"><circle cx="160" cy="30" r="14"/><text x="160" y="30">A₂</text></g><g class="nd"><circle cx="30" cy="140" r="14"/><text x="30" y="140">B₁</text></g><g class="nd"><circle cx="110" cy="140" r="14"/><text x="110" y="140">B₂</text></g><g class="nd"><circle cx="190" cy="140" r="14"/><text x="190" y="140">B₃</text></g></svg></div>

**Планарний граф** можна намалювати на площині без перетинів ребер. Задача про три будинки й три джерела, де кожен будинок треба з'єднати з кожним джерелом, — це граф $K_{3,3}$, і він не планарний. $K_5$ теж не планарний. $K_4$ планарний, тільки його треба намалювати інакше:

<div class="graph"><svg viewBox="0 0 170 170" width="170" role="img" aria-label="graf"><defs><marker id="ga11" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M44,30 Q80,30 116,30"/><path class="ed" d="M39.9,39.9 Q80,80 120.1,120.1"/><path class="ed" d="M30,44 Q30,80 30,116"/><path class="ed" d="M130,44 Q130,80 130,116"/><path class="ed" d="M120.1,39.9 Q80,80 39.9,120.1"/><path class="ed" d="M116,130 Q80,130 44,130"/><g class="nd"><circle cx="30" cy="30" r="14"/><text x="30" y="30">A</text></g><g class="nd"><circle cx="130" cy="30" r="14"/><text x="130" y="30">B</text></g><g class="nd"><circle cx="130" cy="130" r="14"/><text x="130" y="130">C</text></g><g class="nd"><circle cx="30" cy="130" r="14"/><text x="30" y="130">D</text></g></svg><svg viewBox="0 0 160 155" width="160" role="img" aria-label="graf"><defs><marker id="ga12" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M73.5,37.4 Q52.5,77.5 31.5,117.6"/><path class="ed" d="M86.5,37.4 Q107.5,77.5 128.5,117.6"/><path class="ed" d="M80,39 Q80,58.5 80,78"/><path class="ed" d="M39,130 Q80,130 121,130"/><path class="ed" d="M36.5,122 Q52.5,111 68.5,100"/><path class="ed" d="M123.5,122 Q107.5,111 91.5,100"/><g class="nd"><circle cx="80" cy="25" r="14"/><text x="80" y="25">A</text></g><g class="nd"><circle cx="25" cy="130" r="14"/><text x="25" y="130">B</text></g><g class="nd"><circle cx="135" cy="130" r="14"/><text x="135" y="130">C</text></g><g class="nd"><circle cx="80" cy="92" r="14"/><text x="80" y="92">D</text></g></svg></div>

<div class="graph"><svg viewBox="0 0 280 180" width="280" role="img" aria-label="graf"><defs><marker id="ga13" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M40,44 Q40,90 40,136"/><path class="ed" d="M49,40.8 Q90,90 131,139.2"/><path class="ed" d="M52,37.2 Q140,90 228,142.8"/><path class="ed" d="M131,40.8 Q90,90 49,139.2"/><path class="ed" d="M140,44 Q140,90 140,136"/><path class="ed" d="M149,40.8 Q190,90 231,139.2"/><path class="ed" d="M228,37.2 Q140,90 52,142.8"/><path class="ed" d="M231,40.8 Q190,90 149,139.2"/><path class="ed" d="M240,44 Q240,90 240,136"/><g class="nd"><circle cx="40" cy="30" r="14"/><text x="40" y="30">D₁</text></g><g class="nd"><circle cx="140" cy="30" r="14"/><text x="140" y="30">D₂</text></g><g class="nd"><circle cx="240" cy="30" r="14"/><text x="240" y="30">D₃</text></g><g class="nd"><circle cx="40" cy="150" r="14"/><text x="40" y="150">S₁</text></g><g class="nd"><circle cx="140" cy="150" r="14"/><text x="140" y="150">S₂</text></g><g class="nd"><circle cx="240" cy="150" r="14"/><text x="240" y="150">S₃</text></g></svg></div>

::: drill dg-specialne

::: quiz
Який граф дводольний?
- [ ] $K_3$
- [ ] $C_5$
- [x] $C_4$
> У $C_4$ протилежні вершини кладемо в одну групу. $K_3$ і $C_5$ містять непарний цикл.
:::

## Маршрути, шляхи й ланцюги

**Маршрут** (walk) — послідовність вершина, ребро, вершина, ребро, … у якій кожне ребро з'єднує сусідні вершини послідовності. Додатковими умовами з маршруту отримуємо:

| назва | умова | замкнена версія |
|---|---|---|
| **шлях** (path) | жодна вершина не повторюється | **цикл** (cycle) |
| **ланцюг** (trail) | жодне ребро не повторюється | **замкнений ланцюг** (circuit) |

Замкнений означає, що перша вершина водночас і остання. Кожен шлях є й ланцюгом (без повторення вершини не може повторитися й ребро), навпаки — ні. Назви в підручниках різняться, тому варто пам'ятати англійські терміни з лекції.

<div class="graph"><svg viewBox="0 0 200 185" width="200" role="img" aria-label="graf"><defs><marker id="ga19" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M161.7,91.3 Q153.5,117 145.9,140.8" marker-end="url(#ga19)"/><path class="ed c1" d="M136.7,142.7 Q120.5,93 105,45.2" marker-end="url(#ga19)"/><path class="ed c1" d="M95.7,43.3 Q79.5,93 64,140.8" marker-end="url(#ga19)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga19)"/><path class="ed dim" d="M111.3,38.2 Q133,54 154.7,69.8"/><path class="ed dim" d="M45.3,69.8 Q67,54 88.7,38.2"/><g class="nd"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd on"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="145.5" y="105.8">1</text><text class="el" x="135.1" y="102.2">2</text><text class="el" x="73.1" y="77">3</text><text class="el" x="59.5" y="121.4">4</text></svg><svg viewBox="0 0 200 185" width="200" role="img" aria-label="graf"><defs><marker id="ga20" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M161.7,91.3 Q153.5,117 145.9,140.8" marker-end="url(#ga20)"/><path class="ed c1" d="M136.7,142.7 Q120.5,93 105,45.2" marker-end="url(#ga20)"/><path class="ed c1" d="M95.7,43.3 Q79.5,93 64,140.8" marker-end="url(#ga20)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga20)"/><path class="ed c1" d="M45.3,69.8 Q67,54 87.1,39.4" marker-end="url(#ga20)"/><path class="ed dim" d="M111.3,38.2 Q133,54 154.7,69.8"/><g class="nd"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd on"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="145.5" y="105.8">1</text><text class="el" x="135.1" y="102.2">2</text><text class="el" x="73.1" y="77">3</text><text class="el" x="59.5" y="121.4">4</text><text class="el" x="66.9" y="67.7">5</text></svg><svg viewBox="0 0 200 185" width="200" role="img" aria-label="graf"><defs><marker id="ga21" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M95.7,43.3 Q79.5,93 64,140.8" marker-end="url(#ga21)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga21)"/><path class="ed c1" d="M45.3,69.8 Q67,54 87.1,39.4" marker-end="url(#ga21)"/><path class="ed dim" d="M111.3,38.2 Q133,54 154.7,69.8"/><path class="ed dim" d="M161.7,91.3 Q153.5,117 145.3,142.7"/><path class="ed dim" d="M136.7,142.7 Q120.5,93 104.3,43.3"/><g class="nd on"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="73.1" y="77">1</text><text class="el" x="59.5" y="121.4">2</text><text class="el" x="66.9" y="67.7">3</text></svg><svg viewBox="0 0 200 185" width="200" role="img" aria-label="graf"><defs><marker id="ga22" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M111.3,38.2 Q133,54 153.1,68.6" marker-end="url(#ga22)"/><path class="ed c1" d="M161.7,91.3 Q153.5,117 145.9,140.8" marker-end="url(#ga22)"/><path class="ed c1" d="M136.7,142.7 Q120.5,93 105,45.2" marker-end="url(#ga22)"/><path class="ed c1" d="M95.7,43.3 Q79.5,93 64,140.8" marker-end="url(#ga22)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga22)"/><path class="ed c1" d="M45.3,69.8 Q67,54 87.1,39.4" marker-end="url(#ga22)"/><g class="nd on"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="119.9" y="58.1">1</text><text class="el" x="145.5" y="105.8">2</text><text class="el" x="135.1" y="102.2">3</text><text class="el" x="73.1" y="77">4</text><text class="el" x="59.5" y="121.4">5</text><text class="el" x="66.9" y="67.7">6</text></svg></div>

На «метелику» зліва: шлях $B, C, A, D, E$; ланцюг $B, C, A, D, E, A$ (вершина $A$ двічі); цикл $A, D, E, A$; замкнений ланцюг $A, B, C, A, D, E, A$, який не є циклом, бо $A$ повторюється й усередині.

**Зв'язний граф:** з кожної вершини є маршрут до кожної іншої.

::: drill dg-prechadzky

::: quiz
Послідовність $A, B, C, A, D$ з ребрами $AB$, $BC$, $CA$, $AD$ — це
- [ ] шлях
- [x] ланцюг, але не шлях
- [ ] замкнений ланцюг
> Ребра не повторюються, вершина $A$ — так. Перша й остання вершини різні, тож він не замкнений.
:::

## Ейлерові графи

Задача про сім мостів шукає **замкнений ланцюг, що проходить кожне ребро рівно раз**: ейлерів цикл.

**Теорема.** Граф **ейлерів** (має ейлерів замкнений ланцюг) тоді й лише тоді, коли він зв'язний і **всі** вершини мають парний степінь.

**Теорема.** Граф **напівейлерів** (має відкритий ланцюг через усі ребра) тоді й лише тоді, коли він зв'язний і **рівно дві** вершини мають непарний степінь. Ланцюг починається в одній із них і закінчується в іншій.

| зв'язний граф, вершин непарного степеня | тип | що існує |
|---|---|---|
| 0 | ейлерів | замкнений ланцюг, старт будь-де |
| 2 | напівейлерів | ланцюг з однієї непарної вершини в іншу |
| 4, 6, … | ні те, ні інше | одним розчерком граф намалювати не можна |

Кенігсберг має степені $5, 3, 3, 3$, тобто чотири непарні вершини: не можна. Так само $K_4$ (усі степені 3).

::: drill dg-euler

::: quiz
Зв'язний граф має степені $3, 2, 2, 3, 4$. Що правильно?
- [ ] він ейлерів
- [ ] він напівейлерів, і ланцюг може починатися будь-де
- [x] він напівейлерів, і ланцюг починається у вершині степеня 3
> Непарних вершин рівно дві, ланцюг мусить починатися в одній із них.
:::

## Алгоритм Флері

Вхід: зв'язний граф з 0 або 2 непарними вершинами.

1. Почніть у будь-якій вершині (ейлерів граф) або в одній з непарних вершин (напівейлерів граф).
2. Виберіть невикористане ребро з поточної вершини так, щоб решта невикористаних ребер лишилася зв'язною.
3. Пройдіть ним і видаліть його.
4. Повторюйте, доки не вичерпаєте всі ребра.

Правило **«не спалюй мости»**: ребро, після видалення якого решта розпалася б, вибирайте лише тоді, коли іншого варіанта немає.

Приклад: будиночок має степені $\deg A = \deg B = 3$, $\deg C = \deg D = 4$, $\deg E = 2$. Непарні — $A$ і $B$, отже граф напівейлерів, і ланцюг почнемо в $A$:

<div class="graph"><svg viewBox="0 0 200 215" width="200" role="img" aria-label="graf"><defs><marker id="ga24" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M54,190 Q100,190 144,190" marker-end="url(#ga24)"/><path class="ed c1" d="M149.2,181 Q100,140 52.3,100.2" marker-end="url(#ga24)"/><path class="ed c1" d="M40,104 Q40,140 40,174" marker-end="url(#ga24)"/><path class="ed c1" d="M50.8,181 Q100,140 147.7,100.2" marker-end="url(#ga24)"/><path class="ed c1" d="M146,90 Q100,90 56,90" marker-end="url(#ga24)"/><path class="ed c1" d="M49.5,79.7 Q70,57.5 89.1,36.8" marker-end="url(#ga24)"/><path class="ed c1" d="M109.5,35.3 Q130,57.5 149.1,78.2" marker-end="url(#ga24)"/><path class="ed c1" d="M160,104 Q160,140 160,174" marker-end="url(#ga24)"/><g class="nd on"><circle cx="40" cy="190" r="14"/><text x="40" y="190">A</text></g><g class="nd"><circle cx="160" cy="190" r="14"/><text x="160" y="190">B</text></g><g class="nd"><circle cx="40" cy="90" r="14"/><text x="40" y="90">C</text></g><g class="nd"><circle cx="160" cy="90" r="14"/><text x="160" y="90">D</text></g><g class="nd"><circle cx="100" cy="25" r="14"/><text x="100" y="25">E</text></g><text class="el" x="88" y="201">1</text><text class="el" x="119" y="141.5">2</text><text class="el" x="29" y="130">3</text><text class="el" x="95" y="158.5">4</text><text class="el" x="112" y="79">5</text><text class="el" x="72.1" y="71.5">6</text><text class="el" x="115.9" y="58.5">7</text><text class="el" x="149" y="130">8</text></svg></div>

Результат: $A, B, C, A, D, C, E, D, B$, усі 8 ребер. Інші рішення в кроці 2 дадуть інший, так само правильний ланцюг.

::: quiz
Алгоритм Флері вибирає міст
- [ ] завжди, коли це можливо
- [x] лише тоді, коли з поточної вершини не веде жодне інше невикористане ребро
- [ ] ніколи
> Якщо пройти міст передчасно, відріжемо ребра, до яких уже не повернемося.
:::

## Алгоритм Хірхольцера

Вхід: зв'язний ейлерів граф. Не треба на кожному кроці шукати мости, тому він швидший.

1. З будь-якої вершини знайдіть якийсь замкнений ланцюг (досить іти, доки не застрягнете; в ейлеровому графі застрягнете лише на старті).
2. Якщо якась вершина $X$ ланцюга ще має невикористані ребра, знайдіть з $X$ наступний замкнений ланцюг із невикористаних ребер.
3. Вставте новий ланцюг у старий на місце вершини $X$.
4. Повторюйте, доки не будуть використані всі ребра.

Приклад: $K_5$ зв'язний і всі степені дорівнюють 4, отже він ейлерів (10 ребер). Перший замкнений ланцюг — контур $A, B, C, D, E, A$ (ребра 1–5). Вершина $A$ ще має невикористані ребра, другий ланцюг — «зірка» $A, C, E, B, D, A$ (ребра 6–10). Після вставлення на місце $A$: $$A, B, C, D, E, A, C, E, B, D, A$$

<div class="graph"><svg viewBox="0 0 206 196" width="206" role="img" aria-label="graf"><defs><marker id="ga27" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed c1" d="M111.3,38.2 Q133,54 153.1,68.6" marker-end="url(#ga27)"/><path class="ed c1" d="M161.7,91.3 Q153.5,117 145.9,140.8" marker-end="url(#ga27)"/><path class="ed c1" d="M127,156 Q100,156 75,156" marker-end="url(#ga27)"/><path class="ed c1" d="M54.7,142.7 Q46.5,117 38.9,93.2" marker-end="url(#ga27)"/><path class="ed c1" d="M45.3,69.8 Q67,54 87.1,39.4" marker-end="url(#ga27)"/><path class="ed c2" d="M104.3,43.3 Q120.5,93 136,140.8" marker-end="url(#ga27)"/><path class="ed c2" d="M129.7,147.8 Q87.5,117 46.9,87.4" marker-end="url(#ga27)"/><path class="ed c2" d="M48,78 Q100,78 150,78" marker-end="url(#ga27)"/><path class="ed c2" d="M154.7,86.2 Q112.5,117 71.9,146.6" marker-end="url(#ga27)"/><path class="ed c2" d="M63.3,142.7 Q79.5,93 95,45.2" marker-end="url(#ga27)"/><g class="nd on"><circle cx="100" cy="30" r="14"/><text x="100" y="30">A</text></g><g class="nd"><circle cx="166" cy="78" r="14"/><text x="166" y="78">B</text></g><g class="nd"><circle cx="141" cy="156" r="14"/><text x="141" y="156">C</text></g><g class="nd"><circle cx="59" cy="156" r="14"/><text x="59" y="156">D</text></g><g class="nd"><circle cx="34" cy="78" r="14"/><text x="34" y="78">E</text></g><text class="el" x="119.9" y="58.1">1</text><text class="el" x="145.5" y="105.8">2</text><text class="el" x="108.2" y="145">3</text><text class="el" x="59.5" y="121.4">4</text><text class="el" x="66.9" y="67.7">5</text><text class="el" x="105.9" y="83.8">6</text><text class="el" x="104.7" y="115.9">7</text><text class="el" x="86.8" y="89">8</text><text class="el" x="116.7" y="100.3">9</text><text class="el" x="85.9" y="109">10</text></svg></div>

На практиці: у графі нижче починаємо в $A$ ланцюгом $A, B, C, A$, потім додаємо $A, G, F, A$, з $G$ ланцюг $G, C, D, G$ і з $D$ ланцюг $D, F, E, D$. Результат: $A, B, C, A, G, C, D, F, E, D, G, F, A$.

<div class="graph"><svg viewBox="0 0 430 235" width="430" role="img" aria-label="graf"><defs><marker id="ga26" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path class="arrow" d="M0,0L10,5L0,10z"/></marker></defs><path class="ed" d="M139.1,48.7 Q100,80 60.9,111.3"/><path class="ed" d="M58.4,131.2 Q80,160 101.6,188.8"/><path class="ed" d="M113.4,186.4 Q130,120 146.6,53.6"/><path class="ed" d="M164,40 Q220,40 276,40"/><path class="ed" d="M300.9,48.7 Q340,80 379.1,111.3"/><path class="ed" d="M376.7,115.6 Q270,80 163.3,44.4"/><path class="ed" d="M279.5,49.3 Q200,120 120.5,190.7"/><path class="ed" d="M124,200 Q175,200 226,200"/><path class="ed" d="M244.2,186.6 Q265,120 285.8,53.4"/><path class="ed" d="M252.4,193.4 Q315,160 377.6,126.6"/><path class="ed" d="M383.7,132.5 Q370,160 356.3,187.5"/><path class="ed" d="M336,200 Q295,200 254,200"/><g class="nd"><circle cx="150" cy="40" r="14"/><text x="150" y="40">A</text></g><g class="nd"><circle cx="290" cy="40" r="14"/><text x="290" y="40">G</text></g><g class="nd"><circle cx="50" cy="120" r="14"/><text x="50" y="120">B</text></g><g class="nd"><circle cx="390" cy="120" r="14"/><text x="390" y="120">F</text></g><g class="nd"><circle cx="110" cy="200" r="14"/><text x="110" y="200">C</text></g><g class="nd"><circle cx="240" cy="200" r="14"/><text x="240" y="200">D</text></g><g class="nd"><circle cx="350" cy="200" r="14"/><text x="350" y="200">E</text></g></svg></div>

::: quiz
Скільки ребер має ейлерів замкнений ланцюг графа $K_7$?
- [ ] 7
- [ ] 14
- [x] 21
> Ейлерів ланцюг проходить кожне ребро один раз: $\frac{7\cdot6}{2} = 21$. $K_7$ ейлерів, усі степені дорівнюють 6.
:::

## Словник

| українською | англійською |
|---|---|
| вершина, ребро | vertex, edge |
| суміжні вершини | adjacent vertices |
| кратні ребра, петля | multiple edges, loop |
| степінь, порядок, розмір | degree, order, size |
| повний, дводольний, планарний граф | complete, bipartite, planar graph |
| доповнення | complement |
| маршрут, шлях, ланцюг | walk, path, trail |
| замкнений ланцюг, цикл | circuit, cycle |
| зв'язний граф, міст | connected graph, bridge |

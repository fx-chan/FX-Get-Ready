> Джерело: Anton, Rorres, *Elementary Linear Algebra*, 11-те видання, розділи 1.4, 1.5 і 1.6. Номери теорем — із цієї книжки.

## Властивості матричних операцій

Для матриць відповідних розмірів і скалярів $a, b$ справджується:

| додавання і скаляри | множення | транспонування |
|---|---|---|
| $\mathbf{A}+\mathbf{B} = \mathbf{B}+\mathbf{A}$ | $(\mathbf{AB})\mathbf{C} = \mathbf{A}(\mathbf{BC})$ | $(\mathbf{A}^{\top})^{\top} = \mathbf{A}$ |
| $(\mathbf{A}+\mathbf{B})+\mathbf{C} = \mathbf{A}+(\mathbf{B}+\mathbf{C})$ | $\mathbf{A}(\mathbf{B}\pm\mathbf{C}) = \mathbf{AB}\pm\mathbf{AC}$ | $(\mathbf{A}\pm\mathbf{B})^{\top} = \mathbf{A}^{\top}\pm\mathbf{B}^{\top}$ |
| $(a+b)\mathbf{C} = a\mathbf{C}+b\mathbf{C}$ | $(\mathbf{B}+\mathbf{C})\mathbf{A} = \mathbf{BA}+\mathbf{CA}$ | $(a\mathbf{C})^{\top} = a\mathbf{C}^{\top}$ |
| $a(b\mathbf{C}) = (ab)\mathbf{C}$ | $a(\mathbf{BC}) = (a\mathbf{B})\mathbf{C} = \mathbf{B}(a\mathbf{C})$ | $(\mathbf{AB})^{\top} = \mathbf{B}^{\top}\mathbf{A}^{\top}$ |

Нульова матриця: $\mathbf{A}+\mathbf{0} = \mathbf{A}$, $\mathbf{A0} = \mathbf{0}$. Одинична: $\mathbf{AI} = \mathbf{IA} = \mathbf{A}$. **Не справджується** комутативність $\mathbf{AB} = \mathbf{BA}$ і скорочення ($\mathbf{AB} = \mathbf{AC} \not\Rightarrow \mathbf{B} = \mathbf{C}$).

## Обернена матриця

Квадратна матриця $\mathbf{A}$ **оборотна (невироджена)**, якщо існує $\mathbf{A}^{-1}$ така, що $\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$. Інакше вона **вироджена**. Обернена матриця єдина.

**Формула для $2\times2$ (теорема 1.4.5):** $$\begin{bmatrix}a&b\\c&d\end{bmatrix}^{-1} = \frac{1}{ad-bc}\begin{bmatrix}d&-b\\-c&a\end{bmatrix},\qquad ad - bc \ne 0$$ (елементи на діагоналі міняємо місцями, поза діагоналлю змінюємо знак, ділимо на визначник).

::: drill d3-inverzia-2x2

::: quiz
Чи оборотна $\begin{bmatrix}2&-4\\-4&8\end{bmatrix}$?
- [ ] так, обернена — $\frac{1}{16}\begin{bmatrix}8&4\\4&2\end{bmatrix}$
- [x] ні, $ad - bc = 16 - 16 = 0$
- [ ] так, бо немає нульового рядка
> Рядки лінійно залежні ($R_2 = -2R_1$), визначник дорівнює 0.
:::

**Властивості** (теореми 1.4.6, 1.4.7, 1.4.9; для оборотних $\mathbf{A}, \mathbf{B}$ та $k \ne 0$):

- $(\mathbf{A}^{-1})^{-1} = \mathbf{A}$, $(\mathbf{A}^{\top})^{-1} = (\mathbf{A}^{-1})^{\top}$,
- $(\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}$ і $(\mathbf{ABC})^{-1} = \mathbf{C}^{-1}\mathbf{B}^{-1}\mathbf{A}^{-1}$ — **порядок змінюється на обернений**,
- $(k\mathbf{A})^{-1} = \frac1k\mathbf{A}^{-1}$, $\mathbf{A}^{-n} = (\mathbf{A}^{-1})^n = (\mathbf{A}^n)^{-1}$.

::: drill d3-vlastnosti

**Як знайти $\mathbf{A}$ з оберненої:** обчисліть обернену до обох частин. З $(7\mathbf{A})^{-1} = \mathbf{M}$ маємо $7\mathbf{A} = \mathbf{M}^{-1}$, $\mathbf{A} = \frac17\mathbf{M}^{-1}$. З $(\mathbf{I}+2\mathbf{A})^{-1} = \mathbf{M}$: $\mathbf{A} = \frac12(\mathbf{M}^{-1} - \mathbf{I})$.

**Рівняння з матрицями:** множте зліва або справа і **зберігайте порядок**: $\mathbf{AXB} = \mathbf{C} \Rightarrow \mathbf{X} = \mathbf{A}^{-1}\mathbf{C}\mathbf{B}^{-1}$ (а не $\mathbf{A}^{-1}\mathbf{B}^{-1}\mathbf{C}$!).

::: quiz
З рівняння $\mathbf{AXB} = \mathbf{C}$ ($\mathbf{A}, \mathbf{B}$ оборотні) випливає
- [ ] $\mathbf{X} = \mathbf{C}\mathbf{A}^{-1}\mathbf{B}^{-1}$
- [x] $\mathbf{X} = \mathbf{A}^{-1}\mathbf{C}\mathbf{B}^{-1}$
- [ ] $\mathbf{X} = \mathbf{A}^{-1}\mathbf{B}^{-1}\mathbf{C}$
> Зліва множимо на $\mathbf{A}^{-1}$, а справа на $\mathbf{B}^{-1}$: $\mathbf{A}^{-1}\mathbf{AXB}\mathbf{B}^{-1} = \mathbf{X}$.
:::

## Многочлен від матриці

Для $p(x) = a_0 + a_1x + \dots + a_mx^m$ визначаємо $p(\mathbf{A}) = a_0\mathbf{I} + a_1\mathbf{A} + \dots + a_m\mathbf{A}^m$ — **сталу множимо на матрицю $\mathbf{I}$**. Оскільки степені $\mathbf{A}$ комутують між собою, маємо $p(x) = p_1(x)p_2(x) \Rightarrow p(\mathbf{A}) = p_1(\mathbf{A})p_2(\mathbf{A})$, напр. $\mathbf{A}^2 - 9\mathbf{I} = (\mathbf{A}+3\mathbf{I})(\mathbf{A}-3\mathbf{I})$.

::: quiz
$p(x) = x^2 - 2x + 3$. Чому дорівнює $p(\mathbf{A})$?
- [ ] $\mathbf{A}^2 - 2\mathbf{A} + 3$
- [x] $\mathbf{A}^2 - 2\mathbf{A} + 3\mathbf{I}$
- [ ] $(\mathbf{A} - 3\mathbf{I})(\mathbf{A} + \mathbf{I})$
> До матриці не можна додати число — стала 3 стає $3\mathbf{I}$.
:::

## Елементарні матриці

**Елементарна матриця** утворюється з $\mathbf{I}_n$ **однією** елементарною операцією над рядками. Множення $\mathbf{EA}$ (зліва) виконує з $\mathbf{A}$ ту саму операцію.

| операція | приклад $\mathbf{E}$ ($3\times3$) | $\mathbf{E}^{-1}$ |
|---|---|---|
| перестановка $R_1 \leftrightarrow R_3$ | $\begin{bmatrix}0&0&1\\0&1&0\\1&0&0\end{bmatrix}$ | та сама перестановка |
| $R_2 \to 5R_2$ | $\begin{bmatrix}1&0&0\\0&5&0\\0&0&1\end{bmatrix}$ | $R_2 \to \frac15R_2$ |
| $R_3 \to R_3 - 2R_1$ | $\begin{bmatrix}1&0&0\\0&1&0\\-2&0&1\end{bmatrix}$ | $R_3 \to R_3 + 2R_1$ |

Множення $\mathbf{EA}$ — це теорема 1.5.1. Елементарна матриця завжди оборотна, і обернена до неї теж елементарна, це протилежна операція (теорема 1.5.2). Матриця, що утворилася **двома** операціями (напр. $-1$ на діагоналі й водночас перестановка), елементарною не є.

::: drill d3-elementarna

::: quiz
Чи є $\begin{bmatrix}-5&1\\1&0\end{bmatrix}$ елементарною?
- [x] ні — її не можна отримати з $\mathbf{I}_2$ однією операцією
- [ ] так, перестановка рядків
- [ ] так, додавання кратного
> Перестановка дає $\begin{bmatrix}0&1\\1&0\end{bmatrix}$; елемент $-5$ вимагав би ще однієї операції.
:::

## Обчислення оберненої вилученням

Перетворюємо $[\mathbf{A}\,|\,\mathbf{I}]$ операціями над рядками, доки зліва не буде $\mathbf{I}$: $$[\mathbf{A}\,|\,\mathbf{I}] \longrightarrow [\mathbf{I}\,|\,\mathbf{A}^{-1}]$$ Якщо зліва з'явиться **нульовий рядок**, $\mathbf{A}$ необоротна.

Чому це працює: якщо $\mathbf{E}_k\cdots\mathbf{E}_2\mathbf{E}_1\mathbf{A} = \mathbf{I}$, то $\mathbf{A}^{-1} = \mathbf{E}_k\cdots\mathbf{E}_1$ і $\mathbf{A} = \mathbf{E}_1^{-1}\mathbf{E}_2^{-1}\cdots\mathbf{E}_k^{-1}$ — кожна оборотна матриця є **добутком елементарних матриць**.

::: drill d3-gauss-jordan

**Рівносильні твердження** (теореми 1.5.3, 1.6.4, 2.3.8) для квадратної $\mathbf{A}$ ($n\times n$): $\mathbf{A}$ оборотна $\iff$ RREF$(\mathbf{A}) = \mathbf{I}$ $\iff$ $\mathbf{Ax} = \mathbf{0}$ має лише тривіальний розв'язок $\iff$ $\mathbf{Ax} = \mathbf{b}$ має єдиний розв'язок для кожного $\mathbf{b}$ $\iff$ $\mathbf{A}$ є добутком елементарних матриць $\iff$ $\det\mathbf{A} \ne 0$.

**Еквівалентність за рядками:** $\mathbf{A} \sim \mathbf{B}$, якщо $\mathbf{B}$ можна отримати з $\mathbf{A}$ операціями над рядками, тобто $\mathbf{B} = \mathbf{CA}$ для деякої оборотної $\mathbf{C}$ (добутку елементарних матриць). Дві матриці еквівалентні за рядками тоді й лише тоді, коли мають однаковий RREF.

::: quiz
Під час перетворення $[\mathbf{A}\,|\,\mathbf{I}]$ зліва вийшов рядок $[0\;0\;0]$. Що це означає?
- [ ] треба переставити рядки й продовжити
- [x] $\mathbf{A}$ необоротна
- [ ] $\mathbf{A}^{-1}$ має нульовий рядок
> Нульовий рядок означає, що RREF$(\mathbf{A}) \ne \mathbf{I}$.
:::

## Системи через обернену матрицю

Якщо $\mathbf{A}$ **квадратна й оборотна**, система $\mathbf{Ax} = \mathbf{b}$ має єдиний розв'язок $$\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}.$$ Перевага: для кількох правих частин досить однієї оберненої. Так само можна одразу виконувати вилучення для $[\mathbf{A}\,|\,\mathbf{b}_1\,|\,\mathbf{b}_2]$ (розділ 1.6). Якщо $\mathbf{A}$ неквадратна або вироджена, метод застосувати не можна — тоді система має жодного або нескінченно багато розв'язків (розв'язуємо вилученням).

::: drill d3-sustava

**Теореми 1.6.3 і 1.6.5:** для квадратних матриць досить перевірити один бік: якщо $\mathbf{BA} = \mathbf{I}$, то вже $\mathbf{B} = \mathbf{A}^{-1}$. Якщо добуток $\mathbf{AB}$ квадратних матриць оборотний, то оборотні й $\mathbf{A}$ та $\mathbf{B}$.

::: quiz
Однорідна система $\mathbf{Ax} = \mathbf{0}$ з оборотною $\mathbf{A}$ має
- [x] лише тривіальний розв'язок $\mathbf{x} = \mathbf{A}^{-1}\mathbf{0} = \mathbf{0}$
- [ ] нескінченно багато розв'язків
- [ ] жодного розв'язку
> Нетривіальний розв'язок існував би лише для виродженої $\mathbf{A}$.
:::

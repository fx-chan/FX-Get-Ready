## Вектори

**Вектор** у $\mathbb{R}^n$ — це впорядкований набір із $n$ чисел. Записуємо його як **рядковий** вектор $(v_1, v_2, \dots, v_n)$ або як **стовпцевий** вектор (матриця $n\times 1$). Вектор — окремий випадок матриці.

| операція | запис | результат |
|---|---|---|
| сума | $\mathbf{u}+\mathbf{v} = (u_1+v_1, \dots, u_n+v_n)$ | вектор |
| множення на скаляр | $k\mathbf{v} = (kv_1, \dots, kv_n)$ | вектор |
| скалярний добуток | $\mathbf{u}\cdot\mathbf{v} = u_1v_1 + \dots + u_nv_n$ | **число** |
| довжина (норма) | $\lVert\mathbf{v}\rVert = \sqrt{v_1^2+\dots+v_n^2} = \sqrt{\mathbf{v}\cdot\mathbf{v}}$ | число $\ge 0$ |

Якщо $\mathbf{u}\cdot\mathbf{v} = 0$, вектори **перпендикулярні (ортогональні)**. Додавати можна лише вектори однакової довжини.

::: quiz
Який скалярний добуток $\mathbf{u} = (2, -1, 3)$ і $\mathbf{v} = (1, 4, 2)$?
- [ ] $(2, -4, 6)$
- [x] $4$
- [ ] $12$
- [ ] неможливо обчислити
> $2\cdot1 + (-1)\cdot4 + 3\cdot2 = 2 - 4 + 6 = 4$. Скалярний добуток — це число, а не вектор.
:::

## Матриця — основні поняття

**Матриця розміру $m\times n$** має $m$ рядків і $n$ стовпців. Елемент в $i$-му рядку та $j$-му стовпці — це $a_{ij}$ (спочатку **рядок**, потім **стовпець**).

$$\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix}\quad (2\times 3)$$

- дві матриці **рівні**, якщо мають однаковий розмір і однакові всі елементи,
- матриця **квадратна**, якщо $m = n$; елементи $a_{11}, a_{22}, \dots, a_{nn}$ утворюють **головну діагональ**,
- **нульова матриця** $\mathbf{0}$ має всі елементи 0, **одинична** $\mathbf{I}_n$ має на діагоналі 1, а решта 0.

::: quiz
Матриця $\mathbf{A}$ має розмір $3\times 4$. Скільки в ній елементів і якого елемента **не існує**?
- [ ] 7 елементів, не існує $a_{34}$
- [x] 12 елементів, не існує $a_{43}$
- [ ] 12 елементів, не існує $a_{34}$
> 3 рядки × 4 стовпці = 12 елементів. $a_{43}$ був би в 4-му рядку — такого в матриці немає.
:::

## Спеціальні квадратні матриці

| тип | умова | приклад |
|---|---|---|
| діагональна | $a_{ij} = 0$ для $i \ne j$ | $\begin{bmatrix}2&0\\0&-1\end{bmatrix}$ |
| верхня трикутна | $a_{ij} = 0$ для $i > j$ (під діагоналлю нулі) | $\begin{bmatrix}1&1&1\\0&1&1\\0&0&1\end{bmatrix}$ |
| нижня трикутна | $a_{ij} = 0$ для $i < j$ (над діагоналлю нулі) | $\begin{bmatrix}0&0&0\\1&0&0\\1&1&0\end{bmatrix}$ |
| симетрична | $\mathbf{A}^{\top} = \mathbf{A}$, тобто $a_{ij} = a_{ji}$ | $\begin{bmatrix}1&5\\5&3\end{bmatrix}$ |
| кососиметрична | $\mathbf{A}^{\top} = -\mathbf{A}$, тобто $a_{ij} = -a_{ji}$, на діагоналі 0 | $\begin{bmatrix}0&2\\-2&0\end{bmatrix}$ |

> Діагональна матриця є **водночас** верхньою і нижньою трикутною та симетричною. Нульова квадратна матриця
> єдина, що є і симетричною, і кососиметричною. Неквадратна матриця не має жодного з цих типів.

::: quiz
Чи є матриця $\begin{bmatrix}0&0&6\\0&-6&0\\-6&0&0\end{bmatrix}$ кососиметричною?
- [ ] так, бо $a_{13} = -a_{31}$
- [x] ні, бо на діагоналі є $-6 \ne 0$
- [ ] так, бо вона квадратна
> Кососиметрична матриця мусить мати $a_{ii} = -a_{ii}$, тобто нулі на діагоналі. Елемент $a_{22} = -6$ це порушує.
:::

::: drill d1-typ

## Додавання та множення на скаляр

- $\mathbf{A}+\mathbf{B}$ — додаємо елементи на однакових позиціях. **Лише для матриць однакового розміру.**
- $k\mathbf{A}$ — кожен елемент множимо на число $k$. Різниця: $\mathbf{A}-\mathbf{B} = \mathbf{A}+(-1)\mathbf{B}$.
- **лінійна комбінація**: $2\mathbf{A} - 3\mathbf{B} + \mathbf{C}$ — спочатку множення, потім суми.

$$2\begin{bmatrix}1&-2\\3&0\end{bmatrix} - \begin{bmatrix}4&1\\-1&5\end{bmatrix} = \begin{bmatrix}-2&-5\\7&-5\end{bmatrix}$$

Властивості: $\mathbf{A}+\mathbf{B} = \mathbf{B}+\mathbf{A}$, $(\mathbf{A}+\mathbf{B})+\mathbf{C} = \mathbf{A}+(\mathbf{B}+\mathbf{C})$, $k(\mathbf{A}+\mathbf{B}) = k\mathbf{A}+k\mathbf{B}$, $\mathbf{A}-\mathbf{A} = \mathbf{0}$.

::: drill d1-scitanie

## Транспонована матриця

$\mathbf{A}^{\top}$ утворюється заміною рядків і стовпців: $(\mathbf{A}^{\top})_{ij} = a_{ji}$. Матриця $m\times n$ стає $n\times m$.

$$\begin{bmatrix}2&0&-1\\5&3&4\end{bmatrix}^{\top} = \begin{bmatrix}2&5\\0&3\\-1&4\end{bmatrix}$$

| властивість | |
|---|---|
| $(\mathbf{A}^{\top})^{\top} = \mathbf{A}$ | транспонувати двічі = нічого не змінити |
| $(\mathbf{A}+\mathbf{B})^{\top} = \mathbf{A}^{\top}+\mathbf{B}^{\top}$ | |
| $(k\mathbf{A})^{\top} = k\mathbf{A}^{\top}$ | |
| $(\mathbf{AB})^{\top} = \mathbf{B}^{\top}\mathbf{A}^{\top}$ | **порядок змінюється на обернений!** |

::: quiz
$\mathbf{C}$ має розмір $2\times 2$, а $\mathbf{F}$ — розмір $3\times 2$. Чи можна обчислити $2\mathbf{C}^{\top} - 3\mathbf{F}$?
- [ ] так, результат $3\times 2$
- [ ] так, результат $2\times 2$
- [x] ні, $\mathbf{C}^{\top}$ має розмір $2\times2$, а $\mathbf{F}$ — $3\times2$
> Транспонування квадратної матриці не змінює розмір. Віднімати можна лише матриці однакового розміру.
:::

::: drill d1-transpozicia

## Слід матриці

**Слід** квадратної матриці — це сума елементів головної діагоналі: $\operatorname{tr}(\mathbf{A}) = a_{11} + a_{22} + \dots + a_{nn}$. Для неквадратної матриці слід **не визначений**.

- $\operatorname{tr}(\mathbf{A}+\mathbf{B}) = \operatorname{tr}\mathbf{A} + \operatorname{tr}\mathbf{B}$, $\operatorname{tr}(k\mathbf{A}) = k\operatorname{tr}\mathbf{A}$,
- $\operatorname{tr}(\mathbf{A}^{\top}) = \operatorname{tr}\mathbf{A}$ (транспонування діагональ не змінює),
- $\operatorname{tr}(\mathbf{AB}) = \operatorname{tr}(\mathbf{BA})$, навіть якщо $\mathbf{AB} \ne \mathbf{BA}$.

> Хитрість: для $\operatorname{tr}(\mathbf{DE}^{\top})$ не треба рахувати весь добуток — досить діагональних елементів:
> $(\mathbf{DE}^{\top})_{ii}$ = скалярний добуток $i$-го рядка $\mathbf{D}$ та $i$-го рядка $\mathbf{E}$.

::: drill d1-stopa

## Множення матриць

Добуток $\mathbf{AB}$ існує, лише якщо **кількість стовпців $\mathbf{A}$ = кількість рядків $\mathbf{B}$**:

$$\underbrace{\mathbf{A}}_{m\times \color{red}{n}}\;\underbrace{\mathbf{B}}_{\color{red}{n}\times p} = \underbrace{\mathbf{C}}_{m\times p},\qquad
c_{ij} = a_{i1}b_{1j} + a_{i2}b_{2j} + \dots + a_{in}b_{nj}$$

Елемент $c_{ij}$ = скалярний добуток **$i$-го рядка $\mathbf{A}$** та **$j$-го стовпця $\mathbf{B}$**.

$$\begin{bmatrix}1&2\\3&4\end{bmatrix}\begin{bmatrix}0&1\\-1&2\end{bmatrix} =
\begin{bmatrix}1\cdot0+2\cdot(-1) & 1\cdot1+2\cdot2\\ 3\cdot0+4\cdot(-1) & 3\cdot1+4\cdot2\end{bmatrix} =
\begin{bmatrix}-2&5\\-4&11\end{bmatrix}$$

::: drill d1-rozmer
::: drill d1-sucin

**Один рядок або стовпець добутку** — усю матрицю рахувати не треба:

- $i$-й рядок $\mathbf{AB}$ = ($i$-й рядок $\mathbf{A}$) $\cdot\,\mathbf{B}$,
- $j$-й стовпець $\mathbf{AB}$ = $\mathbf{A}\,\cdot$ ($j$-й стовпець $\mathbf{B}$).

**Степінь** $\mathbf{A}^k = \mathbf{A}\mathbf{A}\cdots\mathbf{A}$ існує лише для **квадратної** матриці; $\mathbf{A}^0 = \mathbf{I}$. Добуток рядкового вектора $1\times n$ і стовпцевого $n\times1$ — це матриця $1\times1$ (число), у зворотному порядку $n\times n$.

::: quiz
$\mathbf{R}$ має розмір $1\times3$, а $\mathbf{J}$ — $3\times1$. Які розміри мають $\mathbf{RJ}$ і $\mathbf{JR}$?
- [ ] обидва $1\times1$
- [x] $\mathbf{RJ}$ має розмір $1\times1$, $\mathbf{JR}$ — $3\times3$
- [ ] $\mathbf{JR}$ обчислити неможливо
> $(1\times\underline{3})(\underline{3}\times1) = 1\times1$ і $(3\times\underline{1})(\underline{1}\times3) = 3\times3$ — внутрішні числа рівні в обох випадках.
:::

## Властивості множення

| справджується ✓ | не справджується ✗ (у загальному випадку) |
|---|---|
| $(\mathbf{AB})\mathbf{C} = \mathbf{A}(\mathbf{BC})$ — асоціативність | $\mathbf{AB} = \mathbf{BA}$ — комутативність |
| $\mathbf{A}(\mathbf{B}+\mathbf{C}) = \mathbf{AB}+\mathbf{AC}$ — лівий дистрибутивний закон | $\mathbf{AB} = \mathbf{AC} \Rightarrow \mathbf{B} = \mathbf{C}$ — скорочення |
| $(\mathbf{B}+\mathbf{C})\mathbf{A} = \mathbf{BA}+\mathbf{CA}$ — правий дистрибутивний закон | $\mathbf{AB} = \mathbf{0} \Rightarrow \mathbf{A}=\mathbf{0}$ або $\mathbf{B}=\mathbf{0}$ |
| $k(\mathbf{AB}) = (k\mathbf{A})\mathbf{B} = \mathbf{A}(k\mathbf{B})$ | $(\mathbf{A}+\mathbf{B})^2 = \mathbf{A}^2+2\mathbf{AB}+\mathbf{B}^2$ |
| $\mathbf{AI} = \mathbf{IA} = \mathbf{A}$, $(\mathbf{AB})^{\top} = \mathbf{B}^{\top}\mathbf{A}^{\top}$ | $(\mathbf{AB})^{\top} = \mathbf{A}^{\top}\mathbf{B}^{\top}$ |

Матриці **комутативні**, якщо $\mathbf{AB} = \mathbf{BA}$ (напр. будь-яка матриця з $\mathbf{I}$, з $\mathbf{0}$ або сама із собою). Якщо $\mathbf{AB}$ і $\mathbf{BA}$ мають різний розмір, вони не можуть бути рівними.

::: quiz
Яка рівність справджується для всіх матриць відповідних розмірів?
- [ ] $\mathbf{L}(\mathbf{ML}) = \mathbf{L}^2\mathbf{M}$
- [x] $\mathbf{E}(\mathbf{FK}) = (\mathbf{EF})\mathbf{K}$
- [ ] $(\mathbf{AK})^{\top} = \mathbf{A}^{\top}\mathbf{K}^{\top}$
> Асоціативність справджується завжди. $\mathbf{L}(\mathbf{ML}) = \mathbf{LML}$, що дорівнює $\mathbf{L}^2\mathbf{M}$ лише тоді, коли $\mathbf{L}$ і $\mathbf{M}$ комутують. Транспонування добутку змінює порядок.
:::

::: quiz
$\mathbf{A} = \begin{bmatrix}0&1\\0&0\end{bmatrix}$. Чому дорівнює $\mathbf{A}^2$?
- [ ] $\mathbf{A}$
- [x] нульовій матриці, хоча $\mathbf{A} \ne \mathbf{0}$
- [ ] $\mathbf{I}$
> $\mathbf{A}^2 = \begin{bmatrix}0\cdot0+1\cdot0 & 0\cdot1+1\cdot0\\0&0\end{bmatrix} = \mathbf{0}$. Добуток ненульових матриць може бути нульовим.
:::

## На контрольній

1. Перед кожним обчисленням **перевіряйте розміри** — частину задач навмисно обчислити неможливо.
2. Транспонування добутку розпишіть: $(\mathbf{CD})^{\top} = \mathbf{D}^{\top}\mathbf{C}^{\top}$.
3. Для сліду добутку рахуйте лише діагональ.
4. Коли треба «знайти лише рядок/стовпець», множте тільки відповідний рядок/стовпець.

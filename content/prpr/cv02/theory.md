## Priorita operátorov / Приоритет операторов

Od najvyššej po najnižšiu (výber):

| skupina | operátory |
|---|---|
| unárne | `++ -- ! - (typ) sizeof &` |
| multiplikatívne | `* / %` |
| aditívne | `+ -` |
| relačné | `< <= > >=` |
| rovnosť | `== !=` |
| logické | `&&`, potom `\|\|` |
| podmienený | `? :` |
| priradenie | `= += -= *= /= %=` |

Keď si nie ste istí — **použite zátvorky**. / Не уверены — ставьте скобки.

::: quiz
Akú hodnotu má `1 + 2 * 3 > 6 && 0`?
- [ ] 1
- [x] 0
- [ ] 7
> `2*3 = 6`, `1+6 = 7`, `7 > 6` je 1, ale `1 && 0` je 0.
:::

## Podmienený výraz `?:` / Тернарный оператор

```c
int max = (a > b) ? a : b;      // ak a > b, výsledok je a, inak b
printf("%s\n", n % 2 == 0 ? "parne" : "neparne");
```

::: drill d2-ternary
## if – else if – else

```c
if (body >= 92)      printf("A\n");
else if (body >= 83) printf("B\n");
else if (body >= 74) printf("C\n");
else                 printf("FX\n");
```

> **Pozor:** `if (x = 5)` je priradenie (vždy pravda), porovnanie je `if (x == 5)`.

## switch

`switch` porovnáva celočíselnú hodnotu (aj `char`) s konštantami. Bez `break` vykonávanie
**prepadne** do ďalšej vetvy.

```c
switch (znak) {
    case '+': printf("%d\n", a + b); break;
    case '-': printf("%d\n", a - b); break;
    case 'x':
    case '*': printf("%d\n", a * b); break;   // dve vetvy zdieľajú kód
    default:  printf("Zle zadana volba.\n");
}
```

::: quiz
Čo vypíše `int x = 1; switch (x) { case 1: printf("A"); case 2: printf("B"); break; default: printf("C"); }`?
- [ ] `A`
- [x] `AB`
- [ ] `ABC`
- [ ] `C`
> Vo vetve `case 1` chýba `break`, preto sa vykoná aj `case 2`. Tam `break` ukončí switch.
:::

::: drill d2-switch
## Cykly / Циклы

```c
// while: podmienka sa testuje PRED telom (telo sa nemusí vykonať ani raz)
while (n > 0) { sucet += n % 10; n /= 10; }

// do-while: telo sa vykoná ASPOŇ raz (vhodné na opakované načítanie)
do { scanf("%d", &n); } while (n < 0);

// for: inicializácia; podmienka; krok
for (int i = 1; i <= n; i++) sucet += i;
```

- `break` — okamžite ukončí cyklus
- `continue` — preskočí zvyšok tela a pokračuje ďalšou iteráciou

::: quiz
Koľkokrát sa vykoná telo `for (i = 0; i < 10; i += 3)`?
- [ ] 3
- [x] 4
- [ ] 10
- [ ] 3.33
> `i` = 0, 3, 6, 9 → štyrikrát; pri `i = 12` podmienka neplatí.
:::

::: drill d2-for
::: drill d2-while
## Statické jednorozmerné pole / Статический массив

```c
#define N 11
int pole[N];                      // N prvkov, indexy 0 .. N-1
int p[5] = {1, 2, 3};             // zvyšok sa doplní nulami: {1,2,3,0,0}
for (int i = 0; i < N; i++)
    scanf("%d", &pole[i]);
```

- veľkosť statického poľa musí byť známa pri kompilácii (konštanta),
- C **nekontroluje** hranice poľa: `pole[N]` je chyba, ktorú kompilátor neodhalí,
- počet prvkov: `sizeof(p) / sizeof(p[0])`.

::: quiz
`int a[5];` — ktorý prístup je chybný? / Какое обращение ошибочно?
- [ ] `a[0]`
- [ ] `a[4]`
- [x] `a[5]`
> Indexy sú 0 až 4. `a[5]` je mimo poľa — nedefinované správanie.
:::

::: drill d2-array

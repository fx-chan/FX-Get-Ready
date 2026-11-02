## Statická vs. dynamická alokácia / Статическая и динамическая память

| | statická (`int a[100];`) | dynamická (`malloc`) |
|---|---|---|
| veľkosť | známa pri kompilácii | určí sa za behu (napr. načíta sa `n`) |
| kde | zásobník / dátový segment | halda (heap) |
| uvoľnenie | automaticky | **vy** cez `free` |

```c
#include <stdlib.h>

int n;
scanf("%d", &n);
int *a = malloc(n * sizeof(int));       // n prvkov typu int
if (a == NULL) {                        // pamäť nemusí byť k dispozícii
    printf("Malo pamate\n");
    return 1;
}
for (int i = 0; i < n; i++) a[i] = i;
free(a);                                // vrátiť pamäť
a = NULL;                               // ochrana pred použitím uvoľnenej pamäte
```

- `calloc(n, sizeof(int))` — ako `malloc`, ale pamäť **vynuluje**,
- `realloc(p, nova_velkost)` — zmení veľkosť bloku (môže ho presunúť; vráti novú adresu).

::: quiz
Koľko bajtov alokuje `malloc(10 * sizeof(double))`, ak `sizeof(double) == 8`?
- [ ] 10
- [ ] 18
- [x] 80
- [ ] 8
> 10 prvkov po 8 bajtov.
:::

::: drill d6-malloc
## Ukazovateľová aritmetika / Адресная арифметика

Pripočítanie `1` k ukazovateľu ho posunie o **jeden prvok** (nie o jeden bajt).

```c
int a[5] = {10, 20, 30, 40, 50};
int *p = a;            // meno poľa = adresa prvého prvku
printf("%d\n", *(p + 2));   // 30 — to isté ako a[2] alebo p[2]
p++;                   // teraz ukazuje na a[1]
printf("%ld\n", (long)(&a[4] - p));   // rozdiel ukazovateľov = 3 prvky
```

::: quiz
`int a[] = {1, 2, 3, 4}; int *p = a + 1;` Čo je `*(p + 2)`?
- [ ] 2
- [ ] 3
- [x] 4
- [ ] mimo poľa
> `p` ukazuje na `a[1]`, `p + 2` na `a[3]`, čo je 4.
:::

::: drill d6-ptr-arith
## Časté chyby / Частые ошибки

- **memory leak** — zabudnutý `free` (alebo stratená adresa bloku),
- **dangling pointer** — použitie pamäte po `free`,
- **dvojité `free`** toho istého bloku,
- zápis mimo alokovaného bloku (napr. zabudnuté miesto pre `'\0'` pri reťazci: `malloc(strlen(s) + 1)`).

::: drill d6-realloc

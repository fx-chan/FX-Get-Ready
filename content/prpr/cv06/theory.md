## Statická vs. dynamická alokácia

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
- `realloc(p, nova_velkost)` — zmení veľkosť bloku (môže ho presunúť; vráti novú adresu),
- `memset(p, 0, n * sizeof(int))` (`string.h`) — rýchle nastavenie každého **bajtu** bloku na hodnotu
  (bezpečne len na 0; `memset(p, 1, ...)` nedá v `int` jednotky).

```c
int *tmp = realloc(a, 2 * n * sizeof(int));
if (tmp == NULL) { free(a); return 1; }   // pri neúspechu ostáva starý blok platný
a = tmp;
```

### Dynamické pole a funkcie

Funkcia môže pole vytvoriť a vrátiť adresu — alebo ho zapísať cez ukazovateľ na ukazovateľ:

```c
int *vytvor(int n) {                 // vráti adresu nového bloku
    return calloc(n, sizeof(int));
}

void vytvor2(int **p, int n) {       // zmení ukazovateľ volajúceho
    *p = malloc(n * sizeof(int));
}

int *a = vytvor(10);
int *b;
vytvor2(&b, 10);
free(a); free(b);
```

> Vrátiť adresu **lokálneho** poľa (`int pole[10]; return pole;`) nesmiete — zanikne s funkciou.
> Dynamická pamäť žije, kým ju neuvoľníte `free`.

::: quiz
Koľko bajtov alokuje `malloc(10 * sizeof(double))`, ak `sizeof(double) == 8`?
- [ ] 10
- [ ] 18
- [x] 80
- [ ] 8
> 10 prvkov po 8 bajtov.
:::

::: drill d6-malloc
## Ukazovateľová aritmetika

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

### Porovnávanie ukazovateľov, pole a ukazovateľ

- ukazovatele do toho istého poľa možno porovnať `<`, `==`: `p < q` znamená, že `p` je skôr v poli,
- porovnanie s `NULL`: `if (p == NULL)` alebo skrátene `if (!p)`,
- rozdiel `q - p` je počet **prvkov** medzi nimi (typ `ptrdiff_t`),
- `a[i]` je to isté ako `*(a + i)` — operátor `[]` je len skrátený zápis.

```c
for (int *p = a; p < a + n; p++)   // prechod poľom len ukazovateľom
    printf("%d ", *p);
```

Rozdiel medzi poľom a ukazovateľom je pri `sizeof`:

```c
int a[10];
int *d = malloc(10 * sizeof(int));
sizeof(a);    // 40 — celé statické pole
sizeof(d);    // 8  — len veľkosť ukazovateľa! veľkosť bloku si treba pamätať v premennej

void f(int pole[]) {     // pole ako parameter je v skutočnosti int *pole
    sizeof(pole);        // 8, nie veľkosť poľa → dĺžku treba poslať ako ďalší parameter
}
```

**Pole ukazovateľov** — každý prvok je ukazovateľ, napr. na samostatne alokovaný blok alebo reťazec:

```c
char *slova[3];
slova[0] = malloc(10);    // každý prvok má vlastnú pamäť (a vlastný free)
```

::: quiz
`void f(int a[]) { printf("%zu", sizeof(a)); }` — čo vypíše na 64-bitovom systéme pre `int x[100]; f(x);`?
- [ ] 400
- [ ] 100
- [x] 8
> Pole sa do funkcie odovzdá ako ukazovateľ na prvý prvok — `sizeof` vráti veľkosť ukazovateľa.
:::

::: drill d6-ptr-arith
## Časté chyby

- **memory leak** — zabudnutý `free` (alebo stratená adresa bloku),
- **dangling pointer** — použitie pamäte po `free`,
- **dvojité `free`** toho istého bloku,
- zápis mimo alokovaného bloku (napr. zabudnuté miesto pre `'\0'` pri reťazci: `malloc(strlen(s) + 1)`),
- `p = realloc(p, ...)` bez kontroly — pri neúspechu sa stratí pôvodná adresa (leak),
- `malloc(n)` namiesto `malloc(n * sizeof(int))` — alokuje bajty, nie prvky.

::: drill d6-realloc

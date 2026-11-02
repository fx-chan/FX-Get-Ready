## Viacrozmerné polia / Многомерные массивы

```c
#define N 20
int m[N][N];                 // statické 2D pole: N riadkov po N prvkov, v pamäti za sebou
m[i][j] = 5;                 // riadok i, stĺpec j

void vypis(int m[][N], int n);   // pri odovzdaní do funkcie musí byť známy počet stĺpcov
```

Ďalšie varianty z prednášky:

| zápis | význam |
|---|---|
| `int *p[10];` | **pole** 10 ukazovateľov (každý riadok môže mať inú dĺžku) |
| `int (*p)[10];` | **ukazovateľ na pole** 10 intov |
| `int **p;` | ukazovateľ na ukazovateľ — dynamické 2D pole (Cvičenie 6) |

::: quiz
`int m[3][4];` — koľko prvkov má pole a aký je posledný platný prvok?
- [ ] 7 prvkov, `m[3][4]`
- [x] 12 prvkov, `m[2][3]`
- [ ] 12 prvkov, `m[3][4]`
> 3 riadky × 4 stĺpce. Indexy riadkov 0–2, stĺpcov 0–3.
:::

::: drill d7-diagonal
## Rekurzia / Рекурсия

Rekurzívna funkcia volá samu seba. Potrebuje **ukončovaciu podmienku** — inak pretečie zásobník.

```c
long faktorial(int n) {
    if (n <= 1)                      // ukončovacia podmienka
        return 1;
    return n * faktorial(n - 1);     // rekurzívne volanie s menším problémom
}
```

::: quiz
Čo vráti `f(4)`, ak `int f(int n) { return n == 0 ? 0 : n + f(n - 1); }`?
- [ ] 4
- [x] 10
- [ ] 24
- [ ] nekonečná rekurzia
> 4 + 3 + 2 + 1 + 0 = 10.
:::

::: drill d7-recursion
## Konštantné premenné / Константы

```c
const double PI = 3.14159;      // hodnotu nemožno meniť
void vypis(const char *s);      // funkcia sľubuje, že reťazec nezmení
```

## Vlastné dátové typy: struct, typedef, enum, union

```c
typedef struct {
    char meno[101];
    int vek;
    double plat;
} OSOBA;

OSOBA o = {"Jan Novak", 30, 1500.0};
OSOBA *p = &o;
printf("%s %d\n", o.meno, o.vek);    // prístup cez premennú: bodka
p->vek++;                            // prístup cez ukazovateľ: šípka, to isté ako (*p).vek++

typedef enum { PONDELOK, UTOROK, STREDA } DEN;   // pomenované celé čísla 0, 1, 2
union cislo { int i; double d; };   // všetky položky zdieľajú tú istú pamäť
```

::: quiz
`OSOBA *p = &o;` Ako zmeníme vek osoby cez `p`?
- [ ] `p.vek = 31;`
- [x] `p->vek = 31;`
- [ ] `*p.vek = 31;`
> `*p.vek` sa vyhodnotí ako `*(p.vek)` — chyba. Správne `p->vek` alebo `(*p).vek`.
:::

::: drill d7-struct

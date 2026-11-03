## Viacrozmerné polia / Многомерные массивы

```c
#define N 20
int m[N][N];                 // statické 2D pole: N riadkov po N prvkov, v pamäti za sebou
m[i][j] = 5;                 // riadok i, stĺpec j

void vypis(int m[][N], int n);   // pri odovzdaní do funkcie musí byť známy počet stĺpcov
```

Štyri spôsoby, ako vytvoriť 2D pole (prednáška P6):

| zápis | riadky | stĺpce | pamäť |
|---|---|---|---|
| `int m[3][4];` | statické | statické | jeden súvislý blok, riadok za riadkom |
| `int *p[3];` — **pole ukazovateľov** | statické (3) | dynamické, každý riadok iný | `p[i] = malloc(...)` |
| `int (*p)[4];` — **ukazovateľ na pole** | dynamické | statické (4) | `p = malloc(n * sizeof *p);` jeden blok |
| `int **p;` — **ukazovateľ na ukazovateľ** | dynamické | dynamické | pole ukazovateľov + blok pre každý riadok |

Vo všetkých prípadoch sa k prvku pristupuje rovnako: `p[i][j]`.

```c
int n = 3, k = 4;
int **p = malloc(n * sizeof(int *));      // 1. pole ukazovateľov na riadky
for (int i = 0; i < n; i++)
    p[i] = malloc(k * sizeof(int));       // 2. každý riadok zvlášť

for (int i = 0; i < n; i++)               // uvoľnenie v OPAČNOM poradí:
    free(p[i]);                           //    najprv riadky,
free(p);                                  //    potom pole ukazovateľov
```

- **pravouhlé pole** — všetky riadky rovnako dlhé,
- **zubaté pole** (jagged) — riadky rôznej dĺžky (napr. trojuholník, pole reťazcov rôznej dĺžky);
  dá sa len cez pole ukazovateľov alebo `int **`,
- pri odovzdaní do funkcie: statické `int m[][N]` (stĺpce musia byť známe), dynamické `int **p`,
- inicializácia: `int m[2][3] = {{1, 2, 3}, {4, 5, 6}};` alebo `int m[][3] = {1, 2, 3, 4, 5, 6};`.

::: quiz
Prečo pri `int **p` treba najprv uvoľniť `p[i]` a až potom `p`?
- [ ] na poradí nezáleží
- [x] po `free(p)` by sme stratili adresy riadkov — ostal by memory leak (a čítanie `p[i]` po free je chyba)
- [ ] `free(p)` uvoľní automaticky aj riadky
> `free` uvoľní len jeden blok. Riadky sú samostatné bloky a ich adresy sú uložené práve v `p`.
:::

::: drill d7-jagged

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

**Fibonacciho čísla** — rekurzia vs. iterácia:

```c
long fib_r(int n) {                    // krátke, ale exponenciálne pomalé:
    if (n < 2) return n;               // fib_r(40) volá samu seba stovky miliónov krát
    return fib_r(n - 1) + fib_r(n - 2);
}

long fib_i(int n) {                    // cyklus: n krokov, žiadny zásobník
    long a = 0, b = 1;
    for (int i = 0; i < n; i++) { long t = a + b; a = b; b = t; }
    return a;
}
```

- každé volanie si na **zásobníku** vyhradí miesto pre parametre a lokálne premenné — príliš hlboká
  rekurzia skončí pretečením zásobníka (segfault),
- rekurzia je prirodzená pre stromy, delenie problému na polovice (binárne vyhľadávanie), permutácie;
  jednoduché opakovanie je lepšie cyklom,
- **ladenie**: vypisujte parameter a hĺbku pri vstupe aj výstupe — `printf("%*sfib(%d)\n", hlbka * 2, "", n);`
  ukáže strom volaní odsadený podľa hĺbky.

::: quiz
Koľkokrát sa zavolá `fib_r` pri výpočte `fib_r(4)` (vrátane prvého volania)?
- [ ] 4
- [ ] 5
- [x] 9
- [ ] 16
> fib(4) → fib(3) + fib(2); fib(3) → fib(2) + fib(1); každé fib(2) → fib(1) + fib(0). Spolu 1 + 2 + 4 + 2 = 9 volaní.
:::

::: drill d7-recursion
## Konštantné premenné / Константы

```c
const double PI = 3.14159;      // hodnotu nemožno meniť
void vypis(const char *s);      // funkcia sľubuje, že reťazec nezmení
```

Pri ukazovateľoch záleží na tom, **kde** stojí `const`:

| zápis | meniť `*p` (údaj) | meniť `p` (adresu) |
|---|---|---|
| `const int *p` (= `int const *p`) — ukazovateľ na konštantu | nie | áno |
| `int *const p = &x;` — konštantný ukazovateľ | áno | nie |
| `const int *const p = &x;` | nie | nie |

Čítajte sprava doľava: `int *const p` = „p je konštantný ukazovateľ na int“.
Reťazcová konštanta `"ahoj"` sa nesmie meniť — preto `const char *s = "ahoj";`.
Na rozdiel od `#define` má `const` premenná typ a kompilátor ju kontroluje.

::: quiz
`int x = 1, y = 2; int *const p = &x;` Ktorý príkaz je **chybný**?
- [ ] `*p = 5;`
- [x] `p = &y;`
- [ ] `x = *p + 1;`
> `p` je konštantný ukazovateľ — adresu zmeniť nemožno, ale údaj, na ktorý ukazuje, áno.
:::

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

### Štruktúry vo funkciách a dynamická alokácia

```c
void vypis(OSOBA o);          // dostane KÓPIU celej štruktúry (pomalé pri veľkých štruktúrach)
void zvys(OSOBA *o);          // dostane adresu — môže meniť originál, kopíruje sa len adresa
void tlac(const OSOBA *o);    // adresa, ale bez možnosti zmeny

OSOBA *d = malloc(sizeof(OSOBA));    // dynamická štruktúra
d->vek = 20;                         // cez ukazovateľ vždy ->
free(d);

OSOBA tim[10];                       // pole štruktúr
tim[0].vek = 25;                     // prvok poľa je štruktúra → bodka
OSOBA *dt = malloc(n * sizeof(OSOBA));   // dynamické pole štruktúr
dt[i].vek = 30;                      // dt[i] je štruktúra → bodka; (dt + i)->vek je to isté
```

### Kopírovanie: plytká vs. hlboká kópia

Štruktúry **možno** kopírovať priradením `b = a;` (na rozdiel od polí) — skopíruje sa každý bajt,
aj pole vo vnútri štruktúry. Ak však štruktúra obsahuje **ukazovateľ**, skopíruje sa len adresa:

```c
typedef struct { char *meno; int vek; } OSOBA;

OSOBA b = a;                                // plytká kópia: b.meno == a.meno (ten istý blok!)
b.meno = malloc(strlen(a.meno) + 1);        // hlboká kópia: vlastná pamäť
strcpy(b.meno, a.meno);                     // ... a skopírovaný obsah
```

Pri plytkej kópii zmena `a.meno[0]` zmení aj `b.meno`, a dvojité `free` toho istého bloku je chyba.
Štruktúry sa nedajú porovnať `==` — porovnávajte položku po položke.

::: quiz
`typedef struct { char meno[20]; } A;` `A x = {"Eva"}, y = x; y.meno[0] = 'A';` Čo je v `x.meno`?
- [x] `Eva`
- [ ] `Ava`
- [ ] chyba kompilácie
> Pole **vo vnútri** štruktúry sa pri priradení skopíruje celé — `y` má vlastnú kópiu. Problém nastane až pri ukazovateli `char *meno`.
:::

::: drill d7-deepcopy

### enum a union podrobnejšie

```c
typedef enum { NEPRAVDA, PRAVDA } LOGICKA;           // 0, 1
enum farba { CERVENA = 1, ZELENA, MODRA = 10, BIELA }; // 1, 2, 10, 11 — pokračuje od poslednej

const char *nazvy[] = {"PONDELOK", "UTOROK", "STREDA"};
DEN d = UTOROK;
printf("%d %s\n", d, nazvy[d]);     // 1 UTOROK — meno položky sa dá vypísať len cez pole reťazcov
```

`union` má veľkosť **najväčšej** položky; v jednom okamihu platí len jedna z nich. Často sa
vkladá do štruktúry spolu s položkou, ktorá hovorí, čo je práve uložené:

```c
typedef struct {
    enum { CELE, REALNE } typ;
    union { int i; double d; } hodnota;
} CISLO;

CISLO c = { .typ = REALNE, .hodnota.d = 2.5 };
if (c.typ == REALNE) printf("%g\n", c.hodnota.d);
```

::: quiz
`enum { A, B = 5, C };` Akú hodnotu má `C`?
- [ ] 2
- [x] 6
- [ ] 0
> Bez explicitnej hodnoty položka pokračuje o 1 od predchádzajúcej: B = 5, C = 6.
:::

::: quiz
`union U { char c; int i; double d; };` Aká je typicky hodnota `sizeof(union U)`?
- [ ] 13
- [x] 8
- [ ] 1
> Položky zdieľajú pamäť, union je veľký ako najväčšia položka (`double` = 8 B).
:::

::: drill d7-struct

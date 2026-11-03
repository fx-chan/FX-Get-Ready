## Typová konverzia / Приведение типов

- **implicitná**: v `int + double` sa `int` automaticky prevedie na `double`,
- pri priradení do „menšieho“ typu sa môže stratiť informácia: `int i = 3.99;` → `i == 3`,
- **explicitná** (pretypovanie): `(double)a / b` — delenie prebehne reálne.

::: quiz
`int a = 7, b = 2;` Aká je hodnota `(double)(a / b)`?
- [ ] 3.5
- [x] 3.0
- [ ] 4.0
> Zátvorka sa vyhodnotí najprv: `7 / 2 == 3` (celočíselne), až potom sa 3 prevedie na `3.0`. Správne: `(double)a / b`.
:::

## Ukazovateľ / Указатель

Ukazovateľ je premenná, ktorá uchováva **adresu** inej premennej.

```c
int x = 10;
int *p = &x;      // & = adresa premennej x
*p = 20;          // * = dereferencia: zapíš na adresu, kam p ukazuje → x == 20
int *q = NULL;    // neukazuje nikam; neinicializovaný ukazovateľ je nebezpečný
printf("%p\n", (void *)p);   // výpis adresy
```

::: quiz
`int x = 3; int *p = &x; *p = *p + 4;` Akú hodnotu má `x`?
- [ ] 3
- [x] 7
- [ ] adresu x + 4
> `*p` je samotná premenná `x`; `x = 3 + 4`.
:::

::: drill d5-deref

### Ukazovateľ na ukazovateľ, void *, segmentation fault

```c
int x = 5;
int *p = &x;
int **pp = &p;         // adresa ukazovateľa
**pp = 7;              // *pp je p, **pp je x  →  x == 7

void *v = &x;          // generický ukazovateľ: môže ukazovať na čokoľvek
int *q = (int *)v;     // pred dereferenciou ho treba pretypovať; *v je chyba
double d = 2.5;
v = &d;                // ten istý void * teraz ukazuje na double
```

**Segmentation fault** = program siahol do pamäte, ktorá mu nepatrí. Typické príčiny:
dereferencia `NULL` alebo neinicializovaného ukazovateľa, zápis ďaleko za koniec poľa,
použitie pamäte po `free`, nekonečná rekurzia. Na tejto stránke sa prejaví ako chyba behu.

```c
int *p;          // neinicializovaný — ukazuje „niekam“
*p = 3;          // nedefinované správanie, často segfault
int *r = NULL;
*r = 3;          // vždy chyba
```

Viac ukazovateľov môže ukazovať na to isté miesto — zmena cez jeden je viditeľná cez všetky.

::: quiz
`int x = 1; int *p = &x; int **pp = &p;` Čo zmení `x` na 9?
- [ ] `*pp = 9;`
- [x] `**pp = 9;`
- [ ] `pp = 9;`
> `*pp` je ukazovateľ `p` (priradenie by zmenilo adresu), `**pp` je až samotné `x`.
:::

### Ukazovateľ na funkciu / Указатель на функцию

Meno funkcie je jej adresa. Ukazovateľ na funkciu umožní vybrať, ktorá funkcia sa zavolá, až za behu.

```c
int sucet(int a, int b) { return a + b; }

int (*f)(int, int);    // f je ukazovateľ na funkciu (int, int) -> int; zátvorky okolo *f sú nutné
f = sucet;             // alebo f = &sucet;
printf("%d\n", f(2, 3));          // alebo (*f)(2, 3)

int *g(int, int);      // POZOR: toto je funkcia, ktorá vracia int *
```

::: quiz
Čo deklaruje `double (*h)(double);`?
- [ ] funkciu `h`, ktorá vracia ukazovateľ na `double`
- [x] ukazovateľ `h` na funkciu, ktorá berie a vracia `double`
- [ ] pole `double`
> Zátvorky `(*h)` hovoria, že `h` je ukazovateľ; za ním nasleduje zoznam parametrov funkcie.
:::

::: drill d5-funcptr
## Odovzdanie odkazom / Передача по указателю

Funkcia môže zmeniť premennú volajúceho, ak dostane jej adresu — tak „vráti“ viac hodnôt naraz.

```c
void vymen(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}
...
vymen(&x, &y);
```

> **Nikdy** nevracajte adresu lokálnej premennej — po skončení funkcie zaniká.

::: drill d5-swap
::: drill d5-two-results
## Reťazce / Строки

Reťazec je pole `char` ukončené znakom `'\0'`. `"ahoj"` zaberá **5** bajtov.

```c
char s[20] = "ahoj";
char meno[50];
scanf("%49s", meno);           // jedno slovo, bez &, max 49 znakov
fgets(meno, sizeof meno, stdin);   // celý riadok vrátane '\n'
```

| `string.h` | význam |
|---|---|
| `strlen(s)` | dĺžka bez `'\0'` |
| `strcpy(dst, src)` | kopírovanie (dst musí byť dosť veľký) |
| `strcat(dst, src)` | pripojenie na koniec |
| `strcmp(a, b)` | 0 ak sú rovnaké, <0 / >0 podľa abecedy |
| `strchr(s, c)` | ukazovateľ na prvý výskyt znaku alebo `NULL` |
| `strstr(s, t)` | ukazovateľ na prvý výskyt podreťazca alebo `NULL` |

`ctype.h`: `isdigit`, `isalpha`, `isspace`, `toupper`, `tolower`.

::: quiz
Ako správne porovnať dva reťazce `a` a `b`? / Как сравнить строки?
- [ ] `a == b`
- [x] `strcmp(a, b) == 0`
- [ ] `strlen(a) == strlen(b)`
> `a == b` porovnáva adresy polí, nie obsah.
:::

Ďalšie funkcie z `string.h`: `strncpy`, `strncat`, `strncmp` (pracujú najviac s `n` znakmi —
časť reťazca), `strrchr` (posledný výskyt znaku — práca s reťazcom odzadu).

### Reťazcová konštanta vs. pole

```c
char pole[] = "ahoj";   // pole 5 znakov, obsah možno meniť: pole[0] = 'A';
char *s = "ahoj";       // ukazovateľ na konštantu v pamäti len na čítanie
// s[0] = 'A';          // nedefinované správanie (často pád)
const char *t = "ahoj"; // správny zápis — kompilátor zmenu zakáže
```

### Riadkový a formátovaný vstup/výstup z reťazca

| funkcia | čo robí |
|---|---|
| `fgets(s, n, stdin)` | načíta riadok (aj s `'\n'`), max `n-1` znakov — bezpečné |
| `puts(s)` | vypíše reťazec a pridá `'\n'` |
| `gets(s)` | **nepoužívať** — nekontroluje veľkosť, z jazyka bola odstránená |
| `sscanf(s, "%d", &x)` | ako `scanf`, ale číta z reťazca `s` |
| `sprintf(s, "%d", x)` | ako `printf`, ale zapisuje do reťazca `s` (`snprintf` s limitom veľkosti) |

```c
char riadok[100];
fgets(riadok, sizeof riadok, stdin);
riadok[strcspn(riadok, "\n")] = '\0';   // odstránenie '\n' na konci
```

::: drill d5-sscanf

### Prevod reťazca na číslo, kontrola znakov

```c
#include <stdlib.h>
int i = atoi("123");            // 123   (pri chybe vráti 0 — chybu nerozlíšite)
double d = atof("3.14");        // 3.14
char *koniec;
long l = strtol("42abc", &koniec, 10);   // 42, koniec ukazuje na "abc" — vieme, kde prevod skončil
```

`ctype.h`: `isdigit(c)` cifra, `isalpha(c)` písmeno, `isalnum(c)`, `isspace(c)` biely znak,
`isupper(c)`/`islower(c)`, `toupper(c)`/`tolower(c)` vráti zmenený znak.

### Pole reťazcov

```c
char mena[3][20] = {"Jan", "Eva", "Ola"};   // 2D pole znakov: 3 reťazce po max 19 znakov
const char *dni[] = {"Po", "Ut", "St"};      // pole ukazovateľov na reťazcové konštanty
printf("%s %c\n", mena[1], dni[2][0]);       // Eva S
```

### Časté chyby s reťazcami

- zabudnuté miesto pre `'\0'`: `char s[4] = "ahoj";` nemá ukončenie,
- `s = "text";` do poľa — treba `strcpy(s, "text");`,
- `scanf("%s", s)` bez obmedzenia dĺžky → pretečenie poľa; použite `%49s`,
- porovnanie `==` namiesto `strcmp`, `'a'` (znak) vs `"a"` (reťazec s 2 bajtmi).

::: quiz
Čo vráti `atoi("12abc")`?
- [ ] 0
- [x] 12
- [ ] chybu
> `atoi` prevedie úvodnú časť, ktorá vyzerá ako číslo, a zvyšok ignoruje. Kde prevod skončil, zistí len `strtol`.
:::

::: drill d5-strlen

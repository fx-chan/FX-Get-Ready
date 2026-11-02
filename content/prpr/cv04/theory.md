## Štandardný vstup a výstup / Стандартный ввод-вывод

Každý program má tri otvorené prúdy: `stdin` (klávesnica), `stdout` (obrazovka), `stderr` (chyby).

```c
int c = getchar();      // jeden znak zo stdin, na konci vstupu vráti EOF
putchar(c);             // jeden znak na stdout
```

> `getchar` vracia `int`, nie `char` — inak by sa `EOF` (-1) nedal odlíšiť od platného znaku.

```c
int c;
while ((c = getchar()) != EOF)   // klasický cyklus: čítaj až do konca vstupu
    putchar(c);
```

::: quiz
Prečo sa výsledok `getchar()` ukladá do `int`? / Почему результат `getchar()` хранят в `int`?
- [ ] je to rýchlejšie
- [x] aby sa dalo rozlíšiť `EOF` od bežných znakov
- [ ] `char` sa nedá porovnávať
> `EOF` je hodnota mimo rozsahu znakov (obvykle -1).
:::

## Práca so súbormi / Работа с файлами

```c
FILE *f = fopen("data.txt", "r");     // "r" čítanie, "w" zápis (prepíše), "a" pripisovanie
if (f == NULL) {                      // vždy kontrolujte!
    printf("Subor sa nepodarilo otvorit.\n");
    return 1;
}
int c;
while ((c = getc(f)) != EOF)          // getc/putc, fscanf/fprintf, fgets/fputs
    putchar(c);
fclose(f);                            // zatvoriť = zapísať buffer a uvoľniť súbor
```

| funkcia | čo robí |
|---|---|
| `getc(f)`, `putc(c, f)` | znak zo súboru / do súboru |
| `fscanf(f, "%d", &x)` | ako `scanf`, vracia počet načítaných položiek |
| `fprintf(f, "%d\n", x)` | ako `printf` |
| `fgets(buf, n, f)` | celý riadok (max `n-1` znakov), na konci vráti `NULL` |
| `rewind(f)` | späť na začiatok súboru |

Binárne súbory sa otvárajú s `"rb"`/`"wb"` a čítajú/zapisujú cez `fread`/`fwrite`.

::: quiz
Čo spraví `fopen("vystup.txt", "w")`, ak súbor už existuje?
- [ ] vráti NULL
- [ ] pridá text na koniec
- [x] súbor vyprázdni a zapisuje od začiatku
> Na pripisovanie na koniec slúži režim `"a"`.
:::

::: drill d4-fopen
::: drill d4-getc
::: drill d4-fscanf
## Funkcie v praxi / Функции на практике

Rozdeľte program na malé funkcie s jednou úlohou — napr. `zisti_prvocislo`, `reverzne_cislo`.
Funkcia, ktorá „odpovedá áno/nie“, zvyčajne vracia `1`/`0` (alebo podľa zadania `1`/`-1`).

```c
int je_parne(int n) {
    return n % 2 == 0;
}
```

::: drill d4-prime

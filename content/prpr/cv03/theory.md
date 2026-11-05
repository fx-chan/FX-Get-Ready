## Opakovanie: for vs. while

```c
for (inicializacia; podmienka; krok) { telo; }

inicializacia;                 // to isté cez while
while (podmienka) { telo; krok; }
```

## Návratová hodnota scanf

`scanf` vráti **počet úspešne načítaných položiek**, alebo `EOF` na konci vstupu.
Vďaka tomu vieme čítať, kým sú dáta — aj keď vopred nevieme, koľko ich je.

```c
int x, pocet = 0;
while (scanf("%d", &x) == 1)    // čítaj, kým sa darí načítať číslo
    pocet++;
```

::: quiz
Čo vráti `scanf("%d %d", &a, &b)` pre vstup `5 abc`?
- [ ] 2
- [x] 1
- [ ] 0
- [ ] EOF
> Prvé číslo sa načíta, `abc` nie je číslo — úspešne načítaná je jedna položka.
:::

::: drill d3-scanf-eof
## Opakované načítanie do-while

```c
int n;
do {
    scanf("%d", &n);
} while (n < 0);        // opakuj, kým nie je n nezáporné
```

## Vnorené cykly

```c
for (int r = 1; r <= n; r++) {        // riadky
    for (int s = 1; s <= r; s++)      // stĺpce
        printf("*");
    printf("\n");
}
```

::: drill d3-triangle
## Funkcie

Funkcia má **návratový typ**, **meno**, **parametre** a **telo**. Ak sa definuje až za `main`,
treba ju vopred **deklarovať** (prototyp).

```c
#include <stdio.h>

double obvod(double r);            // prototyp (deklarácia)

int main(void) {
    printf("%.2f\n", obvod(2.0));  // volanie
    return 0;
}

double obvod(double r) {           // definícia
    return 2 * 3.14 * r;
}
```

- parametre sa odovzdávajú **hodnotou** — funkcia dostane kópiu, originál nezmení,
- `void` funkcia nič nevracia; `return;` ju môže ukončiť skôr,
- lokálne premenné existujú len počas volania (okrem `static`).

::: quiz
Čo vypíše program?

```c
void zvys(int x) { x = x + 1; }
int main(void) { int a = 5; zvys(a); printf("%d", a); }
```
- [x] 5
- [ ] 6
- [ ] chyba kompilácie
> Funkcia dostala kópiu hodnoty. Na zmenu originálu treba ukazovateľ (Cvičenie 5).
:::

### Bloky a rozsah platnosti

Blok je časť kódu v `{ }`. Premenná definovaná v bloku platí **od miesta definície po koniec
bloku**. Vnútorný blok môže definovať premennú s rovnakým menom — tá potom **zakryje** vonkajšiu.

```c
int x = 1;                 // globálna
int main(void) {
    int x = 2;             // lokálna v main, zakryje globálnu
    {
        int x = 3;         // vnútorný blok
        printf("%d\n", x); // 3
    }
    printf("%d\n", x);     // 2
    for (int i = 0; i < 3; i++) { }
    // i tu už neexistuje
    return 0;
}
```

- `main` je tiež funkcia: vracia `int` (0 = úspech) a môže mať parametre `int argc, char *argv[]`,
- `return` ukončí funkciu okamžite (aj uprostred cyklu),
- funkciu definovanú až za miestom volania treba vopred deklarovať prototypom — inak GCC 15 hlási chybu.

::: quiz
Čo vypíše `int a = 1; { int a = 5; a++; } printf("%d", a);`?
- [x] 1
- [ ] 5
- [ ] 6
> Vnútorné `a` je iná premenná, ktorá zanikne na konci bloku. Vonkajšie `a` ostáva 1.
:::

::: drill d3-function
::: drill d3-void

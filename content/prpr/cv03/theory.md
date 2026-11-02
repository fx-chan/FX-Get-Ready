## Opakovanie: for vs. while

```c
for (inicializacia; podmienka; krok) { telo; }

inicializacia;                 // to isté cez while
while (podmienka) { telo; krok; }
```

## Návratová hodnota scanf / Возвращаемое значение scanf

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

## Vnorené cykly / Вложенные циклы

```c
for (int r = 1; r <= n; r++) {        // riadky
    for (int s = 1; s <= r; s++)      // stĺpce
        printf("*");
    printf("\n");
}
```

::: drill d3-triangle
## Funkcie / Функции

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
Čo vypíše program? / Что выведет программа?

```c
void zvys(int x) { x = x + 1; }
int main(void) { int a = 5; zvys(a); printf("%d", a); }
```
- [x] 5
- [ ] 6
- [ ] chyba kompilácie
> Funkcia dostala kópiu hodnoty. Na zmenu originálu treba ukazovateľ (Cvičenie 5).
:::

::: drill d3-function
::: drill d3-void

Načítajte reálne čísla `a b c` (`a ≠ 0`). Funkcia
`int kvadraticka_rovnica(double a, double b, double c, double *x1, double *x2)` vráti počet reálnych
koreňov rovnice `ax² + bx + c = 0` a korene cez ukazovatele (použite `sqrt` z `math.h`).

Výstup (čísla na 3 desatinné miesta, `x1 = (-b + √D) / 2a`, `x2 = (-b - √D) / 2a`):

```
Rovnica ma 2 korene: x1 = ..., x2 = ...
Rovnica ma 1 koren: x = ...
Rovnica nema realne korene
```

### Ukážky
```
1 5 6     →  Rovnica ma 2 korene: x1 = -2.000, x2 = -3.000
2 -4 2    →  Rovnica ma 1 koren: x = 1.000
```

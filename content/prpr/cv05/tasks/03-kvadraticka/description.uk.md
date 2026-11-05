Зчитайте дійсні числа `a b c` (`a ≠ 0`). Функція `int kvadraticka_rovnica(double a, double b, double c, double *x1, double *x2)` повертає кількість дійсних коренів рівняння `ax² + bx + c = 0` і корені через вказівники (використайте `sqrt` з `math.h`).

Вивід (числа з 3 знаками після коми, `x1 = (-b + √D) / 2a`, `x2 = (-b - √D) / 2a`):

```
Rovnica ma 2 korene: x1 = ..., x2 = ...
Rovnica ma 1 koren: x = ...
Rovnica nema realne korene
```

### Приклади
```
1 5 6     →  Rovnica ma 2 korene: x1 = -2.000, x2 = -3.000
2 -4 2    →  Rovnica ma 1 koren: x = 1.000
```

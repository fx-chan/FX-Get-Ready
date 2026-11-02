Vstupom je jeden riadok s **menom súboru**. Pre každý riadok súboru spočítajte výskyt jednotlivých
písmen (veľké a malé písmená nerozlišujte) a vypíšte tabuľku:

- hlavička: `  #` a potom písmená `A` až `Z`, každé na šírku 3 (`%3c`),
- pre každý riadok súboru: číslo riadku na šírku 3 (`%3d`) a počty písmen na šírku 3 (`%3d`).

### Ukážka vstupu
```
subor.txt
```
### Súbor subor.txt
```
Toto je ukazkovy subor.
V subore su pismena.
```
### Výstup
```
  #  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
  1  1  1  0  0  1  0  0  0  0  1  2  0  0  0  4  0  0  1  1  2  2  1  0  0  1  1
  2  1  1  0  0  2  0  0  0  1  0  0  0  1  1  1  1  0  1  3  0  2  1  0  0  0  0
```

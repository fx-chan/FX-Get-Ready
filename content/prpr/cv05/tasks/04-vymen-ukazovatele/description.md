Napíšte procedúru `void vymen_ukazovatele(int **pa, int **pb)`, ktorá vymení **ukazovatele**
(teda adresy, kam ukazujú), nie hodnoty premenných.

Program načíta hodnoty `a` a `b`, nastaví `int *pa = &a, *pb = &b;` a vypíše stav pred a po volaní.
Adresy sa pri každom spustení líšia, preto ich nevypisujte — stačia hodnoty:

### Ukážka vstupu
```
10 14
```
### Výstup
```
Pred: *pa = 10, *pb = 14
Po: *pa = 14, *pb = 10
a = 10, b = 14
```
Posledný riadok ukazuje, že samotné premenné `a`, `b` sa nezmenili.

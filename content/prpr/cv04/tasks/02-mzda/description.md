V prvom riadku je `n`, potom `n` riadkov s dvojicou reálnych čísel: hodinová mzda a počet
odpracovaných hodín. Pre každú dvojicu zavolajte funkciu `double tyzdenna_mzda(double h_mzda, double hod)`
a vypíšte riadok:

`Hod. mzda: m Euro/hod, hodin: h, spolu: s Euro`

Nadčasy (ako v ukážke zo zadania): prvých **40 hodín** sa platí normálne, hodiny **nad 40 až po 60**
s príplatkom **1,5×**, hodiny **nad 60** dvojnásobne (**2×**).

Na konci vypíšte `Celkova mzda: S Euro`. Všetky čísla na **2 desatinné miesta**.

### Ukážka vstupu
```
3
20 38
22 48
24 68
```
### Výstup
```
Hod. mzda: 20.00 Euro/hod, hodin: 38.00, spolu: 760.00 Euro
Hod. mzda: 22.00 Euro/hod, hodin: 48.00, spolu: 1144.00 Euro
Hod. mzda: 24.00 Euro/hod, hodin: 68.00, spolu: 2064.00 Euro
Celkova mzda: 3968.00 Euro
```

Čítajte znaky zo súboru `text.txt`, kým nenarazíte na `*`.

- `x` alebo `X` → vypíšte `Precital som X`
- `y` alebo `Y` → `Precital som Y`
- `#`, `$` alebo `&` → `Precital som riadiaci znak`
- `*` → `Koniec` a ukončite čítanie.

Nakoniec vypíšte `Pocet precitanych medzier: ` a počet medzier prečítaných pred `*`.

### Súbor text.txt
```
$ abc 5 xyz #
& Q *# abf
```
### Výstup
```
Precital som riadiaci znak
Precital som X
Precital som Y
Precital som riadiaci znak
Precital som riadiaci znak
Koniec
Pocet precitanych medzier: 6
```

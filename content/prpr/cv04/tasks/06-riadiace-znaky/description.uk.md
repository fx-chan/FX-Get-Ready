Читайте символи з файлу `text.txt`, доки не трапиться `*`.

- `x` або `X` → виведіть `Precital som X`
- `y` або `Y` → `Precital som Y`
- `#`, `$` або `&` → `Precital som riadiaci znak`
- `*` → `Koniec` і завершіть читання.

Наприкінці виведіть `Pocet precitanych medzier: ` і кількість пробілів, прочитаних до `*`.

### Файл text.txt
```
$ abc 5 xyz #
& Q *# abf
```
### Вивід
```
Precital som riadiaci znak
Precital som X
Precital som Y
Precital som riadiaci znak
Precital som riadiaci znak
Koniec
Pocet precitanych medzier: 6
```

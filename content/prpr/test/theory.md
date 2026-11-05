## Ako vyzerá počítačový test

Test (napr. skupina A_1_1) nadväzuje na **projekt č. 1**: do svojho odovzdaného projektu
doprogramujete nové funkcie, ktoré sa aktivujú stlačením klávesy (napr. `j`, `x`).

Pravidlá z ukážkového testu:

- pracujete **samostatne**, materiály ani Google nie sú povolené,
- **nepoužívajte globálne premenné, štruktúry ani `goto`**,
- dáta dostávajú funkcie **cez argumenty** (dynamické polia, 2D pole reťazcov `char **`),
- ak ste projekt neodovzdali, použijete predpísané hlavičky funkcií:

```c
void j(char **pole_Mer_Mod, char **pole_Typ_MV, double *hodnota, int velkost_pola);
void x(double *hodnota, int velkost_pola);
```

Tu sú obe úlohy upravené ako **samostatné programy**: `main` načíta dáta, ktoré by inak mal projekt
v pamäti, a zavolá vašu funkciu. Hodnotí sa rovnako — presný výstup.


## Na čo si dať pozor

1. **Presný formát výstupu** — počet desatinných miest (`%.4f`), medzery, bodky na konci viet.
2. **Ošetrenie vstupu** — „načítaj k, kým nie je kladné“: `scanf` môže vrátiť 0 (nečíselný vstup),
   vtedy treba zlé slovo preskočiť (`scanf("%*s")`), inak sa program zacyklí.
3. **Pomocné funkcie** — stredná hodnota, percentuálny rozdiel, výber hodnôt jedného modulu.
4. **Uvoľnenie pamäte** pre každý `malloc`.
5. Reálne čísla neporovnávajte cez `==`, cifry z čísla vyberajte cez zaokrúhlené celé číslo.

### Percentuálny rozdiel

**PR = (B · 100) / A − 100** — v C: `B * 100 / A - 100` (rozdiel **A voči B**).

::: drill dt-pr
::: quiz
Ako bezpečne zistiť **3. cifru za desatinnou čiarkou** čísla `x = 5.254254`?
- [ ] `(int)(x * 1000) % 10`
- [x] `(llround(x * 1e6) / 1000) % 10`
- [ ] `x % 1000`
> Násobenie reálnych čísel môže dať napr. `5254.2539999…`. Bezpečnejšie je zaokrúhliť na celé číslo
> s pevným počtom miest (`llround`) a pracovať s celými číslami. `%` sa na `double` nedá použiť.
:::

::: drill dt-digit
::: drill dt-strings

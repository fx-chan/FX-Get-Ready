Dva stavy sú **ekvivalentné**, ak pre ľubovoľnú vstupnú postupnosť dávajú rovnaký výstup. Ekvivalentné stavy
sa dajú zlúčiť. Hľadajú sa postupným delením: najprv podľa výstupov, potom podľa toho, kam vedú prechody.

| stav | $x = 0$ | $x = 1$ |
|---|---|---|
| $s_1$ | $s_2$ / 0 | $s_3$ / 0 |
| $s_2$ | $s_4$ / 1 | $s_3$ / 0 |
| $s_3$ | $s_2$ / 0 | $s_5$ / 1 |
| $s_4$ | $s_2$ / 1 | $s_5$ / 0 |
| $s_5$ | $s_4$ / 0 | $s_3$ / 1 |

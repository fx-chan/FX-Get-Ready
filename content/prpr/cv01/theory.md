## Algoritmus a paradigmy / Алгоритм и парадигмы

**Algoritmus** je presný postup, ktorý po konečnom počte krokov vyrieši úlohu. Požadované vlastnosti:

| vlastnosť | význam |
|---|---|
| jednoznačnosť | každý krok je presne definovaný |
| determinovanosť | nasledujúci krok je jednoznačne daný |
| rezultatívnosť | po konečnom počte krokov príde k výsledku |
| správnosť | výsledok je vždy korektný |
| efektívnosť | čo najmenej času a pamäte (často protichodné požiadavky) |

**Paradigmy programovania**: procedurálna (C, Pascal), objektovo-orientovaná (Java, C++),
funkcionálna (Lisp, Haskell), logická (Prolog). Jazyk C je **procedurálny**: program je postupnosť
príkazov, ktoré sa vykonávajú v zapísanom poradí, pokiaľ riadiaca štruktúra neurčí inak; údaje sú
v premenných, ktoré počas behu menia hodnotu.

::: quiz
Ktorá vlastnosť algoritmu hovorí, že po konečnom počte krokov musí prísť k výsledku?
- [ ] determinovanosť
- [x] rezultatívnosť
- [ ] efektívnosť
> Determinovanosť = ďalší krok je jednoznačne daný; efektívnosť = šetrí čas a pamäť.
:::

## Od zdrojáku k programu / От исходника к программе

Jazyk C je **kompilovaný**: zdrojový kód (`.c`) sa najprv preloží do strojového kódu a až potom sa spúšťa.
Си — компилируемый язык: исходник сначала переводится в машинный код, потом запускается.

| krok | čo robí | `gcc` prepínač | výsledok |
|---|---|---|---|
| 1. preprocesor | vloží `#include`, rozvinie `#define`, odstráni komentáre | `-E` | `.i` |
| 2. kompilátor | preloží C do assembleru | `-S` | `.s` |
| 3. assembler | assembler → strojový kód | `-c` | `.o` |
| 4. linker | spojí `.o` súbory a knižnice | (bez prepínača) | spustiteľný súbor |

```
gcc -Wall -o hello hello.c     # všetko naraz, výsledok: hello (hello.exe na Windows)
gcc -v hello.c                 # -v vypíše, čo gcc robí v každom kroku
./hello                        # spustenie
```

> Na tejto stránke kód kompiluje server (GCC 15) — stačí stlačiť **Skontrolovať** / **Odoslať**.
> Здесь код компилирует сервер (GCC 15) — просто нажмите кнопку проверки.

## Štruktúra programu / Структура программы

```c
#include <stdio.h>   // printf, scanf

int main(void) {
    printf("Hello world!\n");
    return 0;        // 0 = program skončil úspešne / программа завершилась успешно
}
```

- `#include <stdio.h>` — pripojí hlavičkový súbor štandardného vstupu/výstupu.
- `main` — vstupný bod programu. Vracia `int`.
- Každý príkaz končí bodkočiarkou `;`. `\n` je koniec riadku.
- Komentáre: `// do konca riadku` a `/* viac riadkov */`. Komentáre `/* */` sa **nedajú vnárať**:
  `/* a /* b */ c */` skončí pri prvom `*/` a `c */` je chyba.

::: quiz
Čo musí byť na konci (takmer) každého príkazu v C? / Чем заканчивается почти каждая инструкция?
- [ ] dvojbodka `:`
- [x] bodkočiarka `;`
- [ ] nový riadok
> Koniec riadku pre C nič neznamená — príkazy oddeľuje `;`.
:::

::: drill d1-hello
## Premenné a typy / Переменные и типы

Premenná má **typ**, **meno** a **hodnotu**. Pred použitím ju treba deklarovať.

| typ | veľkosť (typicky) | príklad | `printf` | `scanf` |
|-----|---|---------|----------|---------|
| `char` | 1 B | `'b'` | `%c` (znak), `%d` (kód) | `" %c"` |
| `int` | 4 B | `10`, `-3` | `%d` | `%d` |
| `long` | 4–8 B | `123456L` | `%ld` | `%ld` |
| `float` | 4 B | `3.14f` | `%f` | `%f` |
| `double` | 8 B | `3.14` | `%f`, `%lf`, `%g` | `%lf` |

```c
int i = 10, j = 15;
char c = 'b';
double x = 3.1415926535;
printf("i = %d j = %d\n", i, j);
printf("c = %c | %d\n", c, c);   // c = b | 98  -- znak je číslo z ASCII tabuľky
```

**Modifikátory typov**: `unsigned` (bez znamienka — uvoľnený bit zväčší kladný rozsah), `signed`
(predvolené), `short`, `long`, `long long`. Napr. `unsigned int` (`%u`), `long long` (`%lld`).

**Pravidlá pre mená**: začína písmenom alebo `_`, ďalej len písmená, číslice a `_`; rozlišujú sa
veľké a malé písmená (`pom`, `Pom`, `POM` sú tri premenné); nesmie to byť kľúčové slovo (`int for;`
je chyba). Mená začínajúce `_` nechajte systému.

**Globálne a lokálne premenné**: premenná definovaná mimo funkcií je **globálna** — vidí ju celý
program. Premenná definovaná v bloku `{ }` je **lokálna** — existuje len v tom bloku.

```c
int pocitadlo;          // globálna, automaticky inicializovaná na 0

int main(void) {
    int j = 5;          // lokálna v main; bez inicializácie by mala náhodnú hodnotu
    pocitadlo++;
    return 0;
}
```

::: quiz
Ktoré meno premennej je **neplatné**? / Какое имя переменной недопустимо?
- [ ] `_pom`
- [ ] `pocet2`
- [x] `2pocet`
- [ ] `PocetZnakov`
> Meno nesmie začínať číslicou. `_pom` je platné, ale je vyhradené skôr pre systém.
:::

::: quiz
Akým formátom načítame `double` cez `scanf`? / Каким форматом читать `double`?
- [ ] `%f`
- [x] `%lf`
- [ ] `%d`
- [ ] `%c`
> `scanf` potrebuje vedieť presnú veľkosť: `%f` je pre `float`, `%lf` pre `double`. (V `printf` funguje pre `double` aj `%f`.)
:::

## Vstup a výstup / Ввод и вывод

`scanf` potrebuje **adresu** premennej — preto `&`. `printf` dostáva **hodnotu**.

```c
int a, b;
scanf("%d %d", &a, &b);          // načíta dve celé čísla
printf("Sucet: %d\n", a + b);    // výraz rovno v printf, bez pomocnej premennej
```

Formátovanie čísel / форматирование:

```c
double x = 3.14159;
printf("%.2f\n", x);    // 3.14       2 desatinné miesta
printf("%8.3f|\n", x);  //    3.142|  šírka 8
printf("%g\n", 2.50);   // 2.5        len platné desatinné miesta
printf("%3d|\n", 7);    //   7|       celé číslo na 3 miesta
printf("100%%\n");      // 100%       znak % sa píše ako %%
```

Escape sekvencie: `\n` nový riadok, `\t` tabulátor, `\\` spätné lomítko, `\"` úvodzovky, `\'` apostrof.

::: quiz
Čo vypíše `printf("%.1f", 2.25 * 2);`?
- [ ] `4.50`
- [x] `4.5`
- [ ] `4`
- [ ] `5.0`
> `%.1f` = jedno desatinné miesto; 2.25 · 2 = 4.5.
:::

::: drill d1-scanf
::: drill d1-format
## Operátory / Операторы

- aritmetické: `+ - * / %` — pozor: `/` medzi dvoma `int` je **celočíselné delenie**: `7 / 2 == 3`, `7 % 2 == 1`
- `7 / 2.0 == 3.5` — stačí, aby jeden operand bol reálny
- inkrement / dekrement: `i++` (najprv použije, potom zvýši), `++i` (najprv zvýši)
- priradenie je výraz: `a = b = 5;`, skrátené: `a += 3;` `a %= b;`
- relačné `< <= > >= == !=` a logické `&& || !` vracajú `1` (pravda) alebo `0` (nepravda)

::: quiz
Akú hodnotu má výraz `7 / 2 * 2`? / Чему равно `7 / 2 * 2`?
- [ ] 7
- [x] 6
- [ ] 7.0
- [ ] 8
> `7 / 2` je celočíselné delenie = 3, potom `3 * 2 = 6`.
:::

::: quiz
Platí `int i = 5; int k = i++ + 1;`. Aké sú hodnoty?
- [x] `k == 6`, `i == 6`
- [ ] `k == 7`, `i == 6`
- [ ] `k == 6`, `i == 5`
> `i++` vráti pôvodnú hodnotu 5 a až potom zvýši `i` na 6.
:::

### Bitové operátory / Битовые операторы

Pracujú s jednotlivými bitmi čísla (nepliesť si s logickými `&&`, `||`, `!`):

| operátor | význam | príklad (4-bitovo) |
|---|---|---|
| `&` | AND — 1, ak sú oba bity 1 | `0011 & 0101 = 0001` |
| `|` | OR — 1, ak je aspoň jeden bit 1 | `0011 | 0101 = 0111` |
| `^` | XOR — 1, ak sú bity rôzne | `0011 ^ 0101 = 0110` |
| `~` | negácia každého bitu | `~0101 = 1010` |
| `<<` | posun doľava (= násobenie 2ⁿ) | `0101 << 2 = 10100` (5 → 20) |
| `>>` | posun doprava (= celočíselné delenie 2ⁿ) | `0101 >> 1 = 0010` (5 → 2) |

```c
unsigned n = 5;                 // 101
int bit = (n >> k) & 1;         // hodnota k-teho bitu
n = n | (1u << k);              // nastav k-ty bit na 1
n = n & ~(1u << k);             // vynuluj k-ty bit
```

::: quiz
Akú hodnotu má `6 & 3`? / Чему равно `6 & 3`?
- [x] 2
- [ ] 1
- [ ] 7
- [ ] 9
> `110 & 011 = 010` = 2. Pozor: `6 && 3` by bolo 1 (logické AND), `6 | 3` = 7.
:::

::: drill d1-bits

## Podmienka if / Условие if

```c
char c;
scanf(" %c", &c);                 // medzera pred %c preskočí biele znaky
if (c >= 'A' && c <= 'Z')         // je to veľké písmeno?
    c = c + 'a' - 'A';            // zmena na malé (posun v ASCII)
else
    printf("Nie je velke.\n");
```

Viac príkazov vo vetve → zložené zátvorky `{ }`.

::: drill d1-if

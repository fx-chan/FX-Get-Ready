## Typová konverzia / Приведение типов

- **implicitná**: v `int + double` sa `int` automaticky prevedie na `double`,
- pri priradení do „menšieho“ typu sa môže stratiť informácia: `int i = 3.99;` → `i == 3`,
- **explicitná** (pretypovanie): `(double)a / b` — delenie prebehne reálne.

::: quiz
`int a = 7, b = 2;` Aká je hodnota `(double)(a / b)`?
- [ ] 3.5
- [x] 3.0
- [ ] 4.0
> Zátvorka sa vyhodnotí najprv: `7 / 2 == 3` (celočíselne), až potom sa 3 prevedie na `3.0`. Správne: `(double)a / b`.
:::

## Ukazovateľ / Указатель

Ukazovateľ je premenná, ktorá uchováva **adresu** inej premennej.

```c
int x = 10;
int *p = &x;      // & = adresa premennej x
*p = 20;          // * = dereferencia: zapíš na adresu, kam p ukazuje → x == 20
int *q = NULL;    // neukazuje nikam; neinicializovaný ukazovateľ je nebezpečný
printf("%p\n", (void *)p);   // výpis adresy
```

::: quiz
`int x = 3; int *p = &x; *p = *p + 4;` Akú hodnotu má `x`?
- [ ] 3
- [x] 7
- [ ] adresu x + 4
> `*p` je samotná premenná `x`; `x = 3 + 4`.
:::

::: drill d5-deref
## Odovzdanie odkazom / Передача по указателю

Funkcia môže zmeniť premennú volajúceho, ak dostane jej adresu — tak „vráti“ viac hodnôt naraz.

```c
void vymen(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}
...
vymen(&x, &y);
```

> **Nikdy** nevracajte adresu lokálnej premennej — po skončení funkcie zaniká.

::: drill d5-swap
::: drill d5-two-results
## Reťazce / Строки

Reťazec je pole `char` ukončené znakom `'\0'`. `"ahoj"` zaberá **5** bajtov.

```c
char s[20] = "ahoj";
char meno[50];
scanf("%49s", meno);           // jedno slovo, bez &, max 49 znakov
fgets(meno, sizeof meno, stdin);   // celý riadok vrátane '\n'
```

| `string.h` | význam |
|---|---|
| `strlen(s)` | dĺžka bez `'\0'` |
| `strcpy(dst, src)` | kopírovanie (dst musí byť dosť veľký) |
| `strcat(dst, src)` | pripojenie na koniec |
| `strcmp(a, b)` | 0 ak sú rovnaké, <0 / >0 podľa abecedy |
| `strchr(s, c)` | ukazovateľ na prvý výskyt znaku alebo `NULL` |
| `strstr(s, t)` | ukazovateľ na prvý výskyt podreťazca alebo `NULL` |

`ctype.h`: `isdigit`, `isalpha`, `isspace`, `toupper`, `tolower`.

::: quiz
Ako správne porovnať dva reťazce `a` a `b`? / Как сравнить строки?
- [ ] `a == b`
- [x] `strcmp(a, b) == 0`
- [ ] `strlen(a) == strlen(b)`
> `a == b` porovnáva adresy polí, nie obsah.
:::

::: drill d5-strlen

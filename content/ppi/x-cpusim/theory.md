> Príprava na priebežný test v CPUSime: za 100 minút napísať v assembleri simuláciu jednoduchej hry (Sokoban, Tetris, Hadík …). Lekcia prejde inštrukcie a adresovanie, typické konštrukcie a kostru riešenia; úlohy idú od krátkych cyklov po celé hry z minulých testov.

## Ako test vyzerá

- Riešite v **základnom Simulátore** CPUSimu (von Neumann, 2048 slov po 32 bitoch). Program patrí do buniek **0 – 1023**, údaje sú od **1024**.
- Vstupné údaje (rozmery, matice, postupnosť príkazov) sú už v pamäti testu, programová oblasť je prázdna. Zadanie presne určí, na ktoré adresy zapísať výsledky a ktoré bunky sú voľné na vaše premenné.
- Program musí fungovať pre **všetky povolené vstupy** — skúšajúci ho spustí aj na iných údajoch než na príklade. Pevné rozmery v programe sú istá strata bodov.
- Na konci otvoríte **Riešenie na odovzdanie → Kopírovať** a celý text (hlavička, PROGRAM, DATA, END) vložíte do odpovede v UIS bez úprav.

### Práca v simulátore

- **Ctrl+E** otvorí textový editor: vľavo pamäť inštrukcií (od 0), vpravo pamäť údajov (od 1024). Každý riadok je jedna bunka, prázdny riadok je prázdna bunka, riadok iba s komentárom bunku nezaberá.
- Pri teste zapisujte len **„Zapísať do pamäte inštrukcií“** — „Zapísať všetko“ by prepísalo pripravené údaje.
- **F8** (rýchla simulácia) vykoná naraz nastavený počet mikroinštrukcií (predvolene 2000). Dlhší program treba spustiť viackrát alebo počet zvýšiť v nastavení intervalov. **F7** vykoná jednu inštrukciu, **Ctrl+B** nastaví bod prerušenia.
- Simulácia mení pamäť. Pred ďalším spustením vráťte pamäť na stav pred simuláciou (tlačidlo so šípkou späť), inak program beží na už zmenených údajoch.

## Procesor a inštrukcie

Procesor má akumulátor **ACC**, počítadlo inštrukcií **PC**, register inštrukcie **IR**, adresový register **MAR**, údajový register **MBR** a stavový register **SR** s príznakmi C, V, N, Z. Takmer všetko ide cez ACC: načítaj, prepočítaj, ulož.

Inštrukcia má 32 bitov: operand (24 bitov), spôsob adresovania (2 bity) a operačný kód (6 bitov).

| skupina | inštrukcie | čo robia |
|---|---|---|
| presun | `LOAD x`, `STORE x` | ACC ← operand, pamäť ← ACC |
| aritmetika | `ADD`, `SUB`, `MUL`, `DIV` | ACC ← ACC op operand (DIV celočíselne) |
| o jednu | `INC`, `DEC` | ACC ± 1, bez operandu |
| bitové | `AND`, `OR`, `XOR`, `NOT` | po bitoch |
| posuny | `ROL`, `ROR`, `RLV`, `RRV` | posun ACC o bit (ROL = násobenie dvoma) |
| porovnanie | `CMP x` | C ← 1, ak ACC = operand, inak 0; ACC sa nemení |
| skoky | `JMP`, `JZ`, `JNZ`, `JC`, `JNC` | vždy / ak ACC = 0 / ak ACC ≠ 0 / ak C = 1 / ak C = 0 |
| ostatné | `HALT`, `NOP`, `CLSR` | koniec, nič, vynulovanie SR |

Do kódu sa dajú písať **návestia** (`slucka:` pred inštrukciou) a **komentáre** za bodkočiarkou. Čísla aj ako `0x1F` či `0b101`.

::: quiz
Čo urobí `CMP 1026`, ak je v ACC hodnota 5 a v bunke 1026 tiež 5?
- [ ] vynuluje ACC
- [x] nastaví príznak C na 1 a ACC nechá tak
- [ ] skočí na adresu 1026
> CMP iba porovná na rovnosť a výsledok uloží do C; na rozhodnutie treba ešte JC alebo JNC.
:::

## Tri spôsoby adresovania

| zápis | názov | operand je |
|---|---|---|
| `LOAD #5` | okamžitý | samotné číslo 5 |
| `LOAD 1025` | priamy | obsah bunky 1025 |
| `LOAD [1050]` alebo `LOAD @1050` | nepriamy | obsah bunky, ktorej adresa je v bunke 1050 |

Nepriame adresovanie je kľúč k poliam a maticiam: v pracovnej bunke držíme **ukazovateľ** (adresu prvku) a cez `[ ]` čítame alebo zapisujeme prvok, na ktorý ukazuje. Posun na ďalší prvok = zvýšiť ukazovateľ.

`STORE` nemá okamžitý tvar (do čísla sa zapisovať nedá); `STORE [p]` zapíše ACC na adresu uloženú v `p`.

::: drill d10-adresovanie

::: quiz
V bunke 1050 je 1203 a v bunke 1203 je 4. Čo je v ACC po `LOAD [1050]`?
- [ ] 1050
- [ ] 1203
- [x] 4
> Nepriamo: najprv sa prečíta adresa 1203 z bunky 1050, potom hodnota z bunky 1203.
:::

## Najčastejšia chyba: skoky bez mriežky

Skoky berú cieľ ako operand rovnako ako LOAD. Preto:

- `JMP #slucka` skočí na návestie `slucka` — **toto chceme takmer vždy**;
- `JMP slucka` skočí na adresu, ktorá je **uložená v bunke** `slucka` (tam je však zakódovaná inštrukcia, takže procesor odskočí kamsi do neznáma).

To isté platí pre `JZ`, `JNZ`, `JC`, `JNC`. Keď program „robí nezmysly“ hneď po prvom skoku, skontrolujte mriežky.

::: quiz
Program obsahuje `JNZ slucka`. Kam skočí, ak ACC ≠ 0?
- [ ] na inštrukciu s návestím `slucka`
- [x] na adresu uloženú v bunke `slucka`
- [ ] nikam, je to syntaktická chyba
> Bez # je priame adresovanie: cieľ sa prečíta z pamäte. Správne je `JNZ #slucka`.
:::

## Podmienky

CPUSim nemá skok „ak je menšie“. Podmienky sa skladajú z toho, čo je:

| podmienka | kód |
|---|---|
| x = 0 | `LOAD x`, `JZ #ano` |
| x = k (konštanta) | `LOAD x`, `CMP #k`, `JC #ano` |
| x = y | `LOAD x`, `CMP y`, `JC #ano` |
| x = R + 1 | `LOAD x`, `SUB R`, `DEC`, `JZ #ano` |
| x < y (malé čísla) | `LOAD x`, `SUB y`, `AND #-8388608`, `JNZ #ano` |

Posledný riadok: rozdiel je záporný práve vtedy, keď má nastavený najvyšší bit; `#-8388608` má jednotky v horných deviatich bitoch, takže AND je nenulový iba pre záporné čísla (pri rozdieloch menších ako $2^{23}$).

V simuláciách hier väčšinou stačí rovnosť: súradnica je mimo mapy, keď je **0** alebo **R + 1** (resp. C + 1), lebo sa mení vždy len o 1.

Pozor, `STORE` hodnotu v ACC nezmení, ale `CMP` mení príznak C. Po `CMP` preto skáčte hneď.

::: drill d10-porovnanie

::: quiz
Robot je v riadku 1 a dostane príkaz „hore“. Nový riadok je 0. Ako to zistíte najjednoduchšie?
- [ ] `CMP #-1` a `JC`
- [x] `LOAD nove_r` a `JZ #mimo`
- [ ] `AND #1` a `JNZ`
> Riadky sa číslujú od 1, takže 0 znamená mimo mapy a JZ to otestuje bez porovnania.
:::

## Cyklus cez postupnosť so značkou −1

Príkazy hry ležia za sebou od nejakej adresy a končia hodnotou −1. Kostra:

```
        LOAD #1200
        STORE 1950      ; ukazovatel na aktualny prikaz
cyklus: LOAD [1950]
        CMP #-1
        JC #koniec      ; znacka - koniec simulacie
        ...             ; spracovanie prikazu (je v ACC)
        LOAD 1950
        INC
        STORE 1950
        JMP #cyklus
koniec: ...             ; zapis vystupov
        HALT
```

Rozvetvenie podľa kódu príkazu: `CMP #1`, `JC #hore`, `CMP #2`, `JC #dole` … — ACC sa pri CMP nemení, takže porovnávať možno viackrát za sebou. Ak sa kód dá použiť ako posun adresy (počítadlo príkazu $k$ na $1040 + k$), vetvenie netreba vôbec.

::: drill d10-sucet

## Matice v pamäti

Matica $R \times C$ uložená po riadkoch od adresy $Z$: políčko $(r, c)$ (číslované od 1) je na
$$Z + (r-1) \cdot C + (c-1)$$

```
        LOAD r
        DEC
        MUL 1026        ; (r-1)*C
        ADD c
        ADD #1099       ; + (c-1) + 1100
        STORE 1960      ; adresa policka
        LOAD [1960]     ; hodnota policka
```

Susedia políčka s adresou $A$: vľavo $A - 1$, vpravo $A + 1$, hore $A - C$, dole $A + C$. Ak sú v pamäti dve matice rovnakého tvaru (terén od 1100, debny od 1800), to isté políčko je v druhej o **rozdiel začiatkov** ďalej (tu +700).

V teste si vždy prečítajte presný vzorec — v Tetrise bolo $1100 + (r-1) \cdot C + c$, teda matica začínala na 1101.

::: quiz
Matica má $C = 6$ stĺpcov. Políčko má adresu 1123. Aká je adresa políčka priamo pod ním?
- [ ] 1124
- [x] 1129
- [ ] 1117
> O riadok nižšie = o C buniek ďalej: 1123 + 6.
:::

## Kostra simulácie hry

Všetky testy majú rovnakú stavbu, mení sa len to, čo sa deje pri jednom príkaze:

1. **Inicializácia.** Počiatočnú polohu skopírujte do pracovných buniek, počítadlá vynulujte, ukazovateľ nastavte na prvý príkaz. Ak treba, prejdite maticu a zistite súčty (počet debien, jabĺk, debien na cieli).
2. **Kontrola pred prvým príkazom** (napr. výhra už na začiatku).
3. **Hlavný cyklus:** prečítaj príkaz, ak −1 → koniec; zvýš čas; vypočítaj novú polohu; skontroluj okraje a obsah matíc; ak sa dá, presuň a uprav počítadlá; skontroluj koniec hry; posuň ukazovateľ.
4. **Výstupy:** prepíšte počítadlá a polohu na adresy zo zadania a `HALT`.

Užitočné triky:

- **Smer ako dvojica** $(dr, dc)$ a posun adresy $d = dr \cdot C + dc$ — políčko pred hráčom je $P + d$, za debnou $P + 2d$. MUL aj ADD fungujú so zápornými číslami.
- **Novú polohu počítajte bokom** a do skutočnej zapíšte až po všetkých kontrolách — zablokovaný pohyb potom nič nepokazí.
- **Zoznam (telo hadíka)** ako dvojice od 1800: článok $i$ na $1800 + 2i$. Posun tela ide od chvosta: článok $i$ dostane hodnoty článku $i - 1$.
- Výstupy zapisujte až na konci jedným blokom — každá vetva končenia hry skočí na rovnaké návestie.

::: quiz
Príkaz sa nedá vykonať, lebo by hráč vošiel do steny. Čo sa podľa typického zadania zvýši?
- [x] iba simulačný čas
- [ ] čas aj počet krokov
- [ ] nič
> Čas počíta spracované príkazy (aj zablokované), kroky iba skutočné presuny.
:::

## Ladenie a kontrola pred odovzdaním

- Program, ktorý dôjde na prázdnu bunku, skončí chybou — chýba `HALT` alebo skok späť do cyklu.
- Hlásenie „Čítanie z prázdnej bunky“ znamená, že program číta premennú, do ktorej ešte nič nezapísal (alebo zlú adresu).
- Hlásenie „Zápis do pamäte inštrukcií“ znamená zápis pod adresu 1024 — takmer vždy chyba v adrese.
- Vyskúšajte okrajové prípady: prázdnu postupnosť (−1 hneď na začiatku), pohyb na okraj mapy, koniec hry pred značkou, minimálne a maximálne rozmery.
- Bod prerušenia na začiatok hlavného cyklu a F8 ukážu stav po každom príkaze.

::: quiz
Program má vypočítať výsledok pre mapu ľubovoľného rozmeru. Kde má brať počet stĺpcov?
- [ ] z konštanty `#7`, ak je v príklade C = 7
- [x] z bunky so vstupným parametrom (napr. `MUL 1026`)
- [ ] z počtu riadkov programu
> Skúšajúci spúšťa program aj na iných mapách; rozmery sa vždy čítajú z pamäte.
:::

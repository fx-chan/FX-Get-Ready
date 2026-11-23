### Postup

1. Premenné v pracovnej oblasti: poloha hráča, počítadlá, ukazovateľ príkazov a **P** — adresa terénu
   pod hráčom ($1100 + (r-1) \cdot C + (c-1)$). Pre každý príkaz sa vypočíta smer $(dr, dc)$ a posun adresy
   $d = dr \cdot C + dc$ (MUL funguje aj so zápornými číslami).
2. Šmyk je cyklus: nové $r$, $c$ sa skontrolujú voči okrajom (0 a $R + 1$, resp. $C + 1$ — porovnanie cez
   `SUB 1025`, `DEC`, `JZ`), potom terén na $P + d$. Ak sa dá ísť, zapíše sa nová poloha a $P \leftarrow P + d$.
3. Minca je o 700 ďalej než terén ($1800 - 1100$); zoberie sa cez `STORE [adresa]`.
4. Ak je na novom políčku východ, zvýši sa počet ťahov, nastaví výhra a skočí sa na zápis výstupov.
5. Pri náraze sa ťah započíta, iba ak sa hráč pohol (príznak v pracovnej bunke).

Pozor na skoky: `JMP #slide`, nie `JMP slide` — bez mriežky by sa skočilo na adresu uloženú v bunke `slide`.

### Vzorové riešenie

```
; Klzisko - premenne v pracovnej oblasti od 1900
; 1900 r, 1901 c, 1902 mince, 1903 tahy, 1904 cas, 1905 vyhra, 1906 dr, 1907 dc
; 1908 nr, 1909 nc, 1910 ukazovatel prikazov, 1911 prikaz, 1912 pohol sa?, 1913 T,
; 1914 P = adresa terenu pod hracom, 1915 d = dr*C + dc, 1916 adresa mince
        LOAD 1027
        STORE 1900
        LOAD 1028
        STORE 1901
        LOAD #0
        STORE 1902
        STORE 1903
        STORE 1904
        STORE 1905
        LOAD #1200
        STORE 1910
        LOAD 1900
        DEC
        MUL 1026
        ADD 1901
        ADD #1099
        STORE 1914
main:   LOAD [1910]
        CMP #-1
        JC #out
        STORE 1911
        LOAD 1904
        INC
        STORE 1904
        LOAD 1911
        JZ #next
        CMP #1
        JC #up
        CMP #2
        JC #down
        CMP #3
        JC #left
        LOAD #0
        STORE 1906
        LOAD #1
        STORE 1907
        JMP #dirok
up:     LOAD #-1
        STORE 1906
        LOAD #0
        STORE 1907
        JMP #dirok
down:   LOAD #1
        STORE 1906
        LOAD #0
        STORE 1907
        JMP #dirok
left:   LOAD #0
        STORE 1906
        LOAD #-1
        STORE 1907
dirok:  LOAD 1906
        MUL 1026
        ADD 1907
        STORE 1915
        LOAD #0
        STORE 1912
slide:  LOAD 1900
        ADD 1906
        STORE 1908
        JZ #stop
        SUB 1025
        DEC
        JZ #stop
        LOAD 1901
        ADD 1907
        STORE 1909
        JZ #stop
        SUB 1026
        DEC
        JZ #stop
        LOAD 1914
        ADD 1915
        STORE 1913
        LOAD [1913]
        CMP #1
        JC #stop
        LOAD 1908
        STORE 1900
        LOAD 1909
        STORE 1901
        LOAD 1913
        STORE 1914
        LOAD #1
        STORE 1912
        LOAD 1913
        ADD #700
        STORE 1916
        LOAD [1916]
        JZ #exit
        LOAD #0
        STORE [1916]
        LOAD 1902
        INC
        STORE 1902
exit:   LOAD [1913]
        CMP #2
        JNC #slide
        LOAD 1903
        INC
        STORE 1903
        LOAD #1
        STORE 1905
        JMP #out
stop:   LOAD 1912
        JZ #next
        LOAD 1903
        INC
        STORE 1903
next:   LOAD 1910
        INC
        STORE 1910
        JMP #main
out:    LOAD 1902
        STORE 1040
        LOAD 1903
        STORE 1041
        LOAD 1904
        STORE 1042
        LOAD 1905
        STORE 1043
        LOAD 1900
        STORE 1044
        LOAD 1901
        STORE 1045
        HALT
```

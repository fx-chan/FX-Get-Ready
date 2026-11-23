### Порядок дій

1. Змінні в робочій області: позиція гравця, лічильники, вказівник команд і **P** — адреса місцевості під гравцем ($1100 + (r-1) \cdot C + (c-1)$). Для кожної команди обчислюється напрям $(dr, dc)$ і зсув адреси $d = dr \cdot C + dc$ (MUL працює й з від'ємними числами).
2. Ковзання — це цикл: нові $r$, $c$ перевіряються щодо країв (0 і $R + 1$, відповідно $C + 1$ — порівняння через `SUB 1025`, `DEC`, `JZ`), потім місцевість на $P + d$. Якщо йти можна, записується нова позиція й $P \leftarrow P + d$.
3. Монета лежить на 700 далі від місцевості ($1800 - 1100$); забирається через `STORE [adresa]`.
4. Якщо на новій клітинці вихід, збільшується кількість ходів, встановлюється перемога й відбувається перехід на запис виходів.
5. У разі зіткнення хід враховується лише тоді, коли гравець зрушив (прапорець у робочій комірці).

Остерігайтеся переходів: `JMP #slide`, а не `JMP slide` — без # відбувся б перехід на адресу, збережену в комірці `slide`.

### Зразкове розв'язання

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

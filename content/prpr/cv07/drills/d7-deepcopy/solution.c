#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *meno;
    int vek;
} OSOBA;

OSOBA kopia(const OSOBA *o) {
    OSOBA k = *o;           // plytká kópia: k.meno ukazuje na tú istú pamäť
    k.meno = malloc(strlen(o->meno) + 1);
    strcpy(k.meno, o->meno);
    return k;
}

int main(void) {
    char buf[100];
    OSOBA a;
    scanf("%99s %d", buf, &a.vek);
    a.meno = malloc(strlen(buf) + 1);
    strcpy(a.meno, buf);

    OSOBA b = kopia(&a);
    a.meno[0] = 'X';        // zmena originálu
    a.vek++;

    printf("%s %d\n%s %d\n", a.meno, a.vek, b.meno, b.vek);
    if (b.meno != a.meno) free(b.meno);
    free(a.meno);
    return 0;
}

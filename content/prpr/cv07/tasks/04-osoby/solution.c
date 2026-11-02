#include <stdio.h>
#include <string.h>

typedef struct {
    char meno[101];
    char ulica[101];
    char psc[11];
    char telefon[21];
} OSOBA;

void citaj_riadok(char *s, int n) {
    if (fgets(s, n, stdin) == NULL) {
        s[0] = '\0';
        return;
    }
    s[strcspn(s, "\r\n")] = '\0';
}

int main(void) {
    OSOBA osoby[10];
    int n;
    char riadok[32];
    citaj_riadok(riadok, sizeof riadok);
    sscanf(riadok, "%d", &n);
    for (int i = 0; i < n; i++) {
        citaj_riadok(osoby[i].meno, sizeof osoby[i].meno);
        citaj_riadok(osoby[i].ulica, sizeof osoby[i].ulica);
        citaj_riadok(osoby[i].psc, sizeof osoby[i].psc);
        citaj_riadok(osoby[i].telefon, sizeof osoby[i].telefon);
    }
    for (int i = 0; i < n; i++)
        printf("%d. %s, %s, %s, tel. %s\n", i + 1, osoby[i].meno, osoby[i].ulica, osoby[i].psc, osoby[i].telefon);
    return 0;
}

#include <stdio.h>

int main(void) {
    char riadok[100], vysledok[100] = "";
    int r = 0, m = 0, d = 0;
    fgets(riadok, sizeof riadok, stdin);
    sscanf(riadok, "%d-%d-%d", &r, &m, &d);
    sprintf(vysledok, "%d.%d.%d", d, m, r);
    printf("%s\n", vysledok);
    return 0;
}

#include <stdio.h>

int main(void) {
    char riadok[100], vysledok[100] = "";
    int r = 0, m = 0, d = 0;
    fgets(riadok, sizeof riadok, stdin);
    /* DOPLŇ: sscanf z riadok do r, m, d a sprintf do vysledok */
    printf("%s\n", vysledok);
    return 0;
}

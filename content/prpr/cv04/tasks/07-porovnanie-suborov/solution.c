#include <stdio.h>

int main(void) {
    FILE *a = fopen("prvy.txt", "r");
    FILE *b = fopen("druhy.txt", "r");
    int ca, cb, rozne = 0, navyse = 0;
    while (1) {
        ca = getc(a);
        cb = getc(b);
        if (ca == EOF || cb == EOF)
            break;
        if (ca != cb)
            rozne++;
    }
    while (ca != EOF) { navyse++; ca = getc(a); }
    while (cb != EOF) { navyse++; cb = getc(b); }
    fclose(a);
    fclose(b);
    if (rozne == 0 && navyse == 0) {
        printf("Subory su identicke\n");
    } else {
        printf("Pocet roznych znakov: %d\n", rozne);
        if (navyse)
            printf("Jeden zo suborov je dlhsi o %d znakov\n", navyse);
    }
    return 0;
}

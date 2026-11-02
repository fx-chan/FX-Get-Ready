#include <stdio.h>

typedef struct {
    char meno[50];
    double plat;
} ZAMESTNANEC;

void zvys_plat(ZAMESTNANEC *z, double percent) {
    /* DOPLŇ */
}

int main(void) {
    ZAMESTNANEC z;
    double p;
    scanf("%49s %lf %lf", z.meno, &z.plat, &p);
    zvys_plat(&z, p);
    printf("%s %.2f\n", z.meno, z.plat);
    return 0;
}

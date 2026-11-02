#include <stdio.h>

int zisti_prvocislo(int cislo) {
    if (cislo < 2)
        return -1;
    for (int d = 2; d * d <= cislo; d++)
        if (cislo % d == 0)
            return -1;
    return 1;
}

int main(void) {
    int a, b, nasiel = 0;
    scanf("%d %d", &a, &b);
    if (a > b) {
        int t = a; a = b; b = t;
    }
    for (int i = a; i <= b; i++) {
        if (zisti_prvocislo(i) == 1) {
            printf("%d\n", i);
            nasiel = 1;
        }
    }
    if (!nasiel)
        printf("Prvocislo neexistuje\n");
    return 0;
}

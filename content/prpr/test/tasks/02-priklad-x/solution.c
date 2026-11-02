#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int nacitaj_k(void) {
    int k, r;
    while ((r = scanf("%d", &k)) != EOF) {
        if (r == 0) {
            scanf("%*s");
            continue;
        }
        if (k > 0)
            return k;
    }
    return 0;
}

void x(double *hodnota, int velkost_pola) {
    int k = nacitaj_k();
    if (k == 0)
        return;
    int pocet[10] = {0};
    for (int i = 0; i < velkost_pola; i += k) {
        long long v = llround(hodnota[i] * 1e6);
        pocet[v / 10000 % 10]++;   /* 2. desatinné miesto */
        pocet[v / 1000 % 10]++;    /* 3. */
        pocet[v / 100 % 10]++;     /* 4. */
    }
    printf("cislice:  ");
    for (int d = 0; d < 10; d++)
        if (pocet[d])
            printf("%3d", d);
    printf("\npocetnost:");
    for (int d = 0; d < 10; d++)
        if (pocet[d])
            printf("%3d", pocet[d]);
    printf("\n");
}

int main(void) {
    int n;
    scanf("%d", &n);
    double *hodnota = malloc(n * sizeof(double));
    for (int i = 0; i < n; i++)
        scanf("%lf", &hodnota[i]);
    x(hodnota, n);
    free(hodnota);
    return 0;
}

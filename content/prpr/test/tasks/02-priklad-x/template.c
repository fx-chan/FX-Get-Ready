#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void x(double *hodnota, int velkost_pola) {
    // TODO: načítaj k (> 0), spočítaj cifry na 2.-4. desatinnom mieste pre i = 0, k, 2k, ...
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

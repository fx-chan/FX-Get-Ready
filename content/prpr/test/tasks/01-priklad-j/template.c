#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/* Pomocné funkcie: stredná hodnota, percentuálny rozdiel, ... */

void j(char **pole_Mer_Mod, char **pole_Typ_MV, double *hodnota, int velkost_pola) {
    // TODO: načítaj modul1 modul2 typ, vypočítaj a vypíš
}

int main(void) {
    int n;
    scanf("%d", &n);
    char **mm = malloc(n * sizeof(char *));
    char **typ = malloc(n * sizeof(char *));
    double *h = malloc(n * sizeof(double));
    for (int i = 0; i < n; i++) {
        mm[i] = malloc(4);
        typ[i] = malloc(3);
        scanf("%3s %2s %lf", mm[i], typ[i], &h[i]);
    }
    j(mm, typ, h, n);
    for (int i = 0; i < n; i++) {
        free(mm[i]);
        free(typ[i]);
    }
    free(mm);
    free(typ);
    free(h);
    return 0;
}

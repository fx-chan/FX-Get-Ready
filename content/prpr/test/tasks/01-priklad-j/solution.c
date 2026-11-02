#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

double stredna_hodnota(double *v, int n) {
    double s = 0;
    for (int i = 0; i < n; i++)
        s += v[i];
    return s / n;
}

double pr(double a, double b) {
    return b * 100 / a - 100;
}

/* Hodnoty modulu `mod` s typom `t` skopíruje do nového dynamického poľa; vráti ich počet. */
int vyber(char **mm, char **typ, double *h, int n, const char *mod, const char *t, double **out) {
    int k = 0;
    *out = malloc(n * sizeof(double));
    for (int i = 0; i < n; i++)
        if (strcmp(mm[i], mod) == 0 && strcmp(typ[i], t) == 0)
            (*out)[k++] = h[i];
    return k;
}

void min_max(double *v, int n, double *mn, double *mx) {
    *mn = *mx = v[0];
    for (int i = 1; i < n; i++) {
        if (v[i] < *mn) *mn = v[i];
        if (v[i] > *mx) *mx = v[i];
    }
}

void j(char **pole_Mer_Mod, char **pole_Typ_MV, double *hodnota, int velkost_pola) {
    char m1[4], m2[4], t[3];
    if (scanf("%3s %3s %2s", m1, m2, t) != 3)
        return;
    double *v1, *v2;
    int n1 = vyber(pole_Mer_Mod, pole_Typ_MV, hodnota, velkost_pola, m1, t, &v1);
    int n2 = vyber(pole_Mer_Mod, pole_Typ_MV, hodnota, velkost_pola, m2, t, &v2);
    if (n1 == 0 || n2 == 0) {
        printf("%s a %s sa nemozu porovnat.\n", m1, m2);
    } else {
        double mn1, mx1, mn2, mx2;
        min_max(v1, n1, &mn1, &mx1);
        min_max(v2, n2, &mn2, &mx2);
        double s1 = stredna_hodnota(v1, n1), s2 = stredna_hodnota(v2, n2);
        double r[6] = {pr(mn1, s1), pr(mx1, s1), pr(mn2, s2), pr(mx2, s2), pr(s1, s2), pr(s2, s1)};
        printf("%s %.4f (%.4f) %.4f %.4f (%.4f)\n", m1, mn1, r[0], s1, mx1, r[1]);
        printf("%s %.4f (%.4f) %.4f %.4f (%.4f)\n", m2, mn2, r[2], s2, mx2, r[3]);
        int ok = 1;
        for (int i = 0; i < 6; i++)
            if (fabs(r[i]) > 5)
                ok = 0;
        if (ok)
            printf("%s a %s su v standardnej odchylke.\n", m1, m2);
        else
            printf("%s a %s prekracuju limit povoleneho rozmedzia.\n", m1, m2);
    }
    free(v1);
    free(v2);
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

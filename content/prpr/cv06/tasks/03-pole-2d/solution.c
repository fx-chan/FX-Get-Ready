#include <stdio.h>
#include <stdlib.h>

int **alokuj_2D_pole(int n, int m) {
    int **p = malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++)
        p[i] = malloc(m * sizeof(int));
    return p;
}

void vypis_2D_pole(int **p, int n, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            printf(j ? " %d" : "%d", p[i][j]);
        printf("\n");
    }
}

void uvolni(int **p, int n) {
    for (int i = 0; i < n; i++)
        free(p[i]);
    free(p);
}

int main(void) {
    int n, m;
    scanf("%d %d", &n, &m);
    int **p = alokuj_2D_pole(n, m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            scanf("%d", &p[i][j]);
    vypis_2D_pole(p, n, m);
    uvolni(p, n);
    return 0;
}

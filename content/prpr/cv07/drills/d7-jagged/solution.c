#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int **t = malloc(n * sizeof(int *));      // pole ukazovateľov na riadky
    for (int i = 0; i < n; i++) {
        t[i] = malloc((i + 1) * sizeof(int));
        t[i][0] = t[i][i] = 1;
        for (int j = 1; j < i; j++)
            t[i][j] = t[i - 1][j - 1] + t[i - 1][j];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++)
            printf(j ? " %d" : "%d", t[i][j]);
        printf("\n");
    }
    for (int i = 0; i < n; i++)
        free(t[i]);
    free(t);
    return 0;
}

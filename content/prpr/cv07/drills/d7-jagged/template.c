#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int **t = malloc(n * sizeof(int *));      // pole ukazovateľov na riadky
    for (int i = 0; i < n; i++) {
        t[i] = NULL;  /* DOPLŇ: alokuj riadok s i + 1 prvkami a naplň ho */
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++)
            printf(j ? " %d" : "%d", t[i][j]);
        printf("\n");
    }
    /* DOPLŇ: uvoľni riadky aj pole ukazovateľov */
    return 0;
}

#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    while (scanf("%d", &n) == 1) {
        char *m = malloc(n * n);
        int k = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) {
                int col = i % 2 == 0 ? j : n - 1 - j;
                m[i * n + col] = 'a' + k++ % 26;
            }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                printf(j ? " %c" : "%c", m[i * n + j]);
            printf("\n");
        }
        printf("\n");
        free(m);
    }
    return 0;
}

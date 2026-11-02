#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int cap = 4, n = 0, x;
    int *a = malloc(cap * sizeof(int));
    while (scanf("%d", &x) == 1) {
        if (n == cap) {
            cap *= 2;
            int *tmp = realloc(a, cap * sizeof(int));
            if (tmp == NULL) {
                free(a);
                return 1;
            }
            a = tmp;
        }
        a[n++] = x;
    }
    if (n == 0) {
        printf("Ziadne cisla\n");
    } else {
        printf("Pocet: %d\n", n);
        for (int i = n - 1; i >= 0; i--)
            printf(i == n - 1 ? "%d" : " %d", a[i]);
        printf("\n");
    }
    free(a);
    return 0;
}

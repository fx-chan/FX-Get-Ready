#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int cap = 2, n = 0, x;
    int *a = malloc(cap * sizeof(int));
    while (scanf("%d", &x) == 1) {
        if (n == cap) {
            cap *= 2;
            a = /* DOPLŇ */;
        }
        a[n++] = x;
    }
    printf("%d prvkov, posledny %d\n", n, a[n - 1]);
    free(a);
    return 0;
}

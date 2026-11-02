#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    char *p = malloc(n);
    for (int i = 0; i < n; i++)
        scanf(" %c", p + i);
    for (char *q = p + n - 1; q >= p; q--)
        putchar(*q);
    putchar('\n');
    free(p);
    return 0;
}

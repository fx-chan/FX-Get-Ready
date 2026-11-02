#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, s = 0;
    scanf("%d", &n);
    int *a = /* DOPLŇ */;
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        s += a[i];
    }
    printf("%d\n", s);
    free(a);
    return 0;
}

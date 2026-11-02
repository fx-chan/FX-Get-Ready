#include <stdio.h>

void delenie(int a, int b, int *podiel, int *zvysok) {
    *podiel = a / b;
    *zvysok = a % b;
}

int main(void) {
    int a, b, p, z;
    scanf("%d %d", &a, &b);
    /* DOPLŇ volanie */
    printf("%d %d\n", p, z);
    return 0;
}

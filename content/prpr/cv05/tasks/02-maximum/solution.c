#include <stdio.h>

int *maximum(int *a, int *b) {
    return *a > *b ? a : b;
}

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    int *m = maximum(&x, &y);
    printf("Cislo %d je vacsie.\n", *m);
    return 0;
}

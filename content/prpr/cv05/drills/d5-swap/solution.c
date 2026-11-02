#include <stdio.h>

void vymen(int *a, int *b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    vymen(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}

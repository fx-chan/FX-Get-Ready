#include <stdio.h>

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    int m = (a > b) ? a : b;
    printf("%d\n", m);
    return 0;
}

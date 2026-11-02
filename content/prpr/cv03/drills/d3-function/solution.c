#include <stdio.h>

int vacsie(int a, int b) {
    return a > b ? a : b;
}

int main(void) {
    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d\n", vacsie(x, y));
    return 0;
}

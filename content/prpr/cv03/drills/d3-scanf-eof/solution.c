#include <stdio.h>

int main(void) {
    int x, s = 0;
    while (scanf("%d", &x) == 1)
        s += x;
    printf("%d\n", s);
    return 0;
}

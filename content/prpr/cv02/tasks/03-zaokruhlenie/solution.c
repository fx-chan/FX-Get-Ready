#include <stdio.h>

int main(void) {
    double x;
    scanf("%lf", &x);
    printf("%d %d\n", (int)x, (int)(x + 0.5));
    return 0;
}

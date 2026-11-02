#include <stdio.h>

int main(void) {
    int a, b;
    char z;
    scanf("%d %d %c", &a, &b, &z);
    if (z == '+')
        printf("%d + %d = %d\n", a, b, a + b);
    else if (z == '-')
        printf("%d - %d = %d\n", a, b, a - b);
    else if (z == '*')
        printf("%d * %d = %d\n", a, b, a * b);
    else if (z == '/')
        printf("%d / %d = %d\n", a, b, a / b);
    return 0;
}

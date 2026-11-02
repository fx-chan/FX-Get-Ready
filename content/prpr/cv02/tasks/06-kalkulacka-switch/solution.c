#include <stdio.h>

int main(void) {
    int a, b;
    char z;
    scanf("%d %d %c", &a, &b, &z);
    switch (z) {
        case '+': printf("%d + %d = %d\n", a, b, a + b); break;
        case '-': printf("%d - %d = %d\n", a, b, a - b); break;
        case '*': printf("%d * %d = %d\n", a, b, a * b); break;
        case '/': printf("%d / %d = %d\n", a, b, a / b); break;
        default: printf("Zle zadana volba.\n");
    }
    return 0;
}

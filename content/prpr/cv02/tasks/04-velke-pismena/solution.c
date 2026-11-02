#include <stdio.h>

int main(void) {
    char a, b;
    scanf(" %c %c", &a, &b);
    a = a - 'a' + 'A';
    b = b - 'a' + 'A';
    printf("%c %d\n%c %d\n", a, a, b, b);
    return 0;
}

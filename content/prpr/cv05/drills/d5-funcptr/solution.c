#include <stdio.h>

int sucet(int a, int b)   { return a + b; }
int rozdiel(int a, int b) { return a - b; }
int sucin(int a, int b)   { return a * b; }

int main(void) {
    int a, b;
    char op;
    scanf("%d %c %d", &a, &op, &b);
    int (*f)(int, int) = sucet;
    if (op == '-') f = rozdiel;
    else if (op == '*') f = sucin;
    printf("%d\n", f(a, b));
    return 0;
}

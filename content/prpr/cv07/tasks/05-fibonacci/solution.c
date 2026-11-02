#include <stdio.h>

long fib(int n) {
    if (n < 2)
        return n;
    return fib(n - 1) + fib(n - 2);
}

int main(void) {
    int n;
    while (scanf("%d", &n) == 1)
        printf("fib(%d) = %ld\n", n, fib(n));
    return 0;
}

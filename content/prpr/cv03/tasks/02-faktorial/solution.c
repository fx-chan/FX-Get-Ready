#include <stdio.h>

int main(void) {
    int n;
    do {
        scanf("%d", &n);
    } while (n < 0);
    long long f = 1;
    for (int i = 2; i <= n; i++)
        f *= i;
    printf("%lld\n", f);
    return 0;
}

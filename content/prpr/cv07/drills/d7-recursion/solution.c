#include <stdio.h>

int sucet_cifier(int n) {
    if (n < 10)
        return n;
    return n % 10 + sucet_cifier(n / 10);
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d\n", sucet_cifier(n));
    return 0;
}

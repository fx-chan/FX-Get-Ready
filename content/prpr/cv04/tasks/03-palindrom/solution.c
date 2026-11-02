#include <stdio.h>

long reverzne_cislo(long x) {
    long r = 0;
    while (x > 0) {
        r = r * 10 + x % 10;
        x /= 10;
    }
    return r;
}

int main(void) {
    long x;
    while (scanf("%ld", &x) == 1) {
        long r = reverzne_cislo(x);
        printf("%ld\n", r);
        printf("Cislo %ld %s palindrom\n", x, r == x ? "je" : "nie je");
    }
    return 0;
}

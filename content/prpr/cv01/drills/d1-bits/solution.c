#include <stdio.h>

int main(void) {
    unsigned n, k;
    scanf("%u %u", &n, &k);
    unsigned bit = (n >> k) & 1u;
    unsigned zap = n | (1u << k);
    unsigned vyp = n & ~(1u << k);
    printf("%u\n%u\n%u\n", bit, zap, vyp);
    return 0;
}

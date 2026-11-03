#include <stdio.h>

int main(void) {
    unsigned n, k;
    scanf("%u %u", &n, &k);
    unsigned bit = 0;       /* DOPLŇ: hodnota k-teho bitu */
    unsigned zap = n;       /* DOPLŇ: n s nastaveným k-tym bitom */
    unsigned vyp = n;       /* DOPLŇ: n s vynulovaným k-tym bitom */
    printf("%u\n%u\n%u\n", bit, zap, vyp);
    return 0;
}

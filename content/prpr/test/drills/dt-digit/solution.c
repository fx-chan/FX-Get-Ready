#include <stdio.h>
#include <math.h>

int main(void) {
    double x;
    int p;
    scanf("%lf %d", &x, &p);
    long long v = llround(x * 1e6);
    long long delitel = 1;
    for (int i = 0; i < 6 - p; i++)
        delitel *= 10;
    printf("%d\n", (int)(v / delitel % 10));
    return 0;
}

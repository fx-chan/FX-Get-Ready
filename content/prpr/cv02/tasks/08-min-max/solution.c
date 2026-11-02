#include <stdio.h>

int main(void) {
    int n;
    double x, mn, mx;
    scanf("%d", &n);
    scanf("%lf", &x);
    mn = mx = x;
    for (int i = 1; i < n; i++) {
        scanf("%lf", &x);
        if (x < mn) mn = x;
        if (x > mx) mx = x;
    }
    printf("Minimum: %.2f\nMaximum: %.2f\n", mn, mx);
    return 0;
}

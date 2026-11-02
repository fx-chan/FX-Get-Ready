#include <stdio.h>

double pr(double a, double b) {
    return b * 100 / a - 100;
}

int main(void) {
    double a, b;
    scanf("%lf %lf", &a, &b);
    printf("%.4f\n", pr(a, b));
    return 0;
}

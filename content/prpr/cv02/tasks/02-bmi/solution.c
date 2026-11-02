#include <stdio.h>

int main(void) {
    double v, m;
    scanf("%lf %lf", &v, &m);
    v /= 100;
    printf("BMI: %.3f\n", m / (v * v));
    return 0;
}

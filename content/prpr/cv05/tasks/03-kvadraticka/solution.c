#include <stdio.h>
#include <math.h>

int kvadraticka_rovnica(double a, double b, double c, double *x1, double *x2) {
    double d = b * b - 4 * a * c;
    if (d < 0)
        return 0;
    if (d == 0) {
        *x1 = *x2 = -b / (2 * a);
        return 1;
    }
    *x1 = (-b + sqrt(d)) / (2 * a);
    *x2 = (-b - sqrt(d)) / (2 * a);
    return 2;
}

int main(void) {
    double a, b, c, x1, x2;
    scanf("%lf %lf %lf", &a, &b, &c);
    int n = kvadraticka_rovnica(a, b, c, &x1, &x2);
    if (n == 2)
        printf("Rovnica ma 2 korene: x1 = %.3f, x2 = %.3f\n", x1, x2);
    else if (n == 1)
        printf("Rovnica ma 1 koren: x = %.3f\n", x1);
    else
        printf("Rovnica nema realne korene\n");
    return 0;
}

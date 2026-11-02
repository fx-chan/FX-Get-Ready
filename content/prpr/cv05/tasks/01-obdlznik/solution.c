#include <stdio.h>

void nacitaj(double *a, double *b) {
    scanf("%lf %lf", a, b);
}

void vypocitaj(double a, double b, double *obsah, double *obvod) {
    *obsah = a * b;
    *obvod = 2 * (a + b);
}

int main(void) {
    double a, b, s, o;
    nacitaj(&a, &b);
    vypocitaj(a, b, &s, &o);
    printf("Obsah: %.3f\nObvod: %.3f\n", s, o);
    return 0;
}

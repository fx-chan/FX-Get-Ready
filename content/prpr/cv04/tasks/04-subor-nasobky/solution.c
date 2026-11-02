#include <stdio.h>

int main(void) {
    double x;
    int c;
    scanf("%lf", &x);
    FILE *f = fopen("nasobky.txt", "w");
    for (int i = 1; i <= 10; i++)
        fprintf(f, "%2d * %.2f = %.2f\n", i, x, i * x);
    fclose(f);
    f = fopen("nasobky.txt", "r");
    while ((c = getc(f)) != EOF)
        putchar(c);
    fclose(f);
    return 0;
}

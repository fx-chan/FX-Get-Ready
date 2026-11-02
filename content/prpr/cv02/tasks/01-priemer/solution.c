#include <stdio.h>

int main(void) {
    double x, y, z;
    scanf("%lf %lf %lf", &x, &y, &z);
    printf("Priemer cisel %g %g %g je: %g\n", x, y, z, (x + y + z) / 3);
    return 0;
}

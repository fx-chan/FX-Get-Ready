#include <stdio.h>

void mocnina(double x, int n) {
    double y = 1;
    for (int i = 1; i <= n; i++) {
        y *= x;
        printf("%.2f^%d = %.2f\n", x, i, y);
    }
}

int main(void) {
    double x;
    int n;
    scanf("%lf %d", &x, &n);
    mocnina(x, n);
    return 0;
}

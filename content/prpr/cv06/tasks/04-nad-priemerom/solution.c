#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);
    double *a = malloc(n * sizeof(double)), s = 0;
    for (double *p = a; p < a + n; p++) {
        scanf("%lf", p);
        s += *p;
    }
    double avg = s / n;
    printf("Priemer: %.2f\nNad priemerom:", avg);
    for (double *p = a; p < a + n; p++)
        if (*p > avg)
            printf(" %g", *p);
    printf("\n");
    free(a);
    return 0;
}

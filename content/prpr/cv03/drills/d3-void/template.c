#include <stdio.h>

/* DOPLŇ prototyp */

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%.1f\n", priemer(a, b));
    return 0;
}

double priemer(int a, int b) {
    return (a + b) / 2.0;
}

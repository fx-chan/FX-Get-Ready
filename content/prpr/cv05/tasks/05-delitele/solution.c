#include <stdio.h>

int delitele(int x[], int pocetx, int y[], int k) {
    int n = 0;
    for (int i = 0; i < pocetx; i++)
        if (x[i] != 0 && k % x[i] == 0)
            y[n++] = x[i];
    return n;
}

int main(void) {
    int x[100], y[100], n, k;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        scanf("%d", &x[i]);
    scanf("%d", &k);
    int m = delitele(x, n, y, k);
    printf("pocety: %d\ny: {", m);
    for (int i = 0; i < m; i++)
        printf(i ? ", %d" : "%d", y[i]);
    printf("}\n");
    return 0;
}

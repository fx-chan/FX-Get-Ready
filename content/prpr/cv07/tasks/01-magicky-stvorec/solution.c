#include <stdio.h>
#define N 20

int magicky(int m[][N], int n) {
    int ciel = 0, d1 = 0, d2 = 0;
    for (int j = 0; j < n; j++)
        ciel += m[0][j];
    for (int i = 0; i < n; i++) {
        int r = 0, s = 0;
        for (int j = 0; j < n; j++) {
            r += m[i][j];
            s += m[j][i];
        }
        if (r != ciel || s != ciel)
            return 0;
        d1 += m[i][i];
        d2 += m[i][n - 1 - i];
    }
    return d1 == ciel && d2 == ciel;
}

int main(void) {
    int m[N][N], n;
    scanf("%d", &n);
    if (n > N) {
        printf("Prilis velky rozmer\n");
        return 0;
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &m[i][j]);
    printf(magicky(m, n) ? "Stvorec je magicky\n" : "Stvorec nie je magicky\n");
    return 0;
}

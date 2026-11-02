#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    if (n < 1 || n > 15) {
        printf("Cislo nie je z daneho intervalu\n");
        return 0;
    }
    for (int r = 1; r <= n; r++) {
        printf("%d:", r);
        for (int k = n - r + 1; k >= 1; k--)
            printf(" %2d", k);
        printf("\n");
    }
    return 0;
}

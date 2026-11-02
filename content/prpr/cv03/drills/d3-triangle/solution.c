#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for (int r = 1; r <= n; r++) {
        for (int s = 1; s <= r; s++)
            printf("*");
        printf("\n");
    }
    return 0;
}

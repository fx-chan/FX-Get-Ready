#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    if (n < 1 || n > 15 || n % 2 == 0) {
        printf("Zly vstup\n");
        return 0;
    }
    int s = n / 2;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++)
            putchar(r == c || r + c == n - 1 || r == s || c == s ? '*' : ' ');
        putchar('\n');
    }
    return 0;
}

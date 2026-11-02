#include <stdio.h>

int je_prvocislo(int n) {
    if (n < 2)
        return 0;
    for (int d = 2; d * d <= n; d++)
        if (n % d == 0)
            return 0;
    return 1;
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d\n", je_prvocislo(n));
    return 0;
}

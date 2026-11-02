#include <stdio.h>
#define N 11

int main(void) {
    int a[N], ok = 1;
    for (int i = 0; i < N; i++)
        scanf("%d", &a[i]);
    if (a[0] < 0 || a[0] > 10)
        ok = 0;
    for (int i = 1; i < N && ok; i++)
        if (a[i] > 2 * a[i - 1] || 2 * a[i] < a[i - 1])
            ok = 0;
    printf(ok ? "Postupnost je spravna\n" : "Postupnost nie je spravna\n");
    return 0;
}

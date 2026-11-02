#include <stdio.h>

int main(void) {
    int m[10][10], n, s = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &m[i][j]);
    for (int i = 0; i < n; i++)
        s += m[i][i];
    printf("%d\n", s);
    return 0;
}

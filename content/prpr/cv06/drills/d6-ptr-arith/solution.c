#include <stdio.h>

int main(void) {
    int a[6];
    for (int i = 0; i < 6; i++)
        scanf("%d", a + i);
    int *p = a;
    for (int i = 0; i < 6; i++)
        printf(i ? " %d" : "%d", *(p + i));
    printf("\n");
    return 0;
}

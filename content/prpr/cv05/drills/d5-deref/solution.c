#include <stdio.h>

int main(void) {
    int x;
    scanf("%d", &x);
    int *p = &x;
    *p = *p * 3;
    printf("%d\n", x);
    return 0;
}

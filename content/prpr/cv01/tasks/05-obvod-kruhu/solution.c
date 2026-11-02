#include <stdio.h>

int main(void) {
    int r;
    scanf("%d", &r);
    printf("Obvod kruhu s polomerom %d je: %.2f\n", r, 2 * 3.14 * r);
    return 0;
}

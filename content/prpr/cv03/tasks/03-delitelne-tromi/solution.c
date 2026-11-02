#include <stdio.h>

int main(void) {
    int f, g, prve = 1;
    scanf("%d %d", &f, &g);
    for (int i = f; i <= g; i++) {
        if (i % 3 == 0) {
            printf(prve ? "%d" : " %d", i);
            prve = 0;
        }
    }
    printf("\n");
    return 0;
}

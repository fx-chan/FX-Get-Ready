#include <stdio.h>

int main(void) {
    int n, x, pocet = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x);
        if (x > 0 && x <= 100)
            pocet++;
    }
    printf("%d\n", pocet);
    return 0;
}

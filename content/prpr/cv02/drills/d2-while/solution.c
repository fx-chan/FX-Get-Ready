#include <stdio.h>

int main(void) {
    int n, pocet = 0;
    scanf("%d", &n);
    while (n > 0) {
        pocet++;
        n /= 10;
    }
    printf("%d\n", pocet);
    return 0;
}

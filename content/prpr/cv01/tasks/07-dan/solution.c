#include <stdio.h>

int main(void) {
    int c;
    scanf("%d", &c);
    printf("Cena bez dane: %d\n", c);
    printf("Predajna cena s danou 20%%: %.1f\n", c * 1.2);
    return 0;
}

#include <stdio.h>

int main(void) {
    FILE *f = fopen("cisla.txt", "r");
    int x, s = 0;
    while (/* DOPLŇ */)
        s += x;
    fclose(f);
    printf("%d\n", s);
    return 0;
}

#include <stdio.h>

int main(void) {
    FILE *f = fopen("cisla.txt", "r");
    int x, s = 0;
    while (fscanf(f, "%d", &x) == 1)
        s += x;
    fclose(f);
    printf("%d\n", s);
    return 0;
}

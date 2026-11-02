#include <stdio.h>

int main(void) {
    FILE *f = fopen("text.txt", "r");
    int c, riadky = 0;
    while (/* DOPLŇ */)
        if (c == '\n')
            riadky++;
    fclose(f);
    printf("%d\n", riadky);
    return 0;
}

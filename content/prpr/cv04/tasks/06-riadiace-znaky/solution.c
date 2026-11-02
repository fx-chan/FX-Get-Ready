#include <stdio.h>

int main(void) {
    FILE *f = fopen("text.txt", "r");
    int c, medzery = 0;
    while ((c = getc(f)) != EOF) {
        if (c == 'x' || c == 'X')
            printf("Precital som X\n");
        else if (c == 'y' || c == 'Y')
            printf("Precital som Y\n");
        else if (c == '#' || c == '$' || c == '&')
            printf("Precital som riadiaci znak\n");
        else if (c == ' ')
            medzery++;
        else if (c == '*') {
            printf("Koniec\n");
            break;
        }
    }
    fclose(f);
    printf("Pocet precitanych medzier: %d\n", medzery);
    return 0;
}

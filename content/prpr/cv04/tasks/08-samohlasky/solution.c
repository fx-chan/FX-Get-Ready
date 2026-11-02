#include <stdio.h>
#include <string.h>

int main(void) {
    char samohlasky[] = "aeiouyAEIOUY";
    char spoluhlasky[] = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ";
    FILE *f = fopen("vstup.txt", "r");
    int c, s = 0, h = 0, d = 0;
    while ((c = getc(f)) != EOF) {
        if (c == '\0')
            continue;
        if (strchr(samohlasky, c))
            s++;
        else if (strchr(spoluhlasky, c))
            h++;
        else if (c >= '0' && c <= '9')
            d++;
    }
    fclose(f);
    printf("Pocet samohlasok: %d, pocet spoluhlasok: %d, pocet cislic: %d.\n", s, h, d);
    return 0;
}

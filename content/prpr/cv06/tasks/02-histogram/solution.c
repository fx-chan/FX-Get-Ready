#include <stdio.h>
#include <ctype.h>

int main(void) {
    char meno[256];
    int pocty[26] = {0}, c, riadok = 1, nieco = 0;
    scanf("%255s", meno);
    FILE *f = fopen(meno, "r");
    if (f == NULL) {
        printf("Subor sa nepodarilo otvorit\n");
        return 1;
    }
    printf("  #");
    for (int i = 0; i < 26; i++)
        printf("%3c", 'A' + i);
    printf("\n");
    while ((c = getc(f)) != EOF) {
        nieco = 1;
        if (c == '\n') {
            printf("%3d", riadok++);
            for (int i = 0; i < 26; i++) {
                printf("%3d", pocty[i]);
                pocty[i] = 0;
            }
            printf("\n");
            nieco = 0;
        } else if (isalpha(c)) {
            pocty[toupper(c) - 'A']++;
        }
    }
    if (nieco) {
        printf("%3d", riadok);
        for (int i = 0; i < 26; i++)
            printf("%3d", pocty[i]);
        printf("\n");
    }
    fclose(f);
    return 0;
}

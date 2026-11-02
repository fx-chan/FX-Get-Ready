#include <stdio.h>

int main(void) {
    char riadok[100];
    FILE *f = fopen("meno.txt", "r");
    if (f == NULL) {
        printf("Chyba\n");
        return 1;
    }
    fgets(riadok, sizeof riadok, f);
    printf("%s", riadok);
    fclose(f);
    return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int n;
    char buf[101];
    scanf("%d", &n);
    char **pole = /* DOPLŇ */;
    for (int i = 0; i < n; i++) {
        scanf("%100s", buf);
        pole[i] = /* DOPLŇ */;
        strcpy(pole[i], buf);
    }
    for (int i = 0; i < n; i++)
        printf(i ? "-%s" : "%s", pole[i]);
    printf("\n");
    for (int i = 0; i < n; i++)
        free(pole[i]);
    free(pole);
    return 0;
}

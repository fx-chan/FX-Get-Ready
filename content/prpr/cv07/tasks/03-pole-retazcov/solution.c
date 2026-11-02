#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int n;
    char buf[101];
    scanf("%d", &n);
    char **slova = malloc(n * sizeof(char *));
    for (int i = 0; i < n; i++) {
        scanf("%100s", buf);
        slova[i] = malloc(strlen(buf) + 1);
        strcpy(slova[i], buf);
    }
    for (int i = n - 1; i >= 0; i--)
        printf("%d: %s (%d)\n", i + 1, slova[i], (int)strlen(slova[i]));
    for (int i = 0; i < n; i++)
        free(slova[i]);
    free(slova);
    return 0;
}

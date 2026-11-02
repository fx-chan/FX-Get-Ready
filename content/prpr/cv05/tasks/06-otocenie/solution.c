#include <stdio.h>
#include <string.h>

void otoc(char *s) {
    int i = 0, j = strlen(s) - 1;
    while (i < j) {
        char t = s[i];
        s[i++] = s[j];
        s[j--] = t;
    }
}

int main(void) {
    char s[101];
    scanf("%100s", s);
    otoc(s);
    printf("%s\n", s);
    return 0;
}

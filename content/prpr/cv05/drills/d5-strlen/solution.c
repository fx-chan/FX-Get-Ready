#include <stdio.h>

int dlzka(const char *s) {
    int n = 0;
    while (s[n] != '\0')
        n++;
    return n;
}

int main(void) {
    char s[101];
    scanf("%100s", s);
    printf("%d\n", dlzka(s));
    return 0;
}

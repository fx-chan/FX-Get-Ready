#include <stdio.h>

int main(void) {
    char c;
    scanf(" %c", &c);
    if (c >= '0' && c <= '9')
        printf("cislica\n");
    else
        printf("iny znak\n");
    return 0;
}

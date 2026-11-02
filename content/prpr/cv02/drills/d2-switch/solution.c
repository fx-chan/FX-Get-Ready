#include <stdio.h>

int main(void) {
    int d;
    scanf("%d", &d);
    switch (d) {
        case 1: printf("Pondelok\n"); break;
        case 2: printf("Utorok\n"); break;
        case 3: printf("Streda\n"); break;
        default: printf("Iny den\n");
    }
    return 0;
}

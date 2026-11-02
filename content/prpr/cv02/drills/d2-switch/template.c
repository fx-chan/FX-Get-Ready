#include <stdio.h>

int main(void) {
    int d;
    scanf("%d", &d);
    switch (d) {
        case 1: printf("Pondelok\n"); break;
        /* DOPLŇ case 2 a case 3 */
        default: printf("Iny den\n");
    }
    return 0;
}

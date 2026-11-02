#include <stdio.h>
#include <string.h>

int main(void) {
    char w[101], best[101] = "";
    int n = 0;
    while (scanf("%100s", w) == 1) {
        n++;
        if (strlen(w) > strlen(best))
            strcpy(best, w);
    }
    printf("Pocet slov: %d\n", n);
    printf("Najdlhsie slovo: %s (%d)\n", best, (int)strlen(best));
    return 0;
}

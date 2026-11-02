#include <stdio.h>

typedef struct {
    char meno[51];
    int body;
} STUDENT;

STUDENT *najlepsi(STUDENT *s, int n) {
    STUDENT *best = s;
    for (int i = 1; i < n; i++)
        if (s[i].body > best->body)
            best = &s[i];
    return best;
}

int main(void) {
    STUDENT s[100];
    int n, sucet = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%50s %d", s[i].meno, &s[i].body);
        sucet += s[i].body;
    }
    STUDENT *b = najlepsi(s, n);
    printf("Najlepsi: %s (%d b.)\n", b->meno, b->body);
    printf("Priemer: %.2f\n", (double)sucet / n);
    return 0;
}

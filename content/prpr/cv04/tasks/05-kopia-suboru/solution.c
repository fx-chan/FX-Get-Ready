#include <stdio.h>

int main(void) {
    char volba;
    int c;
    scanf(" %c", &volba);
    FILE *in = fopen("znak.txt", "r");
    if (volba == 's') {
        FILE *out = fopen("novy.txt", "w");
        while ((c = getc(in)) != EOF)
            putc(c, out);
        fclose(out);
        printf("Skopirovane do novy.txt:\n");
        out = fopen("novy.txt", "r");
        while ((c = getc(out)) != EOF)
            putchar(c);
        fclose(out);
    } else {
        while ((c = getc(in)) != EOF)
            putchar(c);
    }
    fclose(in);
    return 0;
}

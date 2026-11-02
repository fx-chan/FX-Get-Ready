#include <stdio.h>

double tyzdenna_mzda(double h_mzda, double hod) {
    double s = h_mzda * (hod < 40 ? hod : 40);
    if (hod > 40)
        s += 1.5 * h_mzda * ((hod < 60 ? hod : 60) - 40);
    if (hod > 60)
        s += 2 * h_mzda * (hod - 60);
    return s;
}

int main(void) {
    int n;
    double m, h, celkom = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lf %lf", &m, &h);
        double s = tyzdenna_mzda(m, h);
        celkom += s;
        printf("Hod. mzda: %.2f Euro/hod, hodin: %.2f, spolu: %.2f Euro\n", m, h, s);
    }
    printf("Celkova mzda: %.2f Euro\n", celkom);
    return 0;
}

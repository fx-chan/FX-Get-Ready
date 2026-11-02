#include <stdio.h>

void vymen_ukazovatele(int **pa, int **pb) {
    int *t = *pa;
    *pa = *pb;
    *pb = t;
}

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    int *pa = &a, *pb = &b;
    printf("Pred: *pa = %d, *pb = %d\n", *pa, *pb);
    vymen_ukazovatele(&pa, &pb);
    printf("Po: *pa = %d, *pb = %d\n", *pa, *pb);
    printf("a = %d, b = %d\n", a, b);
    return 0;
}

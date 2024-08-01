#include <stdio.h>
int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
int main() {
    int a = 12, b = 15;
    int lcm = (a * b) / gcd(a, b);
    printf("LCM: %d\n", lcm);
    return 0;
}

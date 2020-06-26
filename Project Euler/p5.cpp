#include <bits/stdc++.h>

using namespace std;

long gcd(long x, long y) {
    long r = max(x, y) % min(x, y);
    if (r == 0) {  
        return min(x, y);
    } else {
        return gcd(min(x, y), r);
    }
}

int main() {
    long multiple = 1;
    for (long i = 1; i < 21; i++) {
        long divisor = gcd(multiple, i);
        if (divisor == 1) {
            multiple *= i;
        } else {
            multiple *= (i / divisor);
        }
    }
    cout << multiple << endl;
    return 0;
}

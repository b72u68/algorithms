// Special Pythagorian triplet
#include <bits/stdc++.h>

using namespace std;

int main() {
    int s = 1000;
    for (int a = 1; a < s/3; a++) {
        for (int b = a; b < s/2; b++) {
            int c = s - a - b;
            if (pow(a,2) + pow(b,2) == pow(c, 2)) {
                cout << a*b*c << endl;
            }
        }
    }
    return 0;
}

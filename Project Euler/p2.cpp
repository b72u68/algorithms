// Even Fibonacci numbers
#include <bits/stdc++.h>

using namespace std;

int main() {
    int sum = 0;
    int i1 = 1, i2 = 2;

    while (i2 <= 4000000) {
        if (i2 % 2 == 0) {
            sum += i2;
        }
        int temp = i1;
        i1 = i2;
        i2 = temp + i2;
    }

    return sum;
}

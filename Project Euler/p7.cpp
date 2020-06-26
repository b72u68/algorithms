// 10001st prime
#include <bits/stdc++.h>

using namespace std;

bool checkPrime(long n) {
    if (n <= 1) {
        return false;
    } else {
        for (int i = 2; i < int(sqrt(n)); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

int main() {
    long counter = 0;
    long prime = 2;
    while (counter < 10001) {
        if (checkPrime(prime)) {
            counter ++;
        }
        prime ++;
    }
    cout << prime-1 << endl;
    return 0;
}

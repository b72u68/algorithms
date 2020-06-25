// Largest prime factor
#include <bits/stdc++.h>

using namespace std;

vector<int> prime_factors(long n) {
    vector<int> factors;
    int d = 2;
    while (n > 1) {
        while (n % d == 0) {
            factors.push_back(d);
            n = n / d;
        } 
        d = d + 1;
        if ((d * d) > n) {
            if (n > 1) {
                factors.push_back(n);
            }
            break;
        }
    }
    return factors;
}

int main() {
    vector<int> factors = prime_factors(600851475143);
    cout << *max_element(factors.begin(), factors.end()) << "\n";
    return 0;
}

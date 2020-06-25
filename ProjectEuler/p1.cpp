// Multiples of 3 and 5
#include <bits/stdc++.h>

using namespace std;

int main() {
    int sum;
    for (int i = 0; i < 1000; i++) {
        if ((i % 3 == 0) || (i % 5 == 0)) {
            sum += i;
        }
    }
    cout << sum << "\n";
    return 0;
}

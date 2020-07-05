// Highly divisible triangular number
#include <bits/stdc++.h>

using namespace std;

vector<int> divisors(int n) {
    vector<int> div;
    for (int i = 1; i <= sqrt(n); i++) {
        if (n%i == 0) {
            if (n/i == i) {
                div.push_back(i);
            } else {
                div.push_back(i);
                div.push_back(n/i);
            }
        }
    }
    return div;
}

int main() {
    int triangle_num = 0;
    int counter = 1;
    while (true) {
        triangle_num += counter;
        if (divisors(triangle_num).size() >= 500) {
            cout << triangle_num << endl;
            return 0;
        }
        counter ++;
    }
}

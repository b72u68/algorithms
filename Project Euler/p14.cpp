// Longest Collatz sequence
#include <bits/stdc++.h>

using namespace std;

vector<long> generate_sequence(long n) {
    vector<long> seq = {n};
    while (n > 1) {
        if (n%2 == 0) {
            n = n/2;
        } else {
            n = n*3 + 1;
        }
        seq.push_back(n);
    }
    return seq;
}

int main() {
    long max_seq_len = 0;
    long num = 0;
    for (int i = 0; i < 1000001; i++) {
        long seq_len = generate_sequence(i).size();
        if (seq_len > max_seq_len) {
            num = i;
            max_seq_len = seq_len;
        }
    }
    cout << num << endl;
    return 0;
}

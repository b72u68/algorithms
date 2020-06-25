#include <bits/stdc++.h>

using namespace std;

void search(int n) {
    vector<int> permutation;
    for (int i = 0; i < n; i++) {
        permutation.push_back(i);
    }
    do {
        // process permutation
        for (int i = 0; i < permutation.size(); i++) {
            cout << permutation[i] << " ";
        }
        cout << "\n";
    } while (next_permutation(permutation.begin(), permutation.end()));
}

#include <bits/stdc++.h>

using namespace std;

void search(vector<int> permutation, vector<bool> chosen, int n) {
    if (permutation.size() == n) {
        // process permutation
        for (int i = 0; i < permutation.size(); i++) {
            cout << permutation[i] << " ";
        }
        cout << "\n";

    } else {
        for (int i = 0; i < n; i++) {
            if (chosen[i]) continue;
            chosen[i] = true;
            permutation.push_back(i);
            search(permutation, chosen, n);
            chosen[i] = false;
            permutation.pop_back();
        }
    }
}

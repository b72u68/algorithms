#include <bits/stdc++.h>

using namespace std;

void search(int k, int n, vector<int> subset) {
    if (k == n) {
        for (int i = 0; i < subset.size(); i++) {
            cout << subset[i] << " ";
        }
        cout << "\n";
    } else {
        search(k+1, n, subset);
        subset.push_back(k);
        search(k+1, n, subset);
        subset.pop_back();
    }
}

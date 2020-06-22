#include <bits/stdc++.h>

using namespace std;

void generate_subset(int n) {
    for (int b = 0; b < (1<<n); b++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if (b&(1<<i)) subset.push_back(i);
        }

        for (int i = 0; i < subset.size(); i++) {
            cout << subset[i] << " ";
        }
        cout << "\n";
    }
}

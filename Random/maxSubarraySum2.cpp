#include <bits/stdc++.h>

using namespace std;

int maxSubarraySum(vector<int> nums) {
    int best = 0;
    for (int i = 0; i < nums.size(); i++) {
        int sum = 0;
        for (int j = i; j < nums.size(); j++) {
            sum += nums.at(j);
            best = max(best, sum);
        }
    }
    return best;
}

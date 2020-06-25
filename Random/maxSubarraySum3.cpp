#include <bits/stdc++.h>

using namespace std;

int maxSubarraySum(vector<int> nums) {
    int sum = 0;
    int best = 0;
    for (int i = 0; i < nums.size(); i++) {
        sum = max(nums.at(i), sum + nums.at(i));
        best = max(best, sum);
    }
    return best;
}

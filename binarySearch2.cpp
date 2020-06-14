#include <bits/stdc++.h>

using namespace std;

int binarySearch(vector<int> nums, int target) {
    int k = 0;
    for (int b = nums.size()/2; b >= 1; b /= 2) {
        while (k+b < nums.size() && nums.at(k+b) <= target) k += b;
    }
    if (nums.at(k) == target) {
        return k;
    }
    return -1;
}

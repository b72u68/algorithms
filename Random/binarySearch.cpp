#include <bits/stdc++.h>

using namespace std;

int binarySearch(vector<int> nums, int target) {
    int left = 0, right = nums.size()-1;

    while (left <= right) {
        int mid = (right - left)/2 + left;
        if (nums.at(mid) == target) {
            return mid;
        } else if (nums.at(mid) < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    return -1;
}

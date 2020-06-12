#include <bits/stdc++.h>

using namespace std;

vector<int> merge(vector<int> nums1, vector<int> nums2) {
    int i = 0;
    int j = 0;
    vector<int> merged;

    while ((i < nums1.size()) and (j < nums2.size())) {
        if (nums1.at(i) < nums2.at(j)) {
            merged.push_back(nums1.at(i));
            i += 1;
        } else {
            merged.push_back(nums2.at(j));
            j += 1;
        }
    }

    while (i < nums1.size()) {
        merged.push_back(nums1.at(i));
        i += 1;
    }

    while (j < nums2.size()) {
        merged.push_back(nums2.at(j));
        j += 1;
    }

    return merged;

}

vector<int> mergeSort(vector<int> nums) {
    if (nums.size() <= 1) {
        return nums;
    } else {
        int mid = nums.size() / 2;
        vector<int> nums1, nums2;

        for (int i = 0; i < mid; i++) {
            nums1.push_back(nums.at(i));
        }

        for (int i = mid; i < nums.size(); i++) {
            nums2.push_back(nums.at(i));
        }

        return merge(mergeSort(nums1), mergeSort(nums2));
    }
}

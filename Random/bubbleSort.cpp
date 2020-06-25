#include <bits/stdc++.h>

using namespace std;

vector<int> bubbleSort(vector<int> nums) {
    for (int i = 0; i < nums.size(); i++) {
        for (int j = 0; j < nums.size()-1; j++) {
            if (nums.at(j) > nums.at(j+1)) {
                /*
                 *int temp = nums.at(j);
                 *nums.at(j) = nums.at(j+1);
                 *nums.at(j+1) = temp;
                 */
                swap(nums.at(j), nums.at(j+1));
            }
        }
    }
    return nums;
}

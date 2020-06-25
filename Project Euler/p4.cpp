// Largest palindrome product
#include <bits/stdc++.h>

using namespace std;

bool checkPalindrome(string n) {
    if (n.size() < 2) {
        return true;
    } else {
        char lastDigit = n[n.size()-1];
        char firstDigit = n[0];
        if (firstDigit == lastDigit) {
            return checkPalindrome(n.substr(1, n.size()-2));
        } else {
            return false;
        }
    }
}

int main() {
    vector<int> palindromeInt;
    for (int i = 100; i < 1000; i++) {
        for (int j = 100; j < 1000; j++) {
            if (checkPalindrome(to_string(i*j))) {
                palindromeInt.push_back(i*j);
            }
        }
    }
    cout << *max_element(palindromeInt.begin(), palindromeInt.end()) << endl;
    return 0;
}

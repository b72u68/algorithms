// Sum square difference
#include <bits/stdc++.h>

using namespace std;

int main() {
    long sumSquare = 0; 
    long squareSum = 0;
    for (int i = 0; i < 101; i++) {
        sumSquare += pow(i, 2);
        squareSum += i;
    }
    long result = pow(squareSum, 2) - sumSquare; 
    cout << result << endl;
    return 0;
}

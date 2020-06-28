#include <bits/stdc++.h>

using namespace std;

// using Sieve of Eratosthenes
vector<long> getPrimes(long limit) {
    vector<long> numList;
    for (long i = 2; i < limit+1; i++) {
        numList.push_back(i);
    }
    long primeIdx = 0;
    while (primeIdx < numList.size()) { 
        if (numList[primeIdx] != 0) {
            long multipleIdx = primeIdx + numList[primeIdx];
            while (multipleIdx < numList.size()) {
                numList[multipleIdx] = 0;
                multipleIdx += numList[primeIdx];
            }
        }
        primeIdx ++;
    }
    return numList;
}

int main() {
    vector<long> primeList = getPrimes(2*(pow(10, 6))+1);
    long sum = 0;
    for (long i = 0; i < primeList.size(); i++) {
        if (primeList[i] != 0) {
            sum += primeList[i];
        }
    }
    cout << sum << endl;
    return 0;
}

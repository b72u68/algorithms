// Lattice paths
#include <bits/stdc++.h>

using namespace std;

long countPath(long gridSize) {
    long paths = 1;
    for (long i = 0; i < gridSize; i++) {
        paths *= (2 * gridSize) - i;
        paths /= i + 1;
    }
    return paths;
}

int main() {
    cout << countPath(20) << endl;
    return 0;
}

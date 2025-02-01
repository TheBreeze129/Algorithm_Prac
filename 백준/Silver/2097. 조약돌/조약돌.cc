#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int N;
    cin >> N;
    int K = N;
    while (true) {
        double T = sqrt(K);
        if (T == (int)T) break;
        K--;
    }
    int C = (int)sqrt(K);
    int R = N / C;
    if (N % C != 0)  R++;
    if (C == 1) C++;
    if (R == 1) C++;
    cout << 2 * (R + C - 2);
    return 0;
}
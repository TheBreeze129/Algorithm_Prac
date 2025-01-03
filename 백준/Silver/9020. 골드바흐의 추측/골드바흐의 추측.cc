#include <iostream>
#include <cmath>
using namespace std;

bool isprime(int n) {
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main()
{
    int N, T, K, M;
    cin >> N;
    for (int j = 0; j < N; j++) {
        cin >> T;
        K = T / 2;
        M = 0;
        while (true) {
            if (isprime(K - M) && isprime(K + M)) {
                cout << K - M << " " << K + M << endl;
                break;
            }
            M++;
        }
    }
    return 0;
}
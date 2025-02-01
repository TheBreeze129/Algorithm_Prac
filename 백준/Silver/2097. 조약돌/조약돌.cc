#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int N;
    cin >> N;
    
    int K = N;

    while (true) {
        double temp = sqrt(K);
        if (temp == (int)temp) {
            break;
        }
        K -= 1;
    }

    int col = (int)sqrt(K);
    int row = N / col;
    if (N % col != 0) {
        row += 1;
    }

    if (col == 1) {
        col += 1;
    }

    if (row == 1) {
        col += 1;
    }

    cout << 2 * (row + col - 2) << endl;

    return 0;
}

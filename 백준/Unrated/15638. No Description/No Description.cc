#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int N;
    cin >> N;
    int sqrtN = sqrt(N);
    bool flag = true;
    for(int i=2;i<=sqrtN;i++) {
        if (N%i==0) {
            flag = false;
            break;
        }
    }
    if (flag) cout << "Yes";
    else cout << "No";
    return 0;
}
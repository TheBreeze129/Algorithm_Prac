#include <iostream>

int new_power(int a, int b) {
    long long s = 1;
    for(int i=0;i<b;i++) {
        s *= a;
        if (s > 1000000009) s %= 1000000009;
    }
    return s;
}

int main()
{
    int N;
    std::cin >> N;
    if (N==1) std::cout << 0;
    else std::cout << (2*new_power(3, N-2)%1000000009);

    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int N, i, lead, mate;
    cin >> N;
    int* nums = new int[N];
    for(i=0;i<N;i++) cin >> nums[i];
    cin >> lead >> mate;
    int answer = N;
    for(i=0;i<N;i++) {
        if (nums[i] <= lead) continue;
        nums[i] -= lead;
        answer += (nums[i]/mate);
        if (nums[i]%mate == 0) answer++; 
    }
    cout << answer;
    return 0;
}
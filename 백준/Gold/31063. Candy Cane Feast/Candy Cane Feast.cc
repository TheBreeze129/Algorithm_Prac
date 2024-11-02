#include <iostream>
#define LEN 220000
using namespace std;
long long cows[LEN], canes[LEN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, i, j;

    cin >> N >> M;
    for (i = 0; i < N; i++) cin >> cows[i];
    for (i = 0; i < M; i++) cin >> canes[i];

    long long diff, increase;
    for (i = 0; i < M; i++) {
        // 현재까지 먹은 먹이의 높이 : diff
        diff = 0;
        for (j = 0; j < N; j++) {
            // 해당 먹이를 다 먹은 경우
            if (canes[i] <= diff) {
                break;
            }
            if (cows[j] < diff) {
                continue;
            }

            // 이번 연산에서 먹는 크기 : increase
            increase = 0;
            if (cows[j] > canes[i]) {
                increase = canes[i] - diff;
            }
            else {
                increase = cows[j] - diff;
            }
            diff += increase;
            cows[j] += increase;
        }
    }

    for (i = 0; i < N; i++) {
        cout << cows[i] << "\n";
    }
    return 0;
}
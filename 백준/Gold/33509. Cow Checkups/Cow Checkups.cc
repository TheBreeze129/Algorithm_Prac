#include <iostream>
#include <vector>

using namespace std;

static const int MAXN = 7500;

static int A[MAXN + 1];
static int B[MAXN + 1];
static long long cntMatches[(size_t)MAXN + 1];
static short diagPS[(size_t)(2 * MAXN + 2) * (MAXN + 1)];

inline int idx(int s, int y, int N) {
    return s * (N + 1) + y;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        cin >> A[i];
    }
    for (int i = 1; i <= N; i++) {
        cin >> B[i];
    }

    int M = 0;
    for (int i = 1; i <= N; i++) {
        if (A[i] == B[i]) M++;
    }

    vector<int> P(N + 1, 0);
    for (int i = 1; i <= N; i++) {
        P[i] = P[i - 1] + ((A[i] == B[i]) ? 1 : 0);
    }

    for (int s = 2; s <= 2 * N; s++) {
        diagPS[idx(s, 0, N)] = 0;

        for (int y = 1; y <= N; y++) {
            short& refPS = diagPS[idx(s, y, N)];
            refPS = diagPS[idx(s, y - 1, N)];

            int x = s - y;
            if (x >= 1 && x <= N) {
                if (A[x] == B[y]) {
                    refPS += 1;
                }
            }
        }
    }

    long long totalPairs = 0LL;
    for (int l = 1; l <= N; l++) {
        for (int r = l; r <= N; r++) {
            int s = l + r;
            int sLR = P[r] - P[l - 1];
            short tLR = diagPS[idx(s, r, N)]
                - diagPS[idx(s, l - 1, N)];

            int newMatch = M - sLR + tLR;

            cntMatches[newMatch]++;
            totalPairs++;
        }
    }

    for (int c = 0; c <= N; c++) {
        cout << cntMatches[c] << "\n";
    }

    return 0;
}
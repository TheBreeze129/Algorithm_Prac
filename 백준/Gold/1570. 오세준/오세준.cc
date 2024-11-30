#include <iostream>
#include <string>
#include <climits>

using namespace std;

int main() {
    int n, sx, sy, ex, ey;
    cin >> n >> sx >> sy >> ex >> ey;

    ex -= sx;
    ey -= sy;

    if (ex < 0 || ey < 0) {
        cout << "-1";
        return 0;
    }

    if (ex == 0) {
        cout << string(min(ey, n), 'U') + string(n - min(ey, n), 'R');
        return 0;
    }

    string best = ""; // 사전순으로 가장 좋은 경로를 저장
    bool found = false;

    for (int x = n, y = 0; x; x--, y++) {
        int h = ex / x * y;
        if (ey - y <= h && h <= ey + y) {
            int x1 = ex % x, x2 = x - x1;
            int y1 = ey - h, y2 = y - y1;

            if (x1 && y1 < 0) continue;
            if (!x1 && y1 < 0) {
                y2 += y1;
                y1 = 0;
            }

            string candidate = string(x1, 'R') + string(y1, 'U') + string(x2, 'R') + string(y2, 'U');

            // 첫 경로를 저장하거나 사전순으로 더 좋은 경로를 찾으면 갱신
            if (!found || candidate < best) {
                best = candidate;
                found = true;
            }
        }
    }

    if (found) {
        cout << best;
    } else {
        cout << "-1";
    }

    return 0;
}

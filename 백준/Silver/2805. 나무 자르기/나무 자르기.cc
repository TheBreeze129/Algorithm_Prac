#include <iostream>
int main() {
	int n, m, max = 0;
	std::cin >> n >> m;
	int* a = new int[n];
	for (int i = 0; i < n; i++) {
		std::cin >> a[i];
		if (max < a[i]) {
			max = a[i];
		}
	}
	long long s = 0, e = max, k, x, ans;
	while (s <= e) {
		//std::cout << s << ' ' << e << '\n';
		k = (s + e) / 2;
		x = 0;
		for (int i = 0; i < n; i++) {
			if (a[i] > k) {
				x += a[i] - k;
			}
		}
		if (x < m) {
			e = k - 1;
		}
		else {
            ans = k;
            s = k + 1;
        }
	}
	std::cout << ans;
	return 0;
}
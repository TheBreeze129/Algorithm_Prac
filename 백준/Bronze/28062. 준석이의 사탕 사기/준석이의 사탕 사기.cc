#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N, T, i, cnt = 0;
	vector<int> odds;
	cin >> N;
	for (i = 0; i < N; i++) {
		cin >> T;
		if (T % 2) odds.push_back(T);
		else cnt += T;
	}
	if (cnt == 0 && odds.size() == 1) cout << 0;
	else {
		for (auto elem : odds) cnt += elem;
		if (odds.size() % 2 == 1) cnt -= *min_element(odds.begin(), odds.end());
		cout << cnt;
	}
}
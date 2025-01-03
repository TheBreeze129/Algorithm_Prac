#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N, T, i;
	vector<int> evens;
	vector<int> odds;
	cin >> N;
	for (i = 0; i < N; i++) {
		cin >> T;
		if (T % 2) odds.push_back(T);
		else evens.push_back(T);
	}
	if (evens.size() == 0 && odds.size() == 1) cout << 0;
	else {
		int all = 0;
		for (auto elem : evens) all += elem;
		for (auto elem : odds) all += elem;
		if (odds.size() % 2 == 1) all -= *min_element(odds.begin(), odds.end());
		cout << all;
	}
}
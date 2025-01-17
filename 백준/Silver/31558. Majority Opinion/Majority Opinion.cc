#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int T, N, i, l;
	cin >> T;
	for (l = 0; l < T; l++) {
		cin >> N;
		int* arr = new int[N];
		for (i = 0; i < N; i++) cin >> arr[i];
		vector<int> result;
		for (i = 0; i < N - 1; i++) {
			if (arr[i] == arr[i + 1] || (i < (N - 2) && arr[i] == arr[i + 2])) {
				result.push_back(arr[i]);
			}
		}
		sort(result.begin(), result.end());
		if (result.size() == 0) result.push_back(-1);
		for (i = 0; i < result.size()-1; i++) {
			if (result[i] != result[i + 1]) cout << result[i] << " ";
		}
		cout << result[result.size()-1] << endl;
	}

	return 0;
}	
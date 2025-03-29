#include <iostream>
#include <queue>
int main() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(0);
	std::cout.tie(0);
	int a, b, c, d, t1, t2;
	std::cin >> a >> b >> c >> d;
	std::vector<int> graph[1000];
	std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> pq;
	for (int i = 0; i < d; i++) {
		std::cin >> t1 >> t2;
		graph[t1 - 1].push_back(t2 - 1);
		graph[t2 - 1].push_back(t1 - 1);
	}
	bool visited[1000];
	for (int i = 0; i < 1000; i++) {
		visited[i] = false;
	}
	pq.push({ 0, a - 1 });
	while (!pq.empty()) {
		int cur = pq.top().second;
		int cost = pq.top().first;
		pq.pop();
		visited[cur] = true;
		if (cur == b - 1) {
			std::cout << cost;
			return 0;
		}
		for (int x : graph[cur]) {
			if (!visited[x]) {
			    visited[x] = true;
				pq.push({ cost + 1, x });
			}
		}
	}
	std::cout << -1;
	return 0;
}
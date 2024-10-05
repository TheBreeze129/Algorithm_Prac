#include <iostream>
using namespace std;

int N;
bool visited[9];
int num[9];

void perm(int idx) {
  if (idx == N) {
    for(int i=0;i<N;i++) cout << num[i] << " ";
    cout << endl;
    return;
  }
  for(int i=0;i<N;i++) {
    if (!visited[i]) {
      visited[i] = true;
      num[idx] = i+1;
      perm(idx+1);
      visited[i] = false;
    }
  }
}

int main() {
  cin >> N;
  perm(0);
}
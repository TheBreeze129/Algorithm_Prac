#include<iostream>
using namespace std;

int main() {
  int E, S, M, i=0;
  cin >> E >> S >> M;
  E--;
  S--;
  M--;
  while (true) {
    if (i%15==E && i%28==S && i%19==M) break;
    i++;
  }
  cout << ++i;
}
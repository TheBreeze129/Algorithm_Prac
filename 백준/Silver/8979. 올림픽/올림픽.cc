#include <iostream>
#include <algorithm>
using namespace std;

struct Country {
  int country;
  int gold;
  int silver;
  int bronze;
};

bool cmp(Country a, Country b) {
  if (a.gold > b.gold) return true;
  if (a.gold < b.gold) return false;
  if (a.silver > b.silver) return true;
  if (a.silver < b.silver) return false;
  if (a.bronze > b.bronze) return true;
  return false;
}

bool operator!=(Country a, Country b) {
  return (a.gold != b.gold || a.silver != b.silver || a.bronze != b.bronze);
}

int main() {
  int N, K;
  cin >> N >> K;
  Country* countries = new Country[N];
  for (int i=0; i<N; i++) cin >> countries[i].country >>countries[i].gold >> countries[i].silver >> countries[i].bronze;
  sort(countries, countries+N, cmp);
  int rank = 1;
  if (countries[0].country == K) cout << rank;
  else {
    for (int i=1; i<N; i++) {
      if (countries[i] != countries[i-1]) rank++;
      if (countries[i].country == K) {
        cout << rank;
        break;
      }
    }
  }
}

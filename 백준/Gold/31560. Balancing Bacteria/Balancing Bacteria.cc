#include <iostream>
#include <vector>
using namespace std;

using ll = long long;

int main() {

    int n; 
    cin >> n;
    vector<ll> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    ll ans = 0;
    ll contribution = 0;
    ll cnt_ops = 0;
    for (int i = 0; i < n; i++) {
        contribution += cnt_ops;
        a[i] += contribution;

        ll cur_ops = -a[i];
        ans += abs(cur_ops);
        cnt_ops += cur_ops;
        contribution += cur_ops;
    }

    cout << ans << '\n';
}
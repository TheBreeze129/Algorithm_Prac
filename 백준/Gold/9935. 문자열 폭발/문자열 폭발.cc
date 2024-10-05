#include <iostream>
#include <string>
using namespace std;

int main() {
  string input_str, boom;
  cin >> input_str;
  cin >> boom;
  string st = "";
  int boom_len = boom.size();
  for(int i=0;i<input_str.size();i++) {
    st.push_back(input_str[i]);
    if(st.size() >= boom_len) {
      if(st.substr(st.size()-boom_len,boom_len)==boom) st.erase(st.size()-boom_len, boom_len);
    }
  }
  if (st.size()) cout << st;
  else cout << "FRULA";
}
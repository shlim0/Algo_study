#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  string s[n];
  pair<int, int> data[1000];
  vector<int> str_int(1000, 0);

  for (int i = 0; i < n; i++) {
    cin >> s[i];
    data[i].first = s[i].length();
    data[i].second = i;
  }

  sort(data, data + n, greater<pair<int, int> >());

  int max_length = data[0].first;

  // max_length : 5, then "GCF" -> "00GCF"
  for (int i = 1; i < n; i++) {
    string tmp = s[data[i].second];
    s[data[i].second] = "";
    for (int j = 0; j < max_length - s[data[i].second].length() - 1; j++)
      s[data[i].second] += "0";

    s[data[i].second] += tmp;
  }

  int cnt = 9;
  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < n; j++) {
      // [0]의 자릿 수가 다른 수들보다 클 때
      char str = s[j][i];
      if (str != '0') {
        if (max_length-- > data[j].first && str_int[str] == 0) {
          str_int[str] = cnt;
          s[j][i] = cnt-- + '0';
          break;
        }
        // 비교 자릿수가 같아질 때, 그 값이 아직 없는 경우
        else if (str_int[str] == 0) {
          str_int[str] = cnt;
          s[j][i] = cnt-- + '0';
          max_length = data[j].first;
        }
        // 비교 자릿수가 같아질 때, 그 값이 이미 있는 경우
        else if (str_int[str] != 0) {
          s[j][i] = str_int[str] + '0';
          max_length = data[j].first;
        }
      }
    }
  }

  int ans = 0;

  // cout << endl << endl;
  for (int i = 0; i < n; i++) {
    stringstream ssInt(s[i]);
    int aa = 0;
    ssInt >> aa;
    // cout << aa << '\n';
    ans += aa;
    // cout << stoi(s[i]) << '\n';
    // cout << s[i] << endl << endl;
  }
  cout << ans;
}
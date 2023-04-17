// 17 min
#include <iostream>
using namespace std;

int main(void) {
  string a, b, min_a, max_a, min_b, max_b;
  cin >> a >> b;

  for (int i = 0; i < a.length(); i++) {
    if (a[i] == '5' || a[i] == '6') {
      min_a[i] = '5';
      max_a[i] = '6';
    } else {
      min_a[i] = a[i];
      max_a[i] = a[i];
    }
  }

  for (int i = 0; i < b.length(); i++) {
    if (b[i] == '5' || b[i] == '6') {
      min_b[i] = '5';
      max_b[i] = '6';
    } else {
      min_b[i] = b[i];
      max_b[i] = b[i];
    }
  }

  int min = stoi(min_a) + stoi(min_b);
  int max = stoi(max_a) + stoi(max_b);
  cout << min << " " << max << '\n';
}
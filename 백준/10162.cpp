// 구현까지 < 10 min. 디버깅때문에 20 min..
#include <iostream>
using namespace std;

int main(void) {
  int t;
  cin >> t;
  int unit[3] = {300, 60, 10};
  // 초기화 안하면 틀림
  int cnt[3] = {};

  for (int i = 0; i < 3 && t >= 0; i++) {
    if (t / unit[i] > 0) {
      cnt[i] += t / unit[i];
      t = t % unit[i];
    }
  }

  if (t == 0)
    for (int i = 0; i < 3; i++)
      cout << cnt[i] << " ";
  else
    cout << "-1";
}
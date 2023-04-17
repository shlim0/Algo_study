// 15 min
#include <iostream>
using namespace std;

int main(void) {
  int n, target = 0, cnt = 0;
  int unit[6] = {500, 100, 50, 10, 5, 1};
  cin >> n;
  target = 1000 - n;

  for (int i = 0; i < 6; i++)
    if (target >= unit[i]) {
      // i.e. 999 / 500 는 1 이다.
      cnt += target / unit[i];
      // i.e. 999 % 500 은 499 이다.
      target = target % unit[i];
    }

  cout << cnt;
}

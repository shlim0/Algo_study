// 19 min

#include <iostream>
using namespace std;

int main(void) {
  int n, cnt = 0;
  cin >> n;

  // 3으로 줄여가다가 5로 딱 떨어지는 경우 찾기
  while (n >= 3) {
    // 5로 딱 떨어지면 5로 나눠주고 나온다
    if (n % 5 == 0) {
      cnt += n / 5;
      n = 0;
      break;
    } else {
      // 아니면 계속 3씩 줄여나간다
      cnt++;
      n -= 3;
    }
  }

  // 남은 값이 없는 경우
  if (n == 0)
    cout << cnt;
  // 남은 값이 있는 경우
  else
    cout << "-1";
}
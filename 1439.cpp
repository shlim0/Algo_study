// 10 min
#include <iostream>
using namespace std;

int main(void) {
  string s;
  cin >> s;

  int zero = 0, one = 0;
  int zero_continue = 0, one_continue = 0;

  for (int i = 0; i < s.length(); i++) {
    // '1'을 연속치 않게 받는 경우
    if (s[i] == '1' && one_continue == 0) {
      zero_continue = 0;
      one_continue = 1;
      one++;
      // '0'을 연속치 않게 받는 경우
    } else if (s[i] == '0' && zero_continue == 0) {
      one_continue = 0;
      zero_continue = 1;
      zero++;
    }
  }

  // '0'과 '1' 중 덜 뒤집는 경우가 정답이 된다.
  if (zero < one)
    cout << zero << '\n';
  else
    cout << one << '\n';
}
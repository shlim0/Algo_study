// 45 min
#include <cstddef>
#include <iostream>
#include <string>
using namespace std;

int main(void) {
  long a, b_int, cnt = 0;
  string b;

  cin >> a >> b;
  b_int = stoi(b);

  while (b_int > a) {
    if (b_int % 2 == 0) {
      b_int /= 2;
      b = to_string(b_int);
    } else if (b[b.length() - 1] == '1') {
      b.erase(b.length() - 1);

      // b.erase()과 같은 의미의 코드
      //   string tmp = "";
      //   for (int i = 0; i < b.length() - 1; i++) {
      //     tmp += b[i];
      //   }
      //   b = tmp;
      if (b.length() != 0)
        b_int = stoi(b);
    }
    cnt++;
  }

  if (b_int != a)
    cout << -1 << '\n';
  else
    cout << cnt + 1 << '\n';
}
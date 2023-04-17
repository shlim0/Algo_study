#include <iostream>
using namespace std;

int main(void) {
  long a, b, cnt = 0;
  cin >> a >> b;

  while (true) {
    if (a > b) {
      cout << -1;
      break;
    } else if (a == b) {
      cnt++;
      cout << cnt;
      break;
    }

    if (b % 2 == 0) {
      b /= 2;
    } else if (b % 10 == 1) {
      b--;
      b /= 10;
    } else {
      cout << -1;
      break;
    }
    cnt++;
  }
}
// 30 min(idea) + 27 min(implementation)
#include <iostream>
using namespace std;

int main(void) {
  long long s;
  cin >> s;

  for (int i = 1;; i++) {
    s -= i;
    if (s <= i) {
      cout << i;
      break;
    }
  }
}

// i=0) 200
// i=1) 199 1
// i=2) 197 2 1
// i=3) 194 3 2 1
// ...
// i=19) 29  18 17 16 15 14 13 12 11 10
//            1  2  3  4  5  6  7  8  9

// i=20) 10  19 ... -> 10이 중복

// 10 0
// i=1) 9 1
// i=2) 7 2 1
// i=3) 4 3 2 1
// i=4) 0 4 3 2 1

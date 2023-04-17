// from https://nanyoungkim.tistory.com/114
#include <cmath>
#include <iostream>
using namespace std;

int main() {

  long S;
  cin >> S;

  long ans = 0;
  long start = 1;
  long end = S;

  while (start <= end) {
    long mid = (start + end) / 2;

    if (mid * (mid + 1) / 2 <= S) {
      ans = mid;
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  cout << ans;

  return 0;
}
#include <iostream>
#include <queue>
using namespace std;

int main(void) {
  long x;
  cin >> x;
  // value, cnt
  queue<pair<long, long> > q;
  q.push(make_pair(x, 0));

  while (!q.empty()) {
    long val = q.front().first;
    long cnt = q.front().second;
    cnt++;
    if (val == 1) {
      cout << q.front().second << '\n';
      break;
    }

    if (val % 3 == 0)
      q.push(make_pair(val / 3, cnt));
    if (val % 2 == 0)
      q.push(make_pair(val / 2, cnt));
    if (val)
      q.push(make_pair(--val, cnt));

    q.pop();
  }
}

// 10
// x 5      9
//   4       3    8
//   2 3    1 2
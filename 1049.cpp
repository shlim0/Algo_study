// 35 min
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(vector<int> &a, vector<int> &b) {
  if (a[1] == b[1])
    return a < b;
  else
    return a[1] < b[1];
}

int main(void) {
  int n, m;
  cin >> n >> m;
  vector<vector<int> > v(m, vector<int>(2, 0));
  for (int i = 0; i < m; i++)
    cin >> v[i][0] >> v[i][1];

  // v[i][0]애 대해 오름차순 정렬
  sort(v.begin(), v.end());
  int package = v[0][0];

  // v[i][1]애 대해 오름차순 정렬
  sort(v.begin(), v.end(), cmp);
  int unit = v[0][1];

  // 묶음으로 사는게 낱개로 6개 사는 것 보다 비싼 경우
  if (package > unit * 6)
    package = unit * 6;

  int res = 0;
  while (n > 0) {
    if (n < 6) {
      // 6개 미만 개수의 줄을 살 때, 낱개로 사는 것보다 묶음으로 사는 게 더 싼 경우
      if (unit * n > package) {
        res += package;
      } else
        res += unit * n;
      break;
    } else {
      res += package * (n / 6);
      n -= 6 * (n / 6);
    }
  }
  cout << res << '\n';
}
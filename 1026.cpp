// 11 min
#include <algorithm>
#include <iostream>
using namespace std;

int cmp(int b1, int b2) { return b1 > b2; }

int main(void) {
  int n, res = 0;
  cin >> n;
  int a[n], b[n];

  for (int i = 0; i < n; i++)
    cin >> a[i];

  for (int i = 0; i < n; i++)
    cin >> b[i];

  // 오름차순 정렬
  sort(a, a + n);

  // 내림차순 정렬
  sort(b, b + n, cmp);
  // sort(b, b + n, greater<int>()); 과 동일

  for (int i = 0; i < n; i++)
    res += a[i] * b[i];

  cout << res;
}
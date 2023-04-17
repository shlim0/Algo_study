// 17 min
#include <iostream>
#include <vector>
using namespace std;

int main(void) {
  int l[10000], p[10000], v[10000], cnt = 0;
  for (int i = 0;; i++, cnt++) {
    cin >> l[i] >> p[i] >> v[i];
    if (l[i] == 0 && p[i] == 0 && v[i] == 0)
      break;
  }

  vector<int> ans(cnt, 0);
  for (int i = 0; i < ans.size(); i++) {
    ans[i] = l[i] * (v[i] / p[i]);
    if (v[i] % p[i] < l[i])
      ans[i] += v[i] % p[i];
    else
      ans[i] += l[i];
    cout << "Case " << i + 1 << ": " << ans[i] << '\n';
  }
}

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(void) {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  long long n, k;
  cin >> n >> k;

  pair<long long, long long> jewel[n];
  long long bag[k];

  for (int i = 0; i < n; i++)
    cin >> jewel[i].first >> jewel[i].second;

  for (int i = 0; i < k; i++)
    cin >> bag[i];

  sort(jewel, jewel + n);
  sort(bag, bag + k);

  int res = 0;
  int j = 0;
  priority_queue<long long> pq;
  for (int i = 0; i < k; i++) {
    for (; j < n && bag[i] >= jewel[j].first;) {
      pq.push(jewel[j].second);
      j++;
    }

    if (!pq.empty()) {
      res += pq.top();
      pq.pop();
    }
  }

  cout << res << '\n';
}
#include <iostream>
#include <vector>
using namespace std;

int main(void) {
  long long n, total = 0;
  cin >> n;

  vector<long long> dis(n, 0);
  vector<long long> cost(n, 0);

  for (int i = 0; i < n - 1; i++)
    cin >> dis[i];

  for (int i = 0; i < n; i++)
    cin >> cost[i];

  // 첫 도시에서는 무조건 주유를 해야 출발할 수 있다.
  total = dis[0] * cost[0];
  // 첫 도시에서의 가격을 기준으로 비교해 나간다.
  int cost_now = cost[0];

  for (int i = 1; i < n; i++) {
    if (cost_now > cost[i]) {
      // 기름값 최소화
      cost_now = cost[i];
      total += cost_now * dis[i];
    } else {
      total += cost_now * dis[i];
    }
  }

  cout << total;
}
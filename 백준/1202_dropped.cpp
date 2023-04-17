// 55 min
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

bool cmp(pair<int, int> a, pair<int, int> b) {
  if (a.first == b.first)
    return a.second < b.second;
  else
    return a.first < b.first;
}

int main(void) {
  long long n, k;
  cin >> n >> k;

  vector<pair<long long, long long> > jewel(n, make_pair(0, 0));
  // 가방에 여러 개의 보석이 들어올 수 있다고 생각했었음....
  priority_queue<long long, vector<long long>, greater<long long> > c;

  // 가격을 기준으로 정렬하기 위해 가격 먼저 입력받음
  for (int i = 0; i < n; i++)
    cin >> jewel[i].second >> jewel[i].first;

  // 가방을 우선순위 큐에 삽입
  for (int i = 0; i < k; i++) {
    int tmp = 0;
    cin >> tmp;
    c.push(tmp);
  }

  // 가격을 기준으로 오름차순 정렬을 하되, 가격이 같다면 무게를 오름차순 정렬
  sort(jewel.begin(), jewel.end(), cmp);

  int res = 0;
  for (int i = 0; i < k; i++) {
    if (!c.empty()) {
      int bag_size = c.top();
      // 가방 사용
      c.pop();
      // 가격이 비싼 보석부터 가방에 넣자
      for (int j = jewel.size() - 1; j >= 0; j--) {
        // 가방에 들어갈 수 있는 무게면 가방에 넣기
        if (bag_size >= jewel[j].second) {
          res += jewel[j].first;
          // 보석 훔침
          jewel.pop_back();
          break;
        }
      }
    } else
      break;
  }

  cout << res << '\n';
}
// 개수 무게 가격
// n   m   v
// k   c

// 무게당 가격이 높을 수록 최대값
// 반례
// 2 1
// 5 10
// 100 100
// 100
// 무게당 가격은 틀렸다.

// 10 2
// 2 10
// m = pq.top();
// pq.pop();
// pq.push(m - m[i]);
// 1 10

// if (m[i] > pq.top())
// pq.pop();
// 10

// 12 20
// 16 16
// 20 0

// 7 14 17

// 3 3
// 1 10
// 2 20
// 1 20
// 3
// 2
// 1
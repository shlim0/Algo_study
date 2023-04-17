#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(void) {
  long n;
  cin >> n;
  vector<long> v(n, 0); 
  for (int i = 0; i < n; i++)
    cin >> v[i];

  // C++에서 priority queue의 root node에 큰 값부터 들어가도록 되어있다.
  // 즉, default로 max heap이 구성된다.
  // 따라서, 내림차순이 아닌 오름차순으로 priority queue를 구성하려면 greater<>를 사용해야 한다.
  // 즉, min heap이 구성된다.
  priority_queue<long, vector<long>, greater<long> > pq;

  // priority queue에 cin 할 수 없으니 vector로 받고 pq에 입력
  for (int i = 0; i < n; i++) {
    pq.push(v[i]);
  }

  int acc = 0; // accumulate: 합산
  while (true) {
    int cmp1 = pq.top();
    pq.pop();
    // cmp1이 마지막 남은 원소였다면 계산할 수 없으므로 비어있지 않은 경우에만 계산
    if (!pq.empty()) {
      int cmp2 = pq.top();
      pq.pop();

      acc += cmp1 + cmp2;
      pq.push(cmp1 + cmp2);
    }
    // cmp1이 마지막 남은 원소였을 경우
    else {
      break;
    }
  }
  cout << acc;
}
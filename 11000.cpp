#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct cmp {
  bool operator()(pair<long, long> &a, pair<long, long> &b) {
    if (a.second == b.second)
    // .second 값을 기준으로 정렬하는 게 목표라서 a.first < b.first 여도 상관없다.
      return a.first > b.first;
    else {
      return a.second > b.second;
    }
  }
};

int main(void) {
  long n;
  cin >> n;

  vector<pair<long, long> > v(n);
  priority_queue<pair<long, long>, vector<pair<long, long> >, cmp> pq;

  for (int i = 0; i < n; i++)
    cin >> v[i].first >> v[i].second;

  sort(v.begin(), v.end());

  // 초기값 설정
  long end = v[0].second;
  pq.push(make_pair(v[0].first, v[0].second));

  for (int i = 1; i < n; i++) {
    // 이전 수업에 연달아 있는 수업이면 계속 강의실 사용
    // i.e. 1-3시 수업 다음 3-5시 수업이 오면 1-5시까지 한 강의실만 사용 하면 됨
    if (pq.top().second <= v[i].first) {
      long start = pq.top().first;
      pq.pop();
      pq.push(make_pair(start, v[i].second));
    } else {
      // 또 다른 수업 추가
      pq.push(make_pair(v[i].first, v[i].second));
    }
  }

  // for 문이 끝나면 강의실 수(==pq.size()) 마다 수업 시간표가 짜여져 있게 됨
  cout << pq.size() << '\n';
}

// 4
// 1 1
// 1 3
// 2 4
// 3 5

// 8
// 1 8
// 9 16
// 3 7
// 8 10
// 10 14
// 5 6
// 6 11
// 11 12
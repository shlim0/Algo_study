#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {

  int n, cnt = 0, end_time = 0;
  cin >> n;

  vector<vector<int> > v(n, vector<int>(2, 0));
  for (int i = 0; i < n; i++)
    // 회의 종료 시간을 먼저 입력 받는다
    cin >> v[i][1] >> v[i][0];

  // 회의 종료 시간 기준으로 정렬
  sort(v.begin(), v.end());

  cnt++;
  end_time = v[0][0];

  for (int i = 1; i < n; i++) {
    // end_time을 이용하지 않으면 이중 for를 써야한다.
    if (end_time <= v[i][1]) {
      end_time = v[i][0];
      cnt++;
    }
  }
  cout << cnt;
}
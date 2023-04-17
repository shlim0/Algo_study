#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(void) {
  int t, n;
  cin >> t;
  vector<int> cnt(t, 0);

  for (int i = 0; i < t; i++) {
    cin >> n;
    // 정렬 후 첫 지원자는 서류 점수가 1등이므로 무조건 합격이다.
    cnt[i] = 1;
    vector<vector<long> > arr(n, vector<long>(2, 0));

    for (int j = 0; j < n; j++)
      cin >> arr[j][0] >> arr[j][1];

    sort(arr.begin(), arr.end());
  
    // 정렬 후 첫 지원자를 기준으로 한다.
    int min = arr[0][1];

    for (int k = 1; k < n; k++) {
      // 면접 순위가 낮은 경우일 경우 기준을 변경
      // 그래야 어떤 지원자랑 비교하더라도 서류, 면접 둘 다 열등하지 않는 지원자가 나올 수 있다.
      if (min > arr[k][1]){
        min = arr[k][1];
        cnt[i]++;
      }
    }
  }

  for (int i = 0; i < cnt.size(); i++)
    cout << cnt[i] << "\n";
}

// 1 4 
// 2 3 
// 3 2 
// 4 1 
// 5 5 x 
// -> 4명 

// 1 4 
// 2 5 x
// 3 6 x
// 4 2 
// 5 7 x
// 6 1 
// 7 3 x
// -> 3명
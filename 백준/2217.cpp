// 18 min
#include <algorithm>
#include <iostream>
using namespace std;

int main(void) {
  int n, w;
  cin >> n;
  int arr[n];

  for (int i = 0; i < n; i++)
    cin >> arr[i];

  // 오름차순 정렬
  sort(arr, arr + n);

  // 비교 기준 설정
  w = arr[n - 1];

  // 뒤에서 두번째 값부터 평균 내기
  for (int i = n - 2, cnt = 2; i >= 0; i--) {
    if (w < arr[i] * cnt)
      w = arr[i] * cnt;
    cnt++;
  }
  cout << w;
}
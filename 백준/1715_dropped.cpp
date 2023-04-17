// 38 min
#include <algorithm>
#include <iostream>
using namespace std;
int main(void) {
  long n;
  cin >> n;
  long arr[n];
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  sort(arr, arr + n);

  int acc = 0;
  arr[1] = arr[0] + arr[1];
  acc = arr[1];
  arr[0] = 0;

  for (int i = 2; i < n; i++) {
    // i-1번째 계산 결과가 i번째와 i+1번째 값보다 큰 경우 i-1번째 원소는 계산에 포함되면 안된다.
    if ((arr[i - 1] > arr[i]) && (arr[i - 1] > arr[i + 1])) {
      arr[i] = arr[i] + arr[i + 1];
      arr[i + 1] = 0; // 계산 완료 처리
      acc += arr[i];
      // 시간 초과를 방지하기 위한 정렬 범위(i-1 ~ i+1) 설정
      // sort(arr + i - 1, arr + i + 1);
    } else {
      arr[i] += arr[i - 1];
      acc += arr[i];
    }
  }
  cout << acc;
}

// 10 20 40 80  100 110 120
//    30 70 150 210

// 10 + 20 = 30
// 30 + 40 = 70        100
// 70 + 80 = 150       250

// ((150 + 100) + 110)

// 150 + (100 + 110)

// test case
// 7
// 10
// 20
// 40
// 80
// 100
// 110
// 120

// 30 + 70 + 150 + 210 + 270 + 480 = 1210
// 55 min + 45 min(debugging)
#include <algorithm>
#include <iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  int arr[n];
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  sort(arr, arr + n);

  long res = 0;

  // 0 이하 정수를 앞에서 부터 연산
  int lower_cnt = 0;
  // 2개씩 연산을 하다가 n을 초과하면 인덱스를 침범하므로
  while (lower_cnt + 1 < n) {
    if (arr[lower_cnt] <= 0 && arr[lower_cnt + 1] <= 0) {
      res += arr[lower_cnt] * arr[lower_cnt + 1];
      lower_cnt += 2;
    } else
      break;
  }

  // 1 이상 정수를 뒤에서 부터 연산
  int upper_cnt = n;
  // 연산할 값이 1개밖에 남지 않은 경우 비교할 수 없음
  while (upper_cnt - lower_cnt > 1) {
    // i.e. 남은 수가 4 5 인 경우
    if (arr[upper_cnt - 2] > 1 && arr[upper_cnt - 1] > 1) {
      res += arr[upper_cnt - 2] * arr[upper_cnt - 1];
      upper_cnt -= 2;
      // i.e. 남은 수가 1 2 만 있는 경우
    } else if (arr[upper_cnt - 2] == 1 && arr[upper_cnt - 1] >= 1) {
      res += arr[upper_cnt - 2] + arr[upper_cnt - 1];
      upper_cnt -= 2;
    } else
      break;
  }

  // 연산이 끝나지 않은 수가 있는 경우
  if (upper_cnt != lower_cnt) {
    // n이 홀수인 경우
    if (n % 2 == 1)
      res += arr[lower_cnt];
    // n이 짝수인 경우
    else
      res += arr[lower_cnt] + arr[upper_cnt - 1];
  }
  cout << res << '\n';
}

// -1 1 2 3  -> 6
// 1이하의 수는 +

// 0 1 2 3 4 5 -> 27

// -1 -> -1
// 하나만 있으면 그대로 출력

// -1 0 1 -> 1
// 0보다 작은 수와 0이 있는경우, 0보다 작은 수 중 최소 * 0
// 앞에서 부터하면 1
// 뒤에서 부터하면 0

// 1 1 -> 2
// 1은 +

// // + or * 비교
// 1. - - -> * 하면 +가 되기에 *
// 2. - 0 -> * 하면 0이 되기에 *
// 3. - +
//    + - -> * 하면 무조건 -가 되기에 +
// 4. + 0 -> * 하면 무조건 0이 되기에 +
// 5. + + -> * 하면 +이 되기에 * (단, 하나라도 1인 경우 +)
// 6. 0 0 -> 뭘 하든 0이 되므로 + or * 상관없다

// 3 -1 -1 0
// 정답 : 1
// 앞에서 부터하면 1
// 뒤에서 부터하면 -1

// 3 1 2 3
// 앞에서 부터하면 6
// 뒤에서 부터하면 7
// 정답 : 7

// 5 1 1 1 4 5
// 정답 : 23

// 결론
// 1. -1 0 1 을 제외하곤 무지성 연산 해도 됨
// 2. 1 초과 양수는 뒤에서부터 읽어서 양수끼리 *을 많이 하면 최대
// 3. 1 은 +을 많이 하면 최대
// 4. 0 이하 정수는 앞에서부터 읽어서 *을 많이 하면 최대
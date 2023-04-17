// 20 min
#include <iostream>
using namespace std;

int main(void) {
  int n, k, cnt = 0;
  cin >> n >> k;

  int arr[n];
  // index를 0 ~ <n이 아니라 1 ~ <=n 으로 해야 정신건강에 이로움
  for (int i = 1; i <= n; i++)
    cin >> arr[i];

  // 큰 단위부터 계산해보자
  for (int i = n; i > 0; i--) {
    // i.e. 4600원 일때, mul_cnt = 4 (int형이니 4600 / 1000에서 600원은 버린다)
    int mul_cnt = k / arr[i];
    // 반례. 370 / 1000 은 mul_cnt가 0 이므로 계산할 필요가 없다
    if (mul_cnt > 0) {
      cnt += mul_cnt;
      k -= mul_cnt * arr[i];
      // 쪼개다가 쪼갤개 없으면 break
      if (k == 0)
        break;
    }
  }

  cout << cnt << '\n';
}
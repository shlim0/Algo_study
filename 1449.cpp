#include <algorithm>
#include <iostream>
using namespace std;

int main(void) {
  int n, l;
  cin >> n >> l;
  int arr[n];
  for (int i = 0; i < n; i++)
    cin >> arr[i];

  sort(arr, arr + n);

  int start = arr[0], cnt = 1;

  for (int i = 1; i < n; i++) {
    // if (arr[i] - start + 1 == l) {
    //   start = arr[i + 1];
    //   i++;
    //   // cnt++;
    // } else
    if (arr[i] - start + 1 > l) {
      start = arr[i];
      cnt++;
    }
  }

  // if (start == arr[n - 1])
  //   cnt++;

  cout << cnt << '\n';
}

// 4 2
// 1 2 100 101
// 0.5~1.5 1.5~2.5 99.5~100.5 100.5~101.5

// 4 3
// 1 2 3 4
// 0.5~1.5 1.5~2.5 2.5~3.5 3.5~4.5

// 3 1
// 1 2 3
// 0.5~1.5 1.5~2.5 2.5~3.5
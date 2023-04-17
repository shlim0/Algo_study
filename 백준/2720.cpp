// 8 min
#include <iostream>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  int arr[n];

  for (int i = 0; i < n; i++)
    cin >> arr[i];

  for (int i = 0; i < n; i++) {
    int q, d, n, p;

    q = arr[i] / 25;
    arr[i] %= 25;

    d = arr[i] / 10;
    arr[i] %= 10;

    n = arr[i] / 5;
    arr[i] %= 5;

    p = arr[i];

    cout << q << " " << d << " " << n << " " << p << '\n';
  }
}
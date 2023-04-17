// 19 min
#include <algorithm>
#include <iostream> //컴파일러에 따라 sort() 이용시 include 해야함
using namespace std;

int n, sum = 0;

int main(void) {
  cin >> n;
  int p[n], wait[n];
  for (int i = 0; i < n; i++)
    cin >> p[i];

  // 오름차순 정렬
  sort(p, p + n);

  for (int i = 0; i < n; i++) {
    // 배열 초기화 안되면 쓰레기값이 들어가서 추가함
    wait[i] = 0;

    for (int j = 0; j <= i; j++) {
      // i번째 사람이 기다리게 되는 시간은 앞에 있는 사람들의 p[j]에 결정된다
      wait[i] += p[j];
    }
    sum += wait[i];
  }
  cout << sum << '\n';
}
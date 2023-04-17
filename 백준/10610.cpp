#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(void) {
  string s;
  cin >> s;

  vector<int> v;
  // vector<int> v(s.size());
  for (int i = 0; i < s.size(); i++)
    // v[i] = s[i] - '0';
    v.push_back(s[i] - '0');

  // 내림차순 정렬
  // 가장 작은 값이 0인지 확인하기 위함
  sort(v.begin(), v.end(), greater<int>());

  int sum = 0;
  for (int i = 0; i < v.size(); i++) {
    sum += v[i];
  }

  // 가장 작은 값이 0이어서 10의 배수인가 && 각 자리수를 더한게 3의 배수인가 -->
  // 30의 배수인가
  if (v[v.size() - 1] == 0 && sum % 3 == 0)
    for (int i = 0; i < v.size(); i++)
      cout << v[i];
  else
    cout << -1;
}
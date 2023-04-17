// 1.5 hours
#include <algorithm>
#include <functional>
#include <iostream>
#include <math.h>
#include <string>
#include <vector>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  string s[n];
  //   pair<int, char> str_int[1000];
  vector<int> str_int(1000, 0);

  // 데이터 입력
  for (int i = 0; i < n; i++) {
    cin >> s[i];
    for (int j = 0; j < s[i].length(); j++) {
      char alphabet = s[i][j];
      str_int[alphabet] +=
          (pow(10, s[i].length() - j - 1)); // 자릿수 마다의 가중치 합산
      //   str_int[alphabet].second = alphabet; // 해당하는 알파벳 기억하기
    }
  }

  // 가중치 기준으로 내림차순 정렬
  //   sort(str_int, str_int + 1000, greater<pair<int, int> >());
  sort(str_int.begin(), str_int.end(), greater<int>());

  //   인덱스
  int res = 0;
  for (int i = 0; i < 10; i++) {
    res += str_int[i] * (9 - i);
  }
  cout << res << '\n';

  //   문자열
  // 가중치가 높은 순으로 9~0 까지 값을 반영
  //   for (int i = 0; i < 10; i++)
  //     str_int[i].first = 9 - i;

  //   int res = 0;

  //   // s[i ~< n]
  //   for (int i = 0; i < n; i++) {
  //     // s[i][j ~< s[i].length]
  //     for (int j = 0; j < s[i].length(); j++) {
  //       // 알파벳은 9~1까지 가중치만 가치있으므로 k < 10
  //       for (int k = 0; k < 10; k++) {
  //         // 입력받은 알파벳의 가중치를 대입해주기 위함
  //         if (s[i][j] == str_int[k].second) {
  //           // + '0' : int to char
  //           s[i][j] = str_int[k].first + '0';
  //           break;
  //         }
  //       }
  //     }
  //     res += stoi(s[i]);
  //   }
  //   cout << res << '\n';
}
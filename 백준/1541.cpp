// 1 hour
#include <iostream>
#include <string>
using namespace std;

int main(void) {
  int res = 0;
  bool isMinus = false;
  string s, tmp = "";
  cin >> s;

  for (int i = 0; i < s.size(); i++) {
    // 수식을 계속 더한다
    tmp += s[i];
    // i) '-' 나오기 전까지의 모든 수식을 res에 더한다
    if (!isMinus && s[i] == '+') {
      res += stoi(tmp);
      tmp = "";
    }
    // ii) 처음 '-'을 만난 순간
    else if (!isMinus && s[i] == '-') {
      isMinus = true;
      // 여태까지의 수식을 res에 더한다
      res += stoi(tmp);
      tmp = "";
    }
    // iii) '-' 나온 후 모든 수식을 뺀다
    else if (isMinus && (s[i] == '-' || s[i] == '+')) {
      res -= stoi(tmp);
      tmp = "";
    }
  }
  // '+' or '-' 연산자가 끝난 후 남은 수식 계산
  if (isMinus)
    res -= stoi(tmp);
  else if (!isMinus)
    res += stoi(tmp);

  cout << res << '\n';
}
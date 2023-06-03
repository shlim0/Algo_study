#include <bits/stdc++.h>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    map<char, int> m;

    for(int i=0; i<s.size(); i++)
     // m[s[i]] = 0;으로 하고 if에 두면 뒤에 오는 글자도 -1이 되니 주의.
        m[s[i]] = -1;
    
    for(int i=0; i<s.size(); i++)
    {
       if(m[s[i]] == -1)
       {
          answer.push_back(-1);
           m[s[i]] = i;
       }
       else
       {
           answer.push_back(i - m[s[i]]);
           m[s[i]] = i;
       }
        
    }
    return answer;
}
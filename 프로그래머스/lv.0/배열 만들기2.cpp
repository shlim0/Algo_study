#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int l, int r) {
    vector<int> a;
    
    // 더하다가 5랑 0만 포함된거 찾으면 되잖아
    for(int i=l; i<=r; i++)
    {
        string s = to_string(i);
        
        int cnt = 0;
        for(int j=0; j<s.length(); j++)
            if((int)s[j] - '0' == 0 || (int)s[j] - '0' == 5)
            {
                cnt++;
                if(cnt == s.length())
                    a.push_back(stoi(s));
            }
    }
    if(a.empty())
        return {-1};
    
    return a;
}
#include <bits/stdc++.h>

using namespace std;

int solution(string t, string p) {
    int res = 0;
    
    for(int i=0; i < t.size() - p.size() + 1; i++)
    {
        string str = t.substr(i, p.size());
        // 굳이 stoi() 할 필요 없음...
        if(str <= p) res++;
    }
    return res;
}
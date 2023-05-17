// 13 min
#include <bits/stdc++.h>
using namespace std;

vector<string> solution(vector<string> p, int k) {
    vector<string> a;
    
    // picture 끝까지
    for(int i=0; i<p.size(); i++)
    {
        string tmp = "";
        
        // picture[i] 끝까지
        for(int j=0; j<p[i].length(); j++)
            // picture[i][j]를 k배씩 늘리기
            for(int l=0; l<k; l++)
                tmp += p[i][j];
        
        // picture[i]를 k배씩 늘리기
        for(int o=0; o<k; o++)
            a.push_back(tmp);
    }
    return a;
}
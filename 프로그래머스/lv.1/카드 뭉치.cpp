// 7 min
#include <bits/stdc++.h>

using namespace std;

string solution(vector<string> c, vector<string> cc, vector<string> g) {
    queue<string> q, qq;
    
    for(auto v : c)
        q.push(v);
    
    for(auto v : cc)
        qq.push(v);
    
    for(auto v : g)
    {
        if(q.front() == v)
            q.pop();
        else if(qq.front() == v)
            qq.pop();
        else return "No";
    }
    return "Yes";
}
// < 10 min
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> n, vector<int> y, vector<vector<string>> p) {
    vector<int> a;
    map<string, int> m;
    
    for(int i=0; i<n.size(); i++)
        m.insert({n[i], y[i]});
    
    for(auto row : p)
    {
        int val = 0;
        for(auto v : row)
            if(m[v])
                val += m[v];
        a.push_back(val);
    }
    
    
    return a;
}
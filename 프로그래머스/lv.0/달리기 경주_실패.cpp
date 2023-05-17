// 40 min + 1h -> wrong
// brute force --> time over
#include <bits/stdc++.h>

using namespace std;

vector<string> solution(vector<string> p, vector<string> c) {
    map<string, int> m;
    map<int, string> m2;
    
    for(int i=0; i<p.size(); i++){
        m.insert({p[i], i});
        m2.insert({i, p[i]});
    }
    
    
    for(auto v : c)
    {
        
        // m) mumu soe poe kai mine
             // 0   1   2   3   4
        // m2)  0   1   2   3   4
         //   mumu soe poe kai mine
        
        // i.e. start, "kai"
        
        --m[v];
            // m["kai"]--;
        // m) mumu soe poe kai mine
             // 0   1   2   2   4
            // m2[m["kai"]] ==> m2[2] ==> poe
        
        
            // m["poe"]++;
        m[m2[m[v]]]++;
        // m) mumu soe poe kai mine
             // 0   1   3   2   4
        
            // m2[m["kai"]+1] = "poe"==> m2[3] = "poe"
        m2[m[v]+1] = m[v];
        // m2)  0   1   2   3   4
         //   mumu soe poe poe mine
        
            // m2[m["kai"]] = "kai"  ==> m2[2] = "kai"
        m2[m[v]] = v;
        // m2)  0   1   2   3   4
         //   mumu soe kai poe mine
        
    }

    
    vector<string> a;
    for(int i=0; i<m2.size(); i++)
        a.push_back(m2[i]);
    
    
    return a;
}
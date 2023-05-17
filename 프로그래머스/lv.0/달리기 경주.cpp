// 답지보고 이해 11 min

#include <bits/stdc++.h>

using namespace std;

vector<string> solution(vector<string> p, vector<string> c) {
    vector<string> a;
    map<int, string> is;
    map<string, int> si;
    
    for(int i=0; i<p.size(); i++)
    {
        is.insert({i, p[i]});
        si.insert({p[i], i});
    }
    
    for(auto v : c)
    {
        int curr_idx = si[v];
        string to_change = is[curr_idx - 1];
        
        is[curr_idx] = to_change;
        is[curr_idx - 1] = v;
        si[v] = curr_idx - 1;
        si[to_change] = curr_idx;
    }
    
    for(int i=0; i<is.size(); i++)
    {
        a.push_back(is[i]);
    }
    
    return a;
}


// #include <string>
// #include <vector>
// #include <map>
// using namespace std;

// vector<string> solution(vector<string> players, vector<string> callings)
// {
//     vector<string> answer;
//     map<int, string> m1;
//     map<string, int> m2;
//     for(int i=0;i<players.size();i++)
//     {
//         m1[i] = players[i];
//         m2[players[i]] = i;
//     }
//     for(int i=0;i<callings.size();i++)
//     {
//         int cur_idx = m2[callings[i]];//호출 선수 이름, 순위
//         string change = m1[cur_idx - 1];//앞선 선수 이름, 순위
//         m1[cur_idx - 1] = callings[i];
//         m1[cur_idx] = change;
//         m2[callings[i]] = cur_idx - 1;
//         m2[change] = cur_idx;
//     }
//     for(auto c : m1) answer.push_back(c.second);
//     return answer;
// }        
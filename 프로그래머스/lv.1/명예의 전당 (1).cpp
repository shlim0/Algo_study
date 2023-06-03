#include <bits/stdc++.h>
using namespace std;

vector<int> solution(int k, vector<int> score) {
    vector<int> top, res;
    
    for(auto v : score)
    {   
        if(top.size() < k){
            top.push_back(v);
            sort(top.begin(), top.end());
            res.push_back(top[0]);
        }
        else if(top[0] < v)
        {
            top.erase(top.begin() + 0);
            top.push_back(v);
            sort(top.begin(), top.end());
            // cout << v << " " << top[0] << '\n';
            res.push_back(top[0]);
        }
        else
            res.push_back(top[0]);
    }
    return res;
}

// 다른 사람의 코드
// #include <string>
// #include <vector>
// #include <algorithm>

// using namespace std;

// vector<int> solution(int k, vector<int> score) {
//     vector<int> answer, tmp;

//     for(auto s : score){
//         tmp.push_back(s);
//         sort(tmp.begin(), tmp.end(), greater<int>());
//         if(tmp.size() >= k) tmp.erase(tmp.begin() + k, tmp.end());
//         answer.push_back(tmp.back());
//     }

//     return answer;

// }
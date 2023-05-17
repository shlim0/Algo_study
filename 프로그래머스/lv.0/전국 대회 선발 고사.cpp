// 14 min
#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> rank, vector<bool> attendance) {
    int answer = 0;
    vector<int> past_rank = rank;
    vector<int> res;
//     3 ~ 99, 3 of 100
//         best 3 but possible best 3.
        
//         rank[]
//         attendance[]
        
//         a, b, c -> 10000*a + 100*b + c
    
    sort(rank.begin(), rank.end());
    
    // 1 2 3 4 5 6 7
    // 3 7 2 5 4 6 1
    
    for(int i=1; i<=rank.size(); i++)
    {
        for(int j=1; j<=past_rank.size(); j++)
        if (rank[i-1] == past_rank[j-1])
            if(attendance[j-1])
                res.push_back(j-1);
    }
    
    answer = 10000 * res[0] + 100 * res[1] + res[2];       
    
    return answer;
}
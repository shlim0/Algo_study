// 9 min test_case : 47/50 
// 14 min total.
// O(n^2)
#include <bits/stdc++.h>

using namespace std;

int solution(int n, int m, vector<int> s) {
    int cnt = 0;
    int j_memo = 0;
    
    for(int i=0; i<n; i++)
    {
        for(int j=j_memo; j<s.size(); j++)
        {   
            // counter example : 1, 1, [1]
            if(i == s[j]-1)
            {
                i = s[j]-1 + m;
                j_memo++;
                cnt++;
            }
        }
    }
    
    return cnt;
}

// O(n)
// #include <string>
// #include <vector>

// using namespace std;

// int solution(int n, int m, vector<int> section) {
//     int answer = 1;

//     int pivot = section[0];
//     for(const auto v : section)
//     {
//         if(v < pivot + m)
//         {
//             continue;
//         }
//         else
//         {
//             pivot = v;
//             answer++;
//         }
//     }

//     return answer;
// }
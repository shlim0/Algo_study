// 87 min... 손으로 직접 풀자
// O(n^4) ㅋㅋ
#include <bits/stdc++.h>    

using namespace std;

vector<int> solution(vector<string> keymap, vector<string> t) {
    vector<int> a;
    
    for(int i=0; i<t.size(); i++)
    {
        int res = 0;
        for(int j=0; j<t[i].size(); j++)
        {
            int min = 100;
            for(int k=0; k<keymap.size(); k++)
            {
                for(int l=0; l<keymap[k].size(); l++)
                {
                    if(t[i][j] == keymap[k][l] && min > l+1)
                    {
                        min = ++l;
                        break;
                    }
                }
            }   
        if(min == 100){
            a.push_back(-1);
            // 찾을 수 없는 값인 경우 이전까지의 계산 무효화
            res = 0;
            break;
        }   
        else
            res += min;   
        }
        if(res)
            a.push_back(res);
    }
    
    return a;
}

// O(n^2)
// #include <string>
// #include <vector>

// using namespace std;

// vector<int> solution(vector<string> keymap, vector<string> targets) {
//     vector<int> answer;
//     vector<int> alpha(26, 999);

//     for(auto key : keymap){
//         for(int i=0;i<key.size();i++){
//             int N = key[i] - 'A';
//             alpha[N] = min(alpha[N], i + 1);
//         }
//     }

//     for(auto target : targets){
//         int count = 0;
//         for(int i=0;i<target.size();i++){
//             int N = target[i] - 'A';
//             if(alpha[N] == 999){
//                 count = -1;
//                 break;
//             }
//             count += alpha[N];
//         }
//         answer.push_back(count);
//     }

//     return answer;
// }
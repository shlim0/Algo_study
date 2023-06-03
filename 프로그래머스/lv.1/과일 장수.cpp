// 9 min
#include <bits/stdc++.h>

using namespace std;

int solution(int k, int m, vector<int> score) {
    int answer = 0;
    sort(score.begin(), score.end(), greater<int>());
    
    for(int i=m-1; i<score.size(); i += m)
    {
        if(i < score.size())
            answer += score[i] * m;
        else
            break;
    }
    
    
    return answer;
}
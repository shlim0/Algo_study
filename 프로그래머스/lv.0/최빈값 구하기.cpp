// 41 min
#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> array) {
    int answer = 0;
    vector<int> cnt(1000, 0);
    
    for(auto i : array)
        cnt[i]++;
    

    int overlap = 0;
    // int i=0이면 [0, 0, 0, 1, 2, 2] 같은 경우 -1이 출력됨.
    for(int i=1; i<=*max_element(array.begin(), array.end()); i++)
    {
        if(cnt[answer] < cnt[i]){
            answer = i;
            overlap = 0;
        }
        else if(cnt[answer] == cnt[i])
            overlap = 1;
    }
    
    if(overlap) //&& array.size() != 1)
        return -1;
    else
        return answer;
}
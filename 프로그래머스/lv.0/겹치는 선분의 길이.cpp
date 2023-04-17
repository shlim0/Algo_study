#include <bits/stdc++.h>

using namespace std;

int arr[200];

int solution(vector<vector<int> > lines) {
    int answer=0;
    
    for(int i=0; i<lines.size(); i++)
        for(int j=lines[i][0]; j<lines[i][1]; j++)
            arr[j+100]++;

    for(int i=0; i<200; i++)
        if(arr[i]>=2) answer++;
    
    return answer;
}
int main()
{
    vector<vector<int> > v(3, vector<int>(2, 0));

        v[0][0] = 0;
        v[0][1] = 1;
        v[1][0] = 2;
        v[1][1] = 5;
        v[2][0] = 3;
        v[2][1] = 9;
    solution(v);
    
}
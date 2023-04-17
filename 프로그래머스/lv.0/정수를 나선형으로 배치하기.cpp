#include <bits/stdc++.h>
using namespace std;
vector<vector<int> > solution(int n);

int main(void){
    solution(5);
}

vector<vector<int> > solution(int n) {
    vector<vector<int> > a(n, vector<int>(n, 0));
    // for(auto i: a){
    //     for(auto j : i)
    //         cout << j <<  " ";
    //     cout << '\n';
    // }
    
    
    // n : 1, 2, 3, ..., 30
    int cnt = 1;
    int first = 0, last = n-1;

    // n == 5일떄.
    // 1, 2, 3, 4
    for(int i=0; i<last; i++)
        a[0][i] = cnt++;
    
    while(cnt < n*n)
    {        
        // 5, 6, 7, 8
        // 19, 20
        if(a[first][last] == 0)
            for(int i=first; i<last; i++)
                a[i][last] = cnt++;
            
        // 9, 10, 11, 12
        // 21, 22
        if(a[last][last] == 0)
            for(int i=last; i>=first; i--)
                a[last][i] = cnt++;
        
        last--;
    
        // 13, 14, 15
        // 23
        if(a[last][first] == 0)
            for(int i=last; i>first+1; i--)
                a[i][first] = cnt++;
        
        // 16, 17, 18
        // 24
        if(a[first+1][first] == 0)
            for(int i=first; i<last; i++)
                a[first+1][i] = cnt++;
                
        first++;
    }
    
    // n이 짝수이고 값이 비어있는 경우
    if(n % 2 == 0 && a[n/2 - 1][n/2] == 0)
        a[n/2 - 1][n/2] = cnt;
    // 홀수이고 값이 비어있는 경우
    else if(a[n/2][n/2] == 0)
        a[n/2][n/2] = cnt;
    
    return a;
}
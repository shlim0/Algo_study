#include<bits/stdc++.h>
using namespace std;

int solution(vector<vector<int> > board) {
    int answer = 0;
    int n = board[0].size();
    
    vector<int> dx = {-1, -1, -1, 0, 1, 1, 1, 0};
    vector<int> dy = {-1, 0, 1, 1, 1, 0, -1, -1};
    vector<vector<int> > booms(n, vector<int>(n, 0));
    
    // 폭탄 위치 저장. 추후 for 돌때 1 사라질수 있으니.
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            if(board[i][j] == 1)
                booms[i][j] = 1;
        
    
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
        {
            // 폭탄이 있는 경우.
            if(booms[i][j])
            {
                for(int k=0; k<8; k++)
                {
                    // 경계면을 지나면 위험지역 제외.
                    if((0 <= i+dx[k] && i+dx[k] < n ) && (0 <= j + dy[k] && j + dy[k] < n))
                        // 또다른 폭탄이 없는 경우에만 위험지역 분류.
                        if(board[i + dx[k]][j + dy[k]] != 1)
                            board[i + dx[k]][j + dy[k]] = -1;
                }
            }
        }
    
    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            if(board[i][j] == 0)
                answer++;
    
    
    return answer;
}
//15 min
#include <bits/stdc++.h>

using namespace std;

string solution(string code) {
    string answer = "";
    int mode = 0;
    
    for(int i=0; i<code.length(); i++)
    {
        if((int)code[i] - '0' == 1){
            mode = mode == 0? 1: 0;
        }
        
        else if(mode == 0 && i % 2 == 0){
            cout << i << " ";
            answer += code[i];
        }
        else if(mode == 1 && i % 2 != 0){
            cout << i << " ";
            answer += code[i];
        }
    }
    
    if(answer == "")
        return "EMPTY";
    
    
    return answer;
}
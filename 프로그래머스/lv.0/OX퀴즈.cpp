#include <bits/stdc++.h>

using namespace std;

vector<string> solution(vector<string> quiz) {
    vector<string> answer;
    for(int i=0; i<quiz.size(); i++)
    {
        istringstream iss(quiz[i]);
        string token;
        int val = 0;
        
        while(iss >> token)
        {
            if(token == "+")
            {
                iss >> token;
                val += stoi(token);
            }
            else if(token == "-")
            {
                iss >> token;
                val -= stoi(token);
            }
            else if(token == "="){
                iss >> token;
                if(val == stoi(token))
                    answer.push_back("O");
                else
                    answer.push_back("X");
                break;
            }
            else
            {
                val = stoi(token);
            }
        }
    }
    
    return answer;
}

// 참고할만한 또 다른 코드
// https://school.programmers.co.kr/learn/courses/30/lessons/120907/solution_groups?language=cpp - 한창균

// bool test(const string& s)
// {
//     int a;
//     int b;
//     int c;
//     char op;
//     char eq;

//     stringstream ss;
//     ss.str(s);
//     ss>>a>>op>>b>>eq>>c;

//     if(op == '+')
//     {
//         return a + b == c;
//     }
//     else if(op == '-')
//     {
//         return a - b == c;
//     }
// }
// vector<string> solution(vector<string> quiz) {
//     vector<string> answer;

//     for(const auto v : quiz)
//     {
//         if(test(v))
//         {
//             answer.push_back("O");
//         }
//         else
//         {
//             answer.push_back("X");
//         }
//     }

//     return answer;
// }
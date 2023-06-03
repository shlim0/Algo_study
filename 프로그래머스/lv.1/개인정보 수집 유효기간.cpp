// getline() 다루는 것만 잘하면 될듯? < 30 min
// substr()로 입력받아도 됨

// i)today - 개인정보 수집 일자 구한 뒤, ii)term과 비교하기
// 단, today가 개인정보 수집 일자보다 미래임.
//      i) yyyy.mm.dd - yyyy.mm.dd 구한 뒤, dd로 변환 (한 달 28일임)
//      ii) mm -> dd로 변환
// iii) 계산값 >= term 이면 result에 추가

#include <bits/stdc++.h>
using namespace std;
typedef struct {
    string y;
    string m;
    string d;
}T;

vector<int> solution(string today, vector<string> terms, vector<string> p) {
    vector<int> answer;
    
    // today 입력
    stringstream ss(today);
    T t;
    getline(ss, t.y, '.');
    getline(ss, t.m, '.');
    getline(ss, t.d, '.');    
    
    // terms 입력
    map<string, int> m;
    for(auto v : terms)
    {
        stringstream terms(v);
        string tType, tPeriod;
        terms >> tType >> tPeriod;
        m[tType] = stoi(tPeriod);
    }
    
    // privacies 입력
    for(int i=0; i<p.size(); i++)
    {
        stringstream pp(p[i]);
        string token;
        int diff = 0;
        
        // yyyy
        getline(pp, token, '.');
        diff += (stoi(t.y) - stoi(token)) * 12 * 28;

        // mm
        getline(pp, token, '.');
        diff += (stoi(t.m) - stoi(token)) * 28;
        
        // dd
        // getline(pp, token, '.');
        pp >> token;
        diff += stoi(t.d) - stoi(token);
        
        // 약관 종류
        pp >> token;
        
        // 약관이 지난 경우
        if(diff / 28 >= m[token])
            answer.push_back(i+1);   
    }
    return answer;
}
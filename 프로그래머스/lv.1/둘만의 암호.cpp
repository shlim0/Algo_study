// 1 hour....
#include <bits/stdc++.h>

using namespace std;

string solution(string s, string skip, int index) {
    string answer = "";
    sort(skip.begin(), skip.end());
    
    for(auto v: s)
    {
        int i=0;
        for(int cnt=0; cnt<index; )
        {
            int flag = 0;
            for(auto sk : skip)
            {
                // 다음 문자열이 skip 대상 || 지금 문자열이 'z' 인데, 'a'가 skip 대상인 경우
                if(v+1 == sk || (v =='z' && 'a' == sk))
                {
                    flag = 1;
                    break;
                }
            }
            // skip 대상에 안걸리면
            if(!flag)
                cnt++;
            if(v == 'z')
                v = 'a';
            else
                v++;
        }
        answer += v;
    }
    
    return answer;
}

// 프로그램 시작(프로그램 호출) 하자마자 x, y가 할당된다.
int x,y;

// 함수가 호출되면, 호출되자마자 para, local_var가 할당된다.
// 즉, func()의 기계어 실행 중, 메모리 할당을 맨처음 한다.
int func(int p1)
{
    int a1, a2;
    {int a3;}
    {int a4;}
    a1 = 10;
    // return이 생략됐다.
}

int main(void)
{
    int s, t;
    {int x, y; func(0);}
}
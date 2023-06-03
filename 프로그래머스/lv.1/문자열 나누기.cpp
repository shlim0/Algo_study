#include <bits/stdc++.h>

using namespace std;

int solution(string s) {
    int res = 0, cmp = 0, cnt = 0;
    
    // 초기 비교값 설정
    char cmp_index = s[0];
    cmp = 1;
    
    for(int i=1; i<s.size(); i++)
    {
        // 다른 글자면서 글자수가 같은 경우
        if(cmp == cnt + 1 && cmp_index != s[i])
        {
            cmp = 0;
            cmp_index = s[i+1];
            cnt = 0;
            res++;
        }
        else if(cmp_index == s[i])
            cmp++;
        else if(cmp_index != s[i])
            cnt++;
    }
    if(cmp)
        res++;
    
    return res;
}


// b :  pos : 0
//      cmp : 1, 이 때 index 'b'

// a :  pos : 1
//      cnt : 1 == cmp 이므로, pos : 2가 cmp가 됨. cnt = 0.res++

// n :  pos : 2
//      cmp : 1, 이 때 index 'n'

// a :  pos : 3
//      cnt : 1 == cmp 이므로, pos : 4가 cmp가 됨. cnt = 0. res++

// n :  pos : 4
//      cmp : 1, 이 때 index 'n'

// a :  pos : 5
//      cnt : 1 == cmp 이므로, pos : 6이 cmp가 됨. cnt = 0. res++

// 두번째 테스트 케이스일때, cmp != 0이면 res++; (남는 친구는 cmp >= 1일 테니)

// 세번째 테스트 케이스일때, 

// a :  pos : 0
//      cmp : 1, 이때 index 'a'

// a :  pos : 1
//      cmp : 2

// a :  pos : 2
//      cmp : 3

// b :  pos : 3
//      cnt : 1

// b :  pos : 4
//      cnt : 2

// a :  pos : 5
//      cmp : 4

// c :  pos : 6
//      cnt : 3

// c :  pos : 7
//      cnt : 4 == cmp 이므로, pos : 8이 cmp가 됨. cnt = 0. res++

// c :  pos : 8
//      cmp : 1, 이 때 index 'c'

// c :  pos : 9
//      cmp : 2

// a :  pos : 10
//      cnt : 1

// b :  pos : 11
//      cnt : 2 == cmp 이므로, pos : 12가 cmp가 됨. cnt = 0. res++

// b :  pos : 12
//      cmp : 1, 이 때 index 'b'

// a :  pos : 13
//      cnt : 1 == cmp, pos : 13이 cmp가 됨. cnt = 0. res++


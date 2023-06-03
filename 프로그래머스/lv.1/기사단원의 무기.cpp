// 방법 i만 이해한듯
#include <string>
#include <vector>
using namespace std;

int solution(int number, int limit, int power) {
    int answer = 0;
    
    for(int i=1; i<=number; i++)
    {
        int cnt = 0;
        for(int j=1; j<=sqrt(i); j++)
        {
            if(i % j == 0){
                cnt++;
                if(j < sqrt(i))
                    cnt++;
            }
        }
        if(cnt <= limit) answer += cnt;
        else answer += power;   
    }
    return answer;
}

// 소인수분해
// 1 : x
// 2 : 2
// 3 : 3
// 4 : 2^2 -> 1 2 4
// 5 : 5
// 6 : 2*3 -> 1 2 3 6
// 7 : 7
// 8 : 2^3


// 다른 사람의 코드
int solution(int number, int limit, int power) {
    int answer = 0;

    vector<int> vk;
    for(int i = 1, cnt = 0; i<=number ; i++){
        cnt = 0;
        // 방법 i
        // for(int j = 1; j*j <= i ; j++){
        //     if(i%j == 0){
        //         cnt++;
        //         if(j*j < i)
        //             cnt++;                
        //     }
        // }        
        // vk.push_back(cnt);
        
        // 방법 ii
        // vector<int> vk(number+1);
        // for (int j = 1; j <= number / i; j++) { 
        //     vk[i * j]++;
        // }
    }

    for(int i = 1; i < vk.size(); i++)
        vk[i] <= limit ? answer += vk[i] : answer += power;    

    return answer;
}

// int main(void)
// {
//     solution(10, 3, 2);
// }

// https://school.programmers.co.kr/questions/46916
// 제곱근 : https://kbw1101.tistory.com/32
// 소인수분해 : https://mathbang.net/201
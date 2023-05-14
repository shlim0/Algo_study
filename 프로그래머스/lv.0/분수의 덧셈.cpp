// 19 min
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    
    // denom1 == denom2인 경우를 위해 값을 대입
    int denom = denom1;
    
    if (denom1 != denom2)
    {
        denom = denom1 * denom2;
        numer1 *= denom2;
        numer2 *= denom1;
    }
    
    int numer = numer1 + numer2;
   
    
    for(int i=2; i<1000; i++)
        if(numer % i == 0 && denom % i == 0)
        {
            numer /= i;
            denom /= i;
            // i.e. 20/16일 때, 10/8 된 후 약분이 안되는 경우 방지.
            i--;
        }
    
    answer.push_back(numer);
    answer.push_back(denom);
    
    return answer;
}
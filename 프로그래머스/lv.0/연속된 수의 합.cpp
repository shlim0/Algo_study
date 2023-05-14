// 12min
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int num, int total) {
    vector<int> answer;
    
    for(int i=-1000; i<1000; i++)
    {
        int val = 0;
        for(int j=i; j<i+num; j++)
            val += j;
            
        if(val == total)
            for(int j=i; j<i+num; j++)
                answer.push_back(j);
    }
    
    return answer;
}
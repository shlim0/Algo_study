// 16 min
#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> w) {
    
    // 반대 지점에서 부터 영역을 확장해 나감
    pair<int, int> s = {w.size(), w[0].size()};
    pair<int, int> e = {0, 0};
    
    for(int i=0; i<w.size(); i++)
    {
        for(int j=0; j<w[i].size(); j++)
        {
            if(w[i][j] == '#')
            {
                if(s.first > i)
                    s.first = i;
                if(s.second > j)
                    s.second = j;
                if(e.first <= i)
                    e.first = i + 1;
                if(e.second <= j)
                    e.second = j + 1;
            }
            // printf("%d, %d, %d, %d\n", s.first, s.second, e.first, e.second);
        }   
    }
    
    return {s.first, s.second, e.first, e.second};
}
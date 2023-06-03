// 22 min
// string.push_back()이 아닌 string += value;
// j < food[i] / 2.
#include <bits/stdc++.h>

using namespace std;

string solution(vector<int> food) {
    string a, r;
    
    for(int i=1; i<food.size(); i++)
    {
        for(int j=0; j<food[i]/2; j++)
        {
            if(food[i] % 2 != 0)
                --food[i];
            a += to_string(i);
        }
    }
    r = a;
    reverse(r.begin(), r.end());
    a += to_string(0);
    a += r;
    
    return a;
}
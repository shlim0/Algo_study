#include <bits/stdc++.h>

using namespace std;

string solution(string polynomial) {
    string ans = "";
    string token = "";
    stringstream ss(polynomial);
    
    int x = 0;
    int c = 0;
    while(ss >> token)
    {
        if(token.find('x') != string::npos)
        {
            if(token.size() != 1)
            {
                token.erase(token.find('x'));
                x += stoi(token);
            }
            // core dumped 피하려면...
            else x++;
        }
       else if(token != "+")
            c += stoi(token);
       
     }  
//     x > 1  && c > 0
        
//     x > 1 && c == 0
        
//     x == 1 && c > 0
    
//     x == 1 && c == 0
        
//     x == 0 && c > 0
    
//     x == 0 && c == 0
    
    // -> c > 0, x > 1
    //           x == 1
    //           x == 0
    //     c ==0, x > 1
    //            x == 1
    //            x == 0
    
    if(c > 0)
    {
        if(x > 1)
            ans = to_string(x) + "x + " + to_string(c);
        else if (x == 1)
            ans = "x + " + to_string(c);
        else if (x == 0)
            ans = to_string(c);
    }
    else if (c == 0)
    {
        if(x > 1)
            ans = to_string(x) + "x";
        else if (x == 1)
            ans = "x";
        else if (x == 0)
            ;
    }
        
    return ans;
}
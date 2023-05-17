#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> p, vector<string> r) {
    vector<int> a;
    pair<int, int> pos;
    pair<int, int> move[4] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    map<string, pair<int, int>> m = {{"E", move[0]}, {"W", move[1]}, {"S", move[2]}, {"N", move[3]}};
    

    // 시작 지점 입력
    for(int i=0; i<p.size(); i++)
        for (int j=0; j<p[i].size(); j++)
            if(p[i][j] == 'S')
                pos = {i, j};
    // cout << s.first << " " << s.second;
    
    for(auto v : r)
    {
        stringstream ss(v);
        string token;
        while(ss >> token)
        {
            // E W S N
            string direction = token;
            ss >> token;
            // 얼마만큼 이동할 것인지
            pair<int, int> tmp_pos = pos;
            int flag = 0;
            
            for(int i=0; i< stoi(token); i++)
            {
                // 경계선 넘지 않도록 index 조절
                if(p[i].size() > tmp_pos.first + m[direction].first && tmp_pos.first + m[direction].first >= 0 
                   && p[i].size() > tmp_pos.second + m[direction].second && tmp_pos.second + m[direction].second >= 0
                   // 이동하다가 시작지점 ('S')으로 다시 돌아올 수도 있는 걸 염두해야 함
                   && p[tmp_pos.first + m[direction].first][tmp_pos.second + m[direction].second] != 'X')
                    {
                        tmp_pos.first += m[direction].first;
                        tmp_pos.second += m[direction].second;
                        cout << tmp_pos.first << " " << tmp_pos.second << '\n';
                    }
                    // 갈 수 없는 지역인 경우 현재까지의 명령 취소
                    else
                    {
                        flag = 1;
                        break;
                    }
            }
            if(!flag)
                pos = tmp_pos;
            
            // cout << pos.first << " " << pos.second << '\n';
        }   
    }
    a.push_back(pos.first);
    a.push_back(pos.second);
    
    return a;
}

// 다른 사람의 풀이
// #include <bits/stdc++.h>
// using namespace std;
// using pi = pair<int, int>;

// int dx[4] = {0, 0, 1, -1};
// int dy[4] = {1, -1, 0, 0};
// map<char, int> mapping = {
//     {'E', 0}, {'W', 1}, {'S', 2}, {'N', 3}
// };

// vector<int> solution(vector<string> park, vector<string> routes) {
//     int cx, cy;
//     for (int i = 0; i < park.size(); ++i) {
//         for (int j = 0; j < park[i].size(); ++j) {
//             if (park[i][j] == 'S') {
//                 tie(cx, cy) = {i, j};
//                 break;
//             }
//         }
//     }

//     for (int i = 0; i < routes.size(); ++i) {
//         int num = routes[i][2] - '0';
//         int dir = mapping[routes[i][0]];

//         int nx = cx, ny = cy;
//         while (num--) {
//             nx += dx[dir];
//             ny += dy[dir];

//             if (!(nx >= 0 && nx < park.size()) || !(ny >= 0 && ny < park[0].size())) break;
//             if (park[nx][ny] == 'X') break;
//         }

//         if (num < 0) {
//             cx = nx;
//             cy = ny;
//         }
//     }
//     return {cx, cy};
// }
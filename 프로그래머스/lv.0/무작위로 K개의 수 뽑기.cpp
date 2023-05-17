#include <string>
#include <vector>

// 33 min
// 중복 제거가 핵심
using namespace std;

vector<int> solution(vector<int> arr, int k) {
    vector<int> answer;
    vector<int> cnt(100000,0);
    
    for(int i=0; i<arr.size(); i++)
    {
        // 처음 들어온 값이면
        if(cnt[arr[i]] == 0)
        {
            cnt[arr[i]]++;
        }
        // 이미 들어온 값이면 중복 제거
        else
        {
            arr.erase(arr.begin() + i);
            i--;
        }
    }
    
    if(arr.size() < k)
        for(int i=arr.size(); i<k; i++)
            arr.push_back(-1);
    else
        arr.erase(arr.begin() + k, arr.end());
        
    return arr;
}

// map을 이용한 풀이
// vector<int> solution(vector<int> arr, int k) {
//     vector<int> answer;
//     unordered_map<int, int> counter;

//     for (const auto& i : arr)
//     {
//         if (counter[i]++ == 0)
//             answer.push_back(i);
//     }
//     answer.resize(k, -1);
//     return answer;
// 


// set을 이용한 풀이
// vector<int> solution(vector<int> arr, int k) {
//     vector<int> answer;

//     set<int> table;
//     for(const auto v : arr)
//     {
//         if(table.size() < k && !table.count(v))
//         {
//             answer.emplace_back(v);
//             table.insert(v);
//         }        
//     }
//     for(int t = table.size(); t < k; ++t)
//     {
//         answer.emplace_back(-1);
//     }
//     return answer;
// }
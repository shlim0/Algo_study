#include <string>
#include <vector>

using namespace std;

// for index 직접 접근하면 잘 되고
// for auto 하면 seg fault... 
vector<int> solution(vector<int> arr, vector<int> query) {    
    // for (int i = 0; i < query.size(); i++) {
    for(auto i : query){
        if (i % 2) {
            arr.erase(arr.begin(), arr.begin() + i);
            // arr.erase(arr.begin(), arr.begin() + query[i]);
        } else {
            arr.erase(arr.begin() + i + 1, arr.end());
            // arr.erase(arr.begin() + query[i] + 1, arr.end());
        }
    }
    return arr;
}
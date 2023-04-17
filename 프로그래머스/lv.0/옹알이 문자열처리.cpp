#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<string> babbling) {

    vector<string> test_case = {"aya", "ye", "woo", "ma"};
    int answer = 0;

    for(string input : babbling){
        string to_compare = "";
        for(int i=0; i < input.length(); i++){
            // 한 글자씩 추가해 나가며 비교한다.
            to_compare += input[i];
            for(string test_case : test_case){
                // 존재하는 단어면 비교할 필요 없으니 비운다.
                if(to_compare == test_case)
                    to_compare = "";
            }
        }
        // 존재하지 않는 단어면 공백이 아니다.
        if (to_compare == "")
            answer++;
    }
}
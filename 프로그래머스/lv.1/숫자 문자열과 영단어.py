# 15 min
from collections import defaultdict

dic = defaultdict(int)
dic = {"zero": 0,
       "one": 1,
       "two": 2,
       "three": 3,
       "four": 4,
       "five": 5,
       "six": 6,
       "seven": 7,
       "eight": 8,
       "nine": 9}

def solution(s):
    tmp = ""
    ans = ""

    for si in range(len(s)):
        if s[si] in [str(i) for i in range(10)]:
            ans += s[si]
            continue

        tmp += s[si]
        for d in dic:
            if tmp == d:
                print(tmp)
                ans += str(dic[d])
                tmp = ""

    return int(ans)

solution("one4seveneight")
import sys
from collections import defaultdict
input = sys.stdin.readline

cnt = 0

for _ in range(int(input())):
    word = input().rstrip()
    words = defaultdict(str)

    for char in range(len(word)):
        # 맨 처음 들어오는 문자
        if words[word[char]] == "":
            words[word[char]] = True
        # 이미 들어온 문자가 연속되어 들어온 경우
        elif word[char] == word[char - 1] and words[word[char]] == True:
            continue
        # 맨 처음 들어오지도 않고 연속되지도 않으면 False
        else:
            words[word[char]] = False

    # False가 없는 경우 그룹 단어 카운트
    if not False in words.values():
        cnt += 1

print(cnt)
# 11퍼 실패 후 코드 리셋 후 구글링.
# 1. 각 나라별로 서로 한번씩은 맞붙음
    # a: b, c, d, e, f
    # b: c, d, e, f
    # c: d, e, f
    # d: e, f
    # e: f
    # 총 15가지 경우
# 2. 그리고 그 맞붙는 경우는 이기거나, 비기거나, 지거나.
# 3. 2번을 나라별로 반복. 단, 앞선 경기결과는 뒤에 영향을 미침.

import sys
from itertools import combinations

ans = []
input = sys.stdin.readline
games = list(combinations(range(6), 2))

def backtrack(k):
    global arr, cnt
    if k == 15:
        for country in arr:
            if not country.count(0) == 3:
                cnt = 0
                return
        cnt = 1
        return

    c1, c2 = games[k]

    for r1, r2 in ((0,2), (1,1), (2,0)):
        if arr[c1][r1] > 0 and arr[c2][r2] > 0:
            arr[c1][r1] -= 1
            arr[c2][r2] -= 1
            backtrack(k+1)
            arr[c1][r1] += 1
            arr[c2][r2] += 1

for _ in range(4):
    cnt = 0
    tmp = list(map(int, input().split()))
    arr = [tmp[i:i+3] for i in range(0, 16, 3)]
    backtrack(0)
    ans.append(cnt)

print(*ans)
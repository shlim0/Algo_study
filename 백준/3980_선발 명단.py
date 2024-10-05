# 14 min 12퍼
# 51 min 29번라인 해결...

# 포지션 갈이
# 능력치: 0~100
    # 0이면 배치 불가!

import sys
input = sys.stdin.readline

def backtrack(k, is_used, positions): # k: 포지션
    global players, mx

    if k == 11:
        if positions.count(0) == 0:
            mx = max(sum(positions), mx)
        return

    for player in range(11):
        if not is_used[player]:
            is_used[player] = 1
            ability = players[player][k]

            if not ability == 0:
                positions[k] = ability
                backtrack(k+1, is_used, positions)
                positions[k] = 0

            is_used[player] = 0 # 능력치가 0일 때에도 해당 선수를 사용하지 않도록 해야함.

TC = int(input())
ans = []
for _ in range(TC):
    mx = 0
    players = [[] for _ in range(11)]
    is_used = [0 for _ in range(11)]
    positions = [0 for _ in range(11)]

    for i in range(11):
        players[i] = list(map(int, input().split()))

    backtrack(0, is_used, positions)
    if mx != 0:
        ans.append(mx)

for tc in ans:
    print(tc)

# for test
# for i in range(11):
#     for j in range(11):
#         if i == j:
#             print(10, end=" ")
#         else:
#             print(0, end=" ")
#     print()

# 1
# 10 0 0 0 0 0 0 0 0 0 0
# 0 10 0 0 0 0 0 0 0 0 0
# 0 0 10 0 0 0 0 0 0 0 0
# 0 0 0 10 0 0 0 0 0 0 0
# 0 0 0 0 10 0 0 0 0 0 0
# 0 0 0 0 0 10 0 0 0 0 0
# 0 0 0 0 0 0 10 0 0 0 0
# 0 0 0 0 0 0 0 10 0 0 0
# 0 0 0 0 0 0 0 0 10 0 0
# 0 0 0 0 0 0 0 0 0 10 10
# 0 0 0 0 0 0 0 0 0 30 2
# 20 min backtracking 시간초과
# import copy
# n = int(input())
# mn = float('inf')
# mn_history = []

# RecursionError: maximum recursion depth exceeded while calling a Python object
# def backtrack(now, cnt, history):
#     global n, mn, mn_history
#
#     history.append(now)
#
#     if now == n and cnt < mn:
#         mn_history = copy.deepcopy(history)
#         mn = cnt
#         return
#
#     if now * 3 <= n:
#         backtrack(now * 3, cnt + 1, history)
#     elif now * 2 <= n:
#         backtrack(now * 2, cnt + 1, history)
#     elif now + 1 <= n:
#         backtrack(now + 1, cnt + 1, history)
#     else:
#         return
#
# backtrack(1, 0, [])
#
# mn_history.reverse()
# print(len(mn_history) - 1)
# print(*mn_history)

# BFS 14퍼 시간초과
# import sys
# from collections import deque
# queue = deque()
# n = int(sys.stdin.readline())
# # start, path
# queue.append([n])
#
# while queue:
#     path = queue.popleft()
#     n = path[0]
#     if n == 1:
#         print(len(path) - 1)
#         print(*path[::-1])
#         break
#
#     if n % 3 == 0:
#         queue.append([n//3] + path)
#     if n % 2 == 0:
#         queue.append([n//2] + path)
#
#     queue.append([n-1] + path)

# DP - bottom up
# https://blog.encrypted.gg/974
import sys
input = sys.stdin.readline
n = int(input())
dp = [float('inf') for _ in range(1000001)]
pre = [0 for _ in range(1000001)]
dp[1] = 0

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1
    pre[i] = i-1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i // 3] + 1
        pre[i] = i//3
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        pre[i] = i//2

print(dp[n])
while n > 0:
    print(n, end=" ")
    n = pre[n]
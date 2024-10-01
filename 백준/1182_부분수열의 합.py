# # < 40min 시간 초과
# N, S = list(map(int, input().split()))
# arr = list(map(int, input().split()))
# is_used = [0 for _ in range(N)]
# is_sumd = []
# is_visited = []
# cnt = 0
# sum = 0
#
# def backtrack(k):
#     global cnt, sum
#     if k == N:
#         is_sumd.append(sum)
#
#     if sum == S and 1 in is_used:
#         cnt += 1
#         is_sumd.append(sum)
#         is_visited.append(is_used)
#         return
#
#     for i in range(N):
#         if is_used[i] == 0:
#             is_used[i] = 1
#             sum += arr[i]
#             if is_used not in is_visited and sum not in is_sumd:
#                 backtrack(k+1)
#             is_used[i] = 0
#             sum -= arr[i]
#
#
# backtrack(1)
# print(cnt)

# https://blog.encrypted.gg/945
sum = 0
def backtrack(k, sum):
    global cnt
    if k == N:
        if sum == S:
            cnt += 1
        return

    backtrack(k+1, sum)
    backtrack(k+1, sum + arr[k])

N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))
cnt = 0
backtrack(0, 0)
if S == 0:
    cnt -= 1
print(cnt)
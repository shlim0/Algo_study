# 8 min
def backtrack(k):
    if k == M:
        print(*arr)
        return

    for i in range(N):
        if not is_used[i]:
            is_used[i] = 1
            arr[k] = i + 1
            backtrack(k+1)
            is_used[i] = 0

N, M = list(map(int, input().split()))
arr = [0 for _ in range(M)]
is_used = [0 for _ in range(N)]
backtrack(0)
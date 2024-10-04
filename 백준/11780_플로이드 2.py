# 11404_플로이드에 경로 구하는 문제
# 20 + 20 min 인듯
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
nxt = [[0 for _ in range(n+1)] for _ in range(n+1)]

# initialize
for _ in range(m):
    # start, end, cost
    s, e, c = list(map(int, input().split()))
    if arr[s][e] > c:
        arr[s][e] = c
        nxt[s][e] = e
        # 도착점에서도 갱신해야함!
        nxt[e][s] = s

# calculate
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # print(i, k, j)
            if i == j:
                continue

            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                # 다음 위치만 대입하면 됨
                nxt[i][j] = nxt[i][k]

for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] == float('inf'):
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()

for i in range(1, n+1):
    for j in range(1, n+1):
        if nxt[i][j] == 0:
            print(0)
            continue

        path = str(i) + " "
        cnt = 1
        s1, s2 = i, nxt[i][j]
        while s2:
            cnt += 1
            s1, s2 = s2, nxt[s2][j]
            path += str(s1) + " "
        print(cnt, path)

# 0, 1 -> 0, 2 -> 0, 3 -> 0, 4
# 0, 1, 1 -> 0, 1, 2 -> 0, 1, 3 -> 0, 1, 4
#
# 1, 2 -> 2, 3 -> 3, 4
# 1, 0, 2 -> 2, 0, 3 -> 3, 0, 4
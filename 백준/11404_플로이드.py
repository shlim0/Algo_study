# 20 min
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

# initialize
for _ in range(m):
    # start, end, cost
    s, e, c = list(map(int, input().split()))
    arr[s][e] = min(arr[s][e], c)

# calculate
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # print(i, k, j)
            if i == j:
                continue

            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if arr[i][j] == float('inf'):
            print(0, end=" ")
        else:
            print(arr[i][j], end=" ")
    print()

# 0, 1 -> 0, 2 -> 0, 3 -> 0, 4
# 0, 1, 1 -> 0, 1, 2 -> 0, 1, 3 -> 0, 1, 4
#
# 1, 2 -> 2, 3 -> 3, 4
# 1, 0, 2 -> 2, 0, 3 -> 3, 0, 4
# 21 min
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

cnt, mx_size = 0, 0

queue, isVisited = set(), set()
def BFS():
    global queue, mx_size
    size = 0

    while queue:
        r, c = queue.pop()
        isVisited.add((r, c))
        size += 1

        for i in range(4):
            ndr = r + dr[i]
            ndc = c + dc[i]

            if 0 <= ndr < n and 0 <= ndc < m and arr[ndr][ndc] == 1 and (ndr, ndc) not in isVisited:
                queue.add((ndr, ndc))

    if size > mx_size:
        mx_size = size

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and (i, j) not in isVisited:
            cnt += 1
            queue.add((i, j))
            BFS()

print(cnt)
print(mx_size)
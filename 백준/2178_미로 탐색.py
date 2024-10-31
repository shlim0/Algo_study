# 30 min 시간초과: BFS 재귀로 백트래킹 했음 -> while loop
# 60 min sol with GPT: visited를 deque()나 set()로 했을 때, if에서 O(n)
    # -> 2D arr로 O(1)로 접근

from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

mn = float('inf')
Q = deque([(0, 0, 1)])
visited = [[False] * M for _ in range(N)]
visited[0][0] = True

while Q:
    r, c, cnt = Q.popleft()

    if r == N - 1 and c == M - 1:
        mn = cnt
        break

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            Q.append((nr, nc, cnt + 1))

print(mn)

import sys
from collections import deque
input = sys.stdin.readline

# <>v^
# dr = [0, 0, 1, -1]
# dc = [-1, 1, 0, 0]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

M, N = map(int, input().split())

tomatoes = [list(map(int, input().split())) for _ in range(N)]

visited = set()
Q = deque()
tomatoes_cnt = 0

for i in range(N):
    for j in range(M):
        # 1: 익음 0: 안익음 -1: 빈칸
        if tomatoes[i][j] == 1:
            Q.append((i, j, 0))
            visited.add((i, j))
            tomatoes_cnt += 1
        elif tomatoes[i][j] == 0:
            tomatoes_cnt += 1

while Q:
    r, c, cnt = Q.popleft()
    # visited.add((r, c))       # 불필요한 중복으로 인한 시간 초과
    print(r, c)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and (nr, nc) not in visited and tomatoes[nr][nc] == 0:
            Q.append((nr, nc, cnt+1))
            visited.add((nr, nc))

if tomatoes_cnt == len(visited):
    print(cnt)
else:
    print(-1)
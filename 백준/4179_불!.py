# 1h 30m
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

R, C = list(map(int, input().split()))
arr = [[v for v in input().strip()] for _ in range(R)]
Q1, Q2 = deque(), deque()
v1, v2 = defaultdict(int), defaultdict(int)

def BFS2(Q, visited):
    global R, C
    while Q:
        r, c, t = Q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0<=nr<R and 0<=nc<C:
                if (arr[nr][nc] == "." or arr[nr][nc] == "J") and visited[(nr, nc)] == 0:
                    visited[(nr, nc)] = t+1
                    Q.append((nr, nc, t+1))
            # 맵 바깥으로 나간다고 해서 시간에 따라 불이 난 모든 위치를 기록하고 종료되는게 아님!
            # 따라서 필요없는 코드임.
            # else:
            #     visited[(nr, nc)] = t+1
            #     return

def BFS1(Q, v1, v2):
    global R, C
    while Q:
        r, c, t = Q.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0<=nr<R and 0<=nc<C:
		            # 파랑색 밑줄: 불이 없거나, 불이 있어도, 사람이 이동해도 불이 아직 옮겨 붙지 않은 상황
                if arr[nr][nc] == "." and v1[(nr, nc)] == 0 and (v2[(nr, nc)] == 0 or t+1 < v2[(nr, nc)]):
                    v1[(nr, nc)] = t+1
                    Q.append((nr, nc, t+1))
            else:
                return t+1
    return -1

for r in range(R):
    for c in range(C):
        if arr[r][c] == "J":
            v1[(r,c)] = -1
            Q1.append((r, c, 0))
        elif arr[r][c] == "F":
            v2[(r,c)] = -1
            Q2.append((r, c, 0))

BFS2(Q2, v2)
t = BFS1(Q1, v1, v2)

if t != -1:
    print(t)
else:
    print("IMPOSSIBLE")

# 4 4
# ####
# #JF#
# #..#
# ####
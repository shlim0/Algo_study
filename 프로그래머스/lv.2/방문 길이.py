# Strategy
# 1. 경로 기록
# 1-1. Record from (x1, y1) to (x2, y2)
# -> 이렇게 해도 되지만... 귀찮아 질거 같아서 (x, y)에서 UDRL 횟수 카운트 하면 되지 않을까
# ex. dictionary[(x, y)] = (U, D, R, L)
# 1-2. And path += 1
# 2. index out of range

# Result
# 23 min: sample tc sol
# 39 min: sol
# The reason: To consider bidirectional checking.
# 추가로, 문제에서 UDRL 순으로 알려주기 때문에 이 순서에 맞춰 if-else 처리했는데,
# 그러면 모듈러 연산(%4)시 규칙성이 없어서 URDL로 순서를 바꿈
from collections import defaultdict

U = (0, 1)
D = (0, -1)
R = (1, 0)
L = (-1, 0)

def solution(dirs):
    ans = 0
    now = (0, 0)
    path = defaultdict()
    # U  R  D  L
    path[(0, 0)] = [0, 0, 0, 0]  # started from (0, 0)
    visited = set()
    visited.add((0, 0))

    for dir in dirs:
        i = -1
        if dir == "U":
            to = (now[0] + U[0], now[1] + U[1])
            i = 0
        elif dir == "R":
            to = (now[0] + R[0], now[1] + R[1])
            i = 1
        elif dir == "D":
            to = (now[0] + D[0], now[1] + D[1])
            i = 2
        elif dir == "L":
            to = (now[0] + L[0], now[1] + L[1])
            i = 3

        if -5 <= to[0] <= 5 and -5 <= to[1] <= 5:  # 맵 바깥이 아니면
            if to not in visited:  # 처음 방문한 좌표
                visited.add(to)
                path[to] = [0, 0, 0, 0]

            if path[now][i] == 0:  # 안간 경로면 기록
                path[now][i] = 1
                path[to][(i + 2) % 4] = 1
                ans += 1

            now = to

    return ans

# 다른 사람의 풀이
# def solution(dirs):
#     s = set()
#     d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
#     x, y = 0, 0
#     for i in dirs:
#         nx, ny = x + d[i][0], y + d[i][1]
#         if -5 <= nx <= 5 and -5 <= ny <= 5:
#             s.add((x,y,nx,ny))
#             s.add((nx,ny,x,y))
#             x, y = nx, ny
#     return len(s)//2
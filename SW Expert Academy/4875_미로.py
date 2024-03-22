from collections import deque

# v / < / ^ / >
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

for tc in range(1, int(input()) + 1):
    n = int(input())
    miro = [[-1] * n for _ in range(n)]
    miro_str = [input().rstrip() for _ in range(n)]

    print(miro_str)

    for i in range(n):
        for j in range(n):
            if miro_str[i][j] == "2":
                start, end = i, j
            miro[i][j] = int(miro_str[i][j])

    stack = deque()
    stack.append([start, end])

    arrived = 0
    while stack:
        r, c = stack.pop()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < n and 0 <= nc < n:
                if miro[nr][nc] == 0:
                    stack.append([nr, nc])
                    miro[nr][nc] = 1
                elif miro[nr][nc] == 3:
                    print(f'#{tc} 1')
                    arrived = 1
                    break

    if arrived == 0:
        print(f'#{tc} 0')
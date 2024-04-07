from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "R":
            Rr, Rc = i, j
        elif arr[i][j] == "B":
            Br, Bc = i, j

# < / ^ / > / v
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

Q = deque()
Q.append((Rr, Rc, Br, Bc, 1)) # 마지막은 cnt. 10회 이하 탐색 제한
visited = []
visited.append((Rr, Rc, Br, Bc))

# 한 쪽 방향으로만 쭉 이동하다가 더 갈 수 없으면 멈추게 됨
def move(r, c, dr, dc):
    cnt = 0
    while arr[r+dr][c+dc] != "#" and arr[r][c] != "O":
        r += dr
        c += dc
        cnt += 1
    return r, c, cnt

while Q:
    Rr, Rc, Br, Bc, cnt = Q.popleft()

    if cnt > 10:
        print(-1)
        exit()

    for i in range(4):
        Rnr, Rnc, Rcnt = move(Rr, Rc, dr[i], dc[i])
        Bnr, Bnc, Bcnt = move(Br, Bc, dr[i], dc[i])

        R, B = arr[Rnr][Rnc], arr[Bnr][Bnc]

        # 파란공이 먼저 나가면 해당 방법으로 굴리는 걸 찾을 필요 없으니 패스
        if B == "O":
            continue

        if R == "O":
            print(cnt)
            exit()
        # 같은 지점에 있을 때, 더 멀리서 온 애가 뒤로 가게

        if Rnr == Bnr and Rnc == Bnc:
            # Rnr, Bnr 헷갈리지 말기
            if Rcnt > Bcnt:
                Rnr -= dr[i]
                Rnc -= dc[i]
            else:
                Bnr -= dr[i]
                Bnc -= dc[i]

        # 방문 처리
        if (Rnr, Rnc, Bnr, Bnc) not in visited:
            Q.append((Rnr, Rnc, Bnr, Bnc, cnt+1))
            visited.append((Rnr, Rnc, Bnr, Bnc))

print(-1)
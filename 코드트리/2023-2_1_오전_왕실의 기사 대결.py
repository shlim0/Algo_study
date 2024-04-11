# https://www.youtube.com/watch?v=eDTV0VMDqFs&ab_channel=%EB%AC%B8%EC%96%B4%EB%B0%95%EC%82%ACIT%ED%8E%B8%EC%9D%98%EC%A0%90
# https://www.codetree.ai/training-field/frequent-problems/problems/royal-knight-duel/description?page=1&pageSize=20

# 1h 52min

# 체스판 밖 == 벽 == 2
# (r, c, h, w, k)

# 어느 기사라도 (밀든, 밀리는 입장이든 간에) 벽에 부딪히면 -> 무효
    # 함수로 빼서 return 하는 방향

# 미는 애는 데미지 무조건 안입음
# 밀린 애는 함정 밟으면 데미지 += 1

from collections import defaultdict

# 상 우 하 좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

N, M, Q = map(int, input().split())
chess = [[2] * (N+2) for _ in range(N+2)]

# 체스판 밖도 벽이니 2로 패딩을 씌움
for i in range(1, N+1):
    chess[i][1:N+1] = map(int, input().split())     # 0: 빈칸, 1: 함정, 2: 벽

units = defaultdict(int)

for i in range(1, M+1):
    units[i] = list(map(int, input().split()))      # (r, c, h, w, k)   # row, col, height, width, 체력

init_k = [0] * (M+1)                                # 초기 체력 비교

for i in range(1, M+1):
    init_k[i] = units[i][4]

order = [0 for _ in range(Q+1)]
for idx in range(1, Q+1):
    knight, dr = map(int, input().split())
    order[idx] = knight, dr

damage = [0] * (M+1)

# 입력 끝---------------

# 하달받은 명령 진행
def move(start, dr):
    q = [start]
    q_set = set()
    tmp_damage = [0] * (M+1)

    while q:
        idx = q.pop(0)
        if not idx in q_set:  q_set.add(idx)            # 처음 이동하는 애라면 방문 처리
        else:   continue                                # 이미 이동한 애면 패스

        # 미는 기준은?

        # 1. 기사의 체력이 남아있는 경우. 즉, 살아있는 경우 (O)
        # 2. 단, 이동할 위치에 벽이 있다면 "무효"
        # 3. 함정있으면 체력 -= 1

        if units[idx][4] <= 0:     continue             # 뒤진 기사는 명령 실행 못함
        # 다만, return이 아닌 continue인 이유는, 하나의 기사가 뒤진 기사를 포함한 2명 이상의 기사를 밀 수도 있으니까.

        ni, nj, th, tw, k = units[idx]                  # now row, now col, ...

        ti, tj = ni + di[dr], nj + dj[dr]               # 이동할 위치

        for i in range(ti, ti+th):                      # 이동할 위치에 함정이나 벽이 있는지 확인
            for j in range(tj, tj+tw):
                if chess[i][j] == 2:                    # 벽이면 이동 안하고 탈출
                    return
                if chess[i][j] == 1 and idx != start:   # 밀린 애만 데미지가 누적됨
                    tmp_damage[idx] += 1                # 데미지 누적해주기

        # 겹치는 기준은?
        # nr, nc, tr, tc를 활용해보자.

        # 밀리는 기준은?
        # 1. 기사의 위치가 겹쳐지는 경우
        # 연쇄적으로 밀릴 수 있다.
        # 2. 단, 이동할 위치에 벽이 있다면 "무효"
        for idx in range(1, M+1):
            if idx in q_set:          continue           # 이미 밀거나, 이미 밀린 애라면 또 밀리지는 않으니까 패스

            ui, uj, uh, uw, _ = units[idx]
            for i in range(ti, ti+th):
                for j in range(tj, tj+tw):
                    if i >= ui and i <= ui+uh-1 and j >= uj and j <= uj+uw-1:   # 겹치는 경우
                        q.append(idx)


    for idx in range(1, M+1):
        if idx in q_set:                                  # 이동한 애였다면은 위치 업데이트
            units[idx][0] += di[dr]
            units[idx][1] += dj[dr]
            units[idx][4] -= tmp_damage[idx]              # 입은 데미지만큼 기사 체력에 반영

    for idx in range(1, M+1):
        damage[idx] += tmp_damage[idx]                    # 모든 기사가 입은 데미지 반영 (모든 기사가 밀린 이후에 데미지가 반영되어야 함)

# 데미지 세는 기준은?
    # 1. 밀린 기사여야 하고, 밀린 위치에 함정이 있어야 함. 그만큼 체력도 깎임.
    # 2. 단, 살아있는 기사 한정. 어떤 기사의 데미지가 체력보다 커지면 뒤지기 때문에 얘는 제외함.

for turn in range(1, Q+1):
    idx, dr = order[turn]                               # 이동할 기사, 이동할 방향
    move(idx, dr)

# print(units)
# print(damage)
# 구하려는 것: 데미지 총합
    # 1. 살아있는 기사 한정하여 입은 데미지
ans = 0
for idx in range(1, M+1):
    if units[idx][4] >= 1:
       ans += damage[idx]
print(ans)
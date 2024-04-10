# https://www.codetree.ai/training-field/frequent-problems/problems/rudolph-rebellion/description?page=1&pageSize=20
# https://www.youtube.com/watch?v=gOGgyXLFgYE&ab_channel=%EB%AC%B8%EC%96%B4%EB%B0%95%EC%82%ACIT%ED%8E%B8%EC%9D%98%EC%A0%90
N, M, P, C, D = map(int, input().split())
v = [[0]*N for _ in range(N)]

ri, rj = map(lambda x:int(x)-1, input().split())
v[ri][rj] = -1

score = [0]*(P+1)
alive = [1]*(P+1)
alive[0] = 0
stun = [1]*(P+1)

santa = [[0]*2 for _ in range(P+1)]
for _ in range(1, P+1):
    n, i, j = map(int, input().split())
    santa[n] = [i-1, j-1]
    v[i-1][j-1] = n

def move_santa(cur, si, sj, di, dj, mul):
    Q = [(cur, si, sj, mul)]

    while Q:
        cur, si, sj, mul = Q.pop(0)
        ni, nj = si + di*mul, sj + dj*mul
        if 0 <= ni < N and 0 <= nj < N:
            if v[ni][nj]==0:
                v[ni][nj] = cur
                santa[cur] = [ni, nj]
                return
            else:
                Q.append([v[ni][nj], ni, nj, 1])
                v[ni][nj]=cur
                santa[cur] = [ni, nj]
        else:
            alive[cur] = 0
            return

for turn in range(1, M+1):
    if alive.count(1)==0:
        break

    min = 2*N**2
    for idx in range(1, P+1):
        if alive[idx]==0: continue

        si, sj = santa[idx]
        dist=(ri-si)**2 + (rj-sj)**2

        if min > dist:
            min = dist
            mlst = [(si, sj, idx)]
        elif min==dist:
            mlst.append((si, sj, idx))

    mlst.sort(reverse=True)
    si, sj, min_idx = mlst[0]

    rdi = rdj = 0
    if ri>si:   rdi = -1
    elif ri<si: rdi = 1

    if rj>sj:   rdj = -1
    elif rj<sj: rdj = 1

    v[ri][rj]=0
    ri, rj = ri+rdi, rj+rdj
    v[ri][rj]=-1

    if (ri, rj)==(si, sj):
        score[min_idx] += C
        stun[min_idx] = turn+2
        move_santa(min_idx, si, sj, rdi, rdj, C)

    for idx in range(1, P+1):
        if alive[idx]==0:   continue
        if stun[idx] > turn: continue

        si, sj = santa[idx]
        min_dist = (ri-si)**2 + (rj-sj)**2
        tlst = []

        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = si+di, sj+dj
            dist = (ri-ni)**2 + (rj-nj)**2
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] <= 0 and min_dist > dist:
                min_dist = dist
                tlst.append((ni, nj, di, dj))
        if len(tlst)==0:    continue
        ni, nj, di, dj = tlst[-1]

        if (ri, rj)==(ni, nj):
            score[idx] += D
            stun[idx] = turn +2
            v[si][sj] = 0
            move_santa(idx, ni, nj, -di, -dj, D)
        else:
            v[si][sj] = 0
            v[ni][nj] = idx
            santa[idx]=[ni,nj]

    for i in range(1, P+1):
        if alive[i]==1:
            score[i] += 1

print(*score[1:])
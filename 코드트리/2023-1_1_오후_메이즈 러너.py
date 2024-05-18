N, M, K = map(int, input().split())     # N: 미로 사이즈, M: 참가자 수, K: 게임 시간

# 좌상단 (1,1)이라 했으니까 그냥 바깥쪽을 패딩씌워서 인덱스 동기화했음
maze = [[-1] * (N+2) for _ in range(N+2)]               # 0: 빈 칸, 1~9: 벽
for i in range(1, N+1):
    maze[i][1:N+1] = list(map(int, input().split()))

player = [(0, 0) for _ in range(M+1)]                   # 참가자 좌표
for i in range(1, M+1):
    r, c = map(int, input().split())
    player[i] = (r, c)

ei, ej = map(int, input().split())                      # exit row, exit col

distances = [0 for _ in range(M+1)]                     # 참가자 별 이동 거리 (1칸씩 이동하니까 이동 횟수로 봐도 무방)

is_contain = [0 for _ in range(M+1)]                    # 참가자 별 정사각형 포함 여부
is_exit = [0 for _ in range(M+1)]                       # 참가자 별 탈출 여부

# 상하좌우. 우선순위: 상하 > 좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for turn in range(1, K+1):                              # 게임 시작후 K초 지나면 게임 종료
    if is_exit.count(1) == K:                           # 모두 미로 탈출 시 게임 종료
        break

    # 참가자 이동 --------------------------------------------------------------------------------------------------------
    # 이동방향은 상하좌우
    # 거리 같으면 상하 우선 이동
    # i.e.
    # 0    출구
    # 참가자 0
    for idx in range(1, M+1):                           # 참가자 별 출구까지의 이동거리 구하기
        if is_exit[idx]:       continue                 # 탈출한 참가자는 이동할 필요가 없으므로

        pi, pj = player[idx]                            # 현재 좌표
        distance = abs(pi-ei) + abs(pj-ej)              # 출구와 가까운 곳: |x1-x2| + |y1-y2|

        # 이동할 칸은 출구와 가까운 곳
        # 움직일 수 없는 상황이란?
        # 출구와 가까운 곳으로 이동한다고 했기 때문에, 출구와 가까워지지 않으면 이동하지 않음

        tmp_distance = []
        for dr in range(4):
            ni, nj = pi+di[dr], pj+dj[dr]               # 이동할 좌표
            tmp_distance.append((abs(ni-ei) + abs(nj-ej), dr, ni, nj))

        tmp_distance.sort()

        for dr in range(4):
            ni, nj = tmp_distance[dr][2], tmp_distance[dr][3]
            if tmp_distance[dr][0] < distance and maze[ni][nj] == 0:                                # 가까워지는 방향이고, 이동할 곳에 벽이 없다면 이동
                player[idx] = (ni, nj)                                                              # 한 칸에 2명 이상 존재 가능
                distances[idx] += 1
                break

        if (ni, nj) == (ei, ej):                        # 이동했는데 탈출하게 되면 탈출 처리 해줌
            is_exit[idx] = 1

    # 미로 회전 ----------------------------------------------------------------------------------------------------------
    # 모든 참가자 이동하면 미로 회전

    # 정사각형을 어떻게 그림?
    # 1. 출구를 기준으로
    # 2. r=0, c=0 순으로 미로를 쭉 순회하면 됨.
    # (동일한 정사각형 >= 2 인 경우, 좌상단 r 작은것, 좌상단 c 작은것 우선 순으로 선택)
    # 2-1. 1x1 -> 2*2 -> 3*3 -> 4*4 -> ... 정사각형을 찾아나감
    # 2-2. 참가자가 있는지 확인해야 함
    # 2-3. 해당 정사각형 영역만큼 시계방향 90도 회전
    # 2-4. 회전된 벽 -= 1 (내구도 0이 되면 빈칸)

    # 정사각형 범위 지정
    def find_exit_and_player():
        global is_contain

        for depth in range(1, N+1):
            for i in range(1, N+1):
                for j in range(1, N+1):
                    contain_exit = 0
                    is_contain = [0 for _ in range(M + 1)]  # 출구가 없으면 참가자 여부 무효

                    if not i <= ei <= i+depth or not j <= ej <= j+depth:    # 선택한 사각형에서 출구가 없다면
                        continue

                    for idx in range(1, M+1):
                        if is_exit[idx]:
                            continue
                        p_i, p_j = player[idx]
                        if i <= p_i <= i+depth and j <= p_j <= j+depth:     # 선택한 사각형에서 참가자가 한명이라도 존재 한다면
                            contain_exit = 1
                            is_contain[idx] = 1

                    if contain_exit:
                        return i, j, i+depth, j+depth
        return 0, 0, 0, 0

    r_si, r_sj, r_ei, r_ej = find_exit_and_player()
    if not r_si and not r_sj and not r_ei and not r_ej:
        continue
    # print("사각형 영역: ", r_si, r_sj, r_ei, r_ej)
    rotate_maze = []                                                        # 1. 미로 회전

    for i in range(r_si, r_ei+1):                                           # 회전할 미로 영역
        rotate_maze.append(maze[i][r_sj:r_ej+1])

    tmp_player = [[0] * (N+2) for _ in range(N+2)]                          # 2. 참가자 회전

    for idx in range(1, M+1):
        if is_contain[idx]:
            i, j = player[idx]
            tmp_player[i][j] = idx

    tmp_player[ei][ej] = -1                                                  # 출구 표시

    rotate_player = []
    for i in range(r_si, r_ei+1):                                            # 회전할 참가자 영역
        rotate_player.append(tmp_player[i][r_sj:r_ej+1])

    rotate_maze = list(map(list, zip(*rotate_maze[::-1])))
    rotate_player = list(map(list, zip(*rotate_player[::-1])))

    r_i, r_j = 0, 0
    # 회전한 미로 반영
    for i in range(r_si, r_ei + 1):
        maze[i][r_sj:r_ej + 1] = rotate_maze[r_i][r_j:len(rotate_maze)]
        r_i += 1

    r_i, r_j = 0, 0
    # 회전한 참가자와 출구 반영
    for i in range(r_si, r_ei + 1):
        tmp_player[i][r_sj:r_ej + 1] = rotate_player[r_i][r_j:len(rotate_player)]
        r_i += 1

    for i in range(r_si, r_ei + 1):                                       # 회전된 영역의 벽 -= 1
        for j in range(r_sj, r_ej + 1):
            if 1 <= maze[i][j] <= 9:
                maze[i][j] -= 1
            if tmp_player[i][j] >= 1:
                player[tmp_player[i][j]] = i, j  # 회전한 플레이어 반영
            if tmp_player[i][j] == -1:  # 회전된 출구 위치 반영
                ei, ej = i, j

    # print("turn: ", turn, "---------------------------")
    #
    # for aa in maze:
    #     print(aa)
    # print()
    #
    # print("참가자 좌표:", player)
    #
    # print("점수:", distances)
    # print("출구:", ei, ej)
    # print("플레이어별 탈출 여부:", is_exit)

    is_contain = [0 for _ in range(M + 1)]

# ans
    # 모든 참가자들의 이동거리 합
    # 출구 좌표
#
total_distance = 0
for distance in distances:
    total_distance += distance
print(total_distance)
print(ei, ej)



# arr = [ [1, 2, 3],
#         [4 ,5, 6],
#         [7, 8, 9]]
#
# # 회전할 범위를 정해서 따로 배열로 분리
# narr = []
# narr.append(arr[0][:2])
# narr.append(arr[1][:2])
#
# # 회전
# narr = list(zip(*narr[::-1]))
# print(narr)
#
# # 기존 배열에 병합
# arr[0][:2] = narr[0][:2]
# arr[1][:2] = narr[1][:2]
#
# for a in arr:
#     print(a)
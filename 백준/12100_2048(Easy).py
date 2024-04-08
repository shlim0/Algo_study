# 3h 17m 1% 틀림
# 3h 30m 시간초과
# 분석까지 5h.
# https://aia1235.tistory.com/44 참고

# 한번 합쳐지면 끝임. 다른 블록과 합체 불가
    # 즉, 블록 추가 안됨
# 같은 수 >= 3개 이상이면 이동하려는 쪽이 먼저 합쳐짐
# 최대 5번 이동
    # 모든 경우의 수
    # < ^ > v
    # < ^ > v
    # < ^ > v
    # < ^ > v
    # < ^ > v
    # 4^5 = 1024가지의 경우가 나옴

    # 백트래킹 기준
    # 1. 가려는 방향으로 이동해도 값이 변할리 없는 경우 갈 필요 없음
    # 2. 가려는 방향으로 0이 "수직으로 모두" 채워져 있는 경우
        # i.e.
        # 4 2 0    0 4 2
        # 8 4 0 -> 0 8 4  (오른쪽 이동)
        # 16 8 0   0 16 8
        # -> 이동해도 의미 없음

        # counter i.e.
        # 4 0    0 4      (오른쪽 이동)
        # 8 4 -> 8 4
        # -> 이동 방향의 수직으로 0이 모두(2개)가 아닌 1개만 있는 경우.

        # counter i.e.2
        # 4 2 0    0 4 2
        # 8 0 0 -> 0 0 8  (오른쪽 이동)
        # 16 8 0   0 16 8
        # -> 이동 방향의 수직으로 0이 모두(0이채워진 모든열)가 아닌 1개 열만 채워진 경우.

    # -> 한 줄이라도 0이 모두 안채워져 있다? -> 탐색. 그게 아니면 탐색 X

    # 이동 조건 결론
    # 1. 가로 또는 세로에 같은 값이 있거나
    # 2. 어떤 한 라인의 0의 개수가 1개 이상이고 N제곱꼴 아닌 형태로 있거나 (N^0 제외. N^1, N^2, N^3, ...)
    # (0개수 % N != 0)
    # XXXXX(잘못 찾음) 이동하기 전 0의 개수와 지금의 0의 개수가 동일할 때 (합쳐져야 0의 개수가 증가하므로)
        # 16 2 0    0 16 2
        # 8 4 2 ->  8 4 2 (오른쪽 이동)
        # 16 8 0    0 16 8
        # -> < / ^ / > / v 어느쪽으로 한 번 이동해도 0의 개수가 그대로인 경우. 그냥 종료.
    # 3. 이동했는 데, 이전 배열과 완전 동일한 경우 종료

    # 이동할 때
    # 가장 왼쪽, 가장 윗쪽, 가장 오른쪽, 가장 아랫쪽을 기준으로 이동
        # 해당 기준을 토대로 해당 라인의 값들을 합치는 결정을 함
        # 1. <: 1 ~ N-1, j (1에서부터 N-1까지. 1이 기준(0) 바로 다음이라)
        # 2. ^: 1 ~ N-1, i
        # 3. >: N-2 ~ 0, j (N-2에서부터 0까지. N-2가 기준(N-1) 바로 앞이라)
        # 4. v: N-2 ~ 0, i

import copy

N = int(input())
origin = [list(map(int, input().split())) for _ in range(N)]

max_value = 0
# < / ^ / > / v
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def move(arr, direction):
    # <
    if direction == 0:
        for i in range(N):
            cursor = 0
            for j in range(1, N):
                if arr[i][j] != 0:  # 0이 아닌 값이
                    tmp = arr[i][j]
                    arr[i][j] = 0  # 일단 비워질꺼니까 0으로 바꿈

                    if arr[i][cursor] == 0:  # 비어있으면
                        arr[i][cursor] = tmp  # 옮긴다

                    elif arr[i][cursor] == tmp:  # 같으면
                        arr[i][cursor] *= 2  # 합친다
                        cursor += 1
                    else:  # 비어있지도 않고 다른 값일때
                        cursor += 1  # pass
                        arr[i][cursor] = tmp  # 바로 옆에 붙임
    # >
    elif direction == 2:
        for i in range(N):
            cursor = N - 1
            for j in range(N - 1, -1, -1):

                if arr[i][j] != 0:
                    tmp = arr[i][j]
                    arr[i][j] = 0

                    if arr[i][cursor] == 0:
                        arr[i][cursor] = tmp

                    elif arr[i][cursor] == tmp:
                        arr[i][cursor] *= 2
                        cursor -= 1
                    else:
                        cursor -= 1
                        arr[i][cursor] = tmp

    # ^
    elif direction == 1:
        for j in range(N):
            cursor = 0
            for i in range(N):
                if arr[i][j] != 0:
                    tmp = arr[i][j]
                    arr[i][j] = 0

                    if arr[cursor][j] == 0:
                        arr[cursor][j] = tmp

                    elif arr[cursor][j] == tmp:
                        arr[cursor][j] *= 2
                        cursor += 1

                    else:
                        cursor += 1
                        arr[cursor][j] = tmp

    # v
    elif direction == 3:
        for j in range(N):
            cursor = N - 1
            for i in range(N - 1, -1, -1):
                if arr[i][j] != 0:
                    tmp = arr[i][j]
                    arr[i][j] = 0

                    if arr[cursor][j] == 0:
                        arr[cursor][j] = tmp

                    elif arr[cursor][j] == tmp:
                        arr[cursor][j] *= 2
                        cursor -= 1

                    else:
                        cursor -= 1
                        arr[cursor][j] = tmp

def recursive(origin, depth):
    global max_value
    # 최대 깊이면 탐색 안함
    if depth == 5:
        for i in range(N):
            for j in range(N):
                if origin[i][j] > max_value:
                    max_value = origin[i][j]
        return

    for i in range(4):
        arr = copy.deepcopy(origin)
        move(arr, i)
        recursive(arr, depth+1)

recursive(origin, 0)
print(max_value)
# 20
# 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
# 2 2 2 2 16 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 8 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 4 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 8 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 8 2 2 2 2 2 512 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 8 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 16 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 4 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 1024 2 2 2 2 2 2 2 2 2 2
# 2 2 2 2 2 2 2 2 2 2 2 2 2 32 2 2 2 2 2 2
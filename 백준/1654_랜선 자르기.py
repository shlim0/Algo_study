# 1h 47m
# 0. 완전 탐색 -> 시간 초과
# 1. 이분 탐색 오랜만 -> 50분 헤맴
# 2. s = m + 1, e = m - 1 조건 생각. K<=M인 e를 구하기.
# 3. basis = LAN[len(LAN)-1]      # 오름차순 정렬이기 때문에, 첫 번째 랜선의 길이가 최소 -> 틀림

# 참고한 테케
#     10 10
#     111
#     222
#     333
#     444
#     555
#     666
#     777
#     888
#     999
#     1000
    # 굳이, 111 짜리까지 자를 필요 없이 같은 길이의 랜선 10개 만들 수 있음.

    # 정답: 444

    # 10 11
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 1
    # 10

    # 정답: 1

    # 4 4
    # 200
    # 200
    # 200
    # 200

    # 정답: 200

K, N = map(int, input().split())
LAN = [int(input().rstrip()) for _ in range(K)]
start, end = 1, max(LAN)

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for now in LAN:
        cnt += now // mid

    if cnt < N:         # 원하는 개수만큼 못 자르면 자르는 단위를 키우기
        end = mid - 1
    elif cnt >= N:      # 자르는 단위를 줄여서 최대 이익 내기
        start = mid + 1

print(end)
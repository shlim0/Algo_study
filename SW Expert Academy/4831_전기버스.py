# 정류장: 0 ~ N
# 최대 이동 가능한 정류장 수: K
# 충전기 설치된 정류장: M
# 몇번 충전하면 도달가능?
    # 1. 도달 불가능시 0 출력

for tc in range(1, int(input())+1):
    k, n, m = map(int, input().split())
    m_data = set(map(int, input().split()))

    # 일단 k칸 가고 시작
    bus = k
    cnt = 0

    # 최종지점 가면 충전 불필요
    while bus < n:
        # k칸 만큼 돌아보고 그리디하게 접근
        for pos in range(bus, bus-k, -1):
            if pos in m_data:
                cnt += 1
                bus = pos
                break
        # for-else
        else:
            cnt = 0
            break

        # 그리디한 곳부터 다시 k칸 가서 탐색
        bus += k

    print(f'#{tc} {cnt}')
# 2 min
for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))

    sum = 0
    for v in arr:
        if not v % 2 == 0:
            sum += v

    print(f'#{tc} {sum}')
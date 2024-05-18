# 10m 30s
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    sum = 0
    last = arr[len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        now = arr[i]

        if now < last:
           sum += last - now
        elif now > last:
            last = now

    print(f'#{tc} {sum}')
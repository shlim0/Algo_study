# 17 min
for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(2, N-2):
        # front front, front, current, next, next next
        ff, f, c, n, nn = arr[i-2], arr[i-1], arr[i], arr[i+1], arr[i+2]

        if c < ff or c < f or c < n or c < nn:  continue

        ans += c - max(ff, f, n, nn)

    print(f'#{tc} {ans}')
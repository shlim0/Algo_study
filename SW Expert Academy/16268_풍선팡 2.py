dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max = 0

    for r in range(n):
        for c in range(m):
            cmp = arr[r][c]
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if nr < 0 or nr >= n or nc <A 0 or nc >= m:
                    continue
                else:
                    cmp += arr[nr][nc]

            if max < cmp:
                max = cmp

    print(f'#{tc} {max}')
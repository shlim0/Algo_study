def find(lines):
    for line in lines:
        for i in range(n - m + 1):
            some_line = line[i:i+m]
            if some_line == some_line[::-1]:
                return some_line

for tc in range(1, int(input()) + 1, 1):
    n, m = map(int, input().split())
    lines = [input() for _ in range(n)]

    if find(lines):
        print(f'#{tc} {find(lines)}')
        continue

    lines = [''.join(line) for line in list(zip(*lines))]

    if find(lines):
        print(f'#{tc} {find(lines)}')

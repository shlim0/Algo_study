def find(lines):
    for line in lines:
        for i in range(n - m + 1):
            # m 만큼 특정구간을 정해 reverse 하는게 더 정신건강에 이로움
            some_line = line[i:i+m]
            if some_line == some_line[::-1]:
                return some_line

for tc in range(1, int(input()) + 1, 1):
    n, m = map(int, input().split())
    lines = [input() for _ in range(n)]

    if find(lines):
        print(f'#{tc} {find(lines)}')
        continue

    # transpose 하면 한 글자씩 쪼개지는 걸 합쳐줌
    lines = [''.join(line) for line in list(zip(*lines))]

    if find(lines):
        print(f'#{tc} {find(lines)}')

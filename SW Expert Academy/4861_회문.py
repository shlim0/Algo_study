# 1h 17m

def find(lines, y_lines):
    # palindrome x axis
    for line in lines:
        if line == line[::-1]:
            print(f'#{tc} {line}')
            return

        for m_step in range(n - m + 1):
            if line[m_step: m_step+m :1] == line[m_step+m-1: m_step-1: -1]:
                print(f'#{tc} {line[m_step: m_step+m :1]}')
                return

    # n = 20, m = 13
    # 0~12
    # 1~13
    # 2~14
    # ...
    # 8~20
    # -> n - m + 2번 (시작지점이 0~8까지 도니까)

    # making transpose array
    for i in range(len(line)):
        y_line = ""
        for line in lines:
            y_line += (line[i])
        y_lines.append(y_line)

    # palindrome y axis
    for line in y_lines:
        if line == line[::-1]:
            print(f'#{tc} {line}')
            return

        for m_step in range(n - m + 1):
            if line[m_step: m_step + m:1] == line[m_step + m - 1: m_step - 1: -1]:
                print(f'#{tc} {line[m_step: m_step + m:1]}')
                return

for tc in range(1, int(input().rstrip()) + 1, 1):
    n, m = map(int, input().split())
    lines, y_lines = [], []

    for _ in range(n):
        lines.append(input().rstrip())

    find(lines, y_lines)
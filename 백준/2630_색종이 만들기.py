n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def devide_conquer(r, c, n):
    global white, blue
    # 해당 배열의 [0][0]에 위치한 원소를 기준으로 비교
    basis = paper[r][c]

    for i in range(r, r + n):
        for j in range(c, c + n):
            if basis != paper[i][j]:
                devide_conquer(r, c, n // 2)
                devide_conquer(r, c + n // 2, n // 2)
                devide_conquer(r + n // 2, c, n // 2)
                devide_conquer(r + n // 2, c + n // 2, n // 2)

                # 색종이가 쪼개지는 경우까지 카운트할 필요는 없기 때문에 return
                return

    if basis == 0:
        white += 1
    else:
        blue += 1

devide_conquer(0, 0, n)
print(white)
print(blue)
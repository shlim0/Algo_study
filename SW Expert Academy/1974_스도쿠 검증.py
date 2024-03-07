# 47 min
def find(sudoku):
    for i in range(len(sudoku)):
        target = [value for value in range(1, 10)]
        if sum(sudoku[i]) != sum(target):
            return False
    return True
def findRectangle(sudoku):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = []
            for r in range(3):
                for c in range(3):
                    tmp.append(sudoku[i+r][j+c])
            if len(set(tmp)) != 9:
                return False
    return True

for tc in range(1, int(input()) + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    y_sudoku = list(zip(*sudoku))

    if find(sudoku) and find(y_sudoku) and findRectangle(sudoku):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq
for tc in range(1, int(input())+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    r_check, c_check, rect_check = [i for i in range(1, 10)], [i for i in range(1, 10)], [i for i in range(1, 10)]

    min_r_index, max_r_index = 0, 3
    for _ in range(3):
        min_c_index, max_c_index = 0, 3
        for _ in range(3):
            cmp = []
            for r in range(min_r_index, max_r_index):
                for c in range(min_c_index, max_c_index):
                    # 1. 가로 체크
                    if sudoku[r][c] in r_check:
                        r_check[sudoku[r][c] - 1] = -1
                    else:
                        print(f'#{tc} 0')
                        exit()
                    # 2. 세로 체크
                    if list(zip(*sudoku))[r][c] in c_check:
                        c_check[sudoku[r][c] - 1] = -1
                    else:
                        print(f'#{tc} 0')
                        exit()

                    # 3. 현재 위치 체크
                    cmp.append(sudoku[r][c])

            for i in range(9):
                if cmp[i] in rect_check:
                    rect_check[sudoku[r][c] - 1] = -1
                else:
                    print(f'#{tc} 0')
                    exit()


            min_c_index += 3
            max_c_index += 3
        min_r_index += 3
        max_r_index += 3

    print(f'#{tc} 1')
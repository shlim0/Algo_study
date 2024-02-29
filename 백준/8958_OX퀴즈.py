#  6 min
for tc in range(int(input())):
    datas = input()
    is_continuous = False
    cnt = 0
    point = 0

    for data in datas:
        if data == "O":
            if is_continuous == True:
                cnt += 1
            else:
                is_continuous = True
                cnt = 1
            point += cnt
        elif data == "X":
            is_continuous = False

    print(point)
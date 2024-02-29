for tc in range(int(input())):
    datas = []
    for k in range(int(input())):
        datas.append(input())

    # data[0] <-> [1], [2], [3], [4]
    # data[1] <-> [2], [3], [4]
    # ...

    f_flag, t_flag = False, False

    for i in range(len(datas)):
        for j in range(i):
            if i == j:
                continue
            # append to front
            front = datas[j] + datas[i]
            # append to tail
            tail = datas[i] + datas[j]

            for f_i in range(int(len(front) / 2)):
                if front[f_i] == front[len(front) - f_i - 1]:
                    f_flag = True
                    continue
                else:
                    f_flag = False
                    break

            for t_i in range(int(len(tail) / 2)):
                if tail[t_i] == tail[len(tail) - t_i - 1]:
                    t_flag = True
                    continue
                else:
                    t_flag = False
                    break

            if f_flag == True:
                print(front)
                break
            elif t_flag == True:
                print(tail)
                break

        if (f_flag == True or t_flag == True):
            break

    if (f_flag == False and t_flag == False):
        print("0")
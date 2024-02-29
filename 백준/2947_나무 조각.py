data = list(map(int, input().split()))
for _ in data:
    for j in range(len(data) - 1):
        if data[j] > data[j + 1]:
            # tmp = data[j + 1]
            # data[j + 1] = data[j]
            # data[j] = tmp
            data[j], data[j+1] = data[j+1], data[j]

            print(*data)
            # a = str()
            # for k in data:
            #     a += str(k) + " "
            # print(a)
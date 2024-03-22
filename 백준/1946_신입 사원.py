import sys
input = sys.stdin.readline

for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        arr.append(list(map(int, input().split())))

    arr.sort()
    standard = arr[0][1]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i][1] < standard:
            cnt += 1
            standard = arr[i][1]

    print(cnt)
# 5 min
arr = []
for _ in range(1, int(input()) + 1):
    arr.append(list(map(int, input().split())))

arr.sort(key= lambda x: (x[0], x[1]))

for now in arr:
    print(*now)
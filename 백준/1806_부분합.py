# https://blog.encrypted.gg/1004
# 먼저 값을 빼주고 인덱스를 옮겨야 했다...
N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))

p1, p2 = 0, 0
mn = 99999999999999
total = arr[0]

while p1 <= p2:
    if total < S:
        p2 += 1
        if p2 < N:
            total += arr[p2]
        else:
            break
    else:
        # print(p1, p2, arr[p1:p2+1])
        mn = min(p2-p1+1, mn)
        total -= arr[p1]
        p1 += 1

if mn == 99999999999999:
    print(0)
else:
    print(mn)

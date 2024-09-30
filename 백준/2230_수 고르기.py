# https://blog.encrypted.gg/1004
n, m = list(map(int, input().split()))
arr = [int(input()) for _ in range(n)]
arr.sort()

mn = 9999999999
p1, p2 = 0, 0

while p1 <= p2 and p2 < n:
    diff = arr[p2] - arr[p1]
    if diff < m:
        p2 += 1
    else:
        mn = min(diff, mn)
        p1 += 1

print(mn)
# 10 min
N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

ans = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            if i == j or j == k or i == k:
                continue
            sum = arr[i] + arr[j] + arr[k]
            if ans < sum <= M:
                ans = sum

print(ans)
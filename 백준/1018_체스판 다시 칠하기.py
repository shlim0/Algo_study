# 38 min
import sys
input = sys.stdin.readline
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우
N, M = list(map(int, input().split()))
arr = [[v for v in input().strip()] for _ in range(N)]

mn = float('inf')

for i in range((N+1)-8):
    for j in range((M+1)-8):
        basis = arr[i][j]
        cnt_same, cnt_diff = 0, 0 # basis와 same인지 diff인지에 따라 cnt
        for i_k in range(i, i+8):
            for j_k in range(j, j+8):
                if (i_k % 2 == i % 2 and j_k % 2 == j % 2) or (i_k % 2 != i % 2 and j_k % 2 != j % 2):
                    # print(basis, i_k, j_k, arr[i_k][j_k], basis != arr[i_k][j_k])
                    if not basis == arr[i_k][j_k]:
                        cnt_same += 1
                    if basis == arr[i_k][j_k]:
                        cnt_diff += 1
                if (i_k % 2 == i % 2 and j_k % 2 != j % 2) or (i_k % 2 != i % 2 and j_k % 2 == j % 2):
                    # print(i, j, basis, i_k, j_k, arr[i_k][j_k], basis == arr[i_k][j_k])
                    if not basis == arr[i_k][j_k]:
                        cnt_diff += 1
                    if basis == arr[i_k][j_k]:
                        cnt_same += 1

        mn = min(cnt_same, cnt_diff, mn)

print(mn)
# 1h - 이분탐색으로 하다가 그냥 dict 활용하는 방식으로 바꿈
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

d = defaultdict(int)

for a in A:
    d[a] += 1

for b in B:
    if d[b]:
        print(d[b], end=" ")
    else:
        print(0, end=" ")
# 13 min
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted([*set(arr)])
d = defaultdict(int)

for i in range(0, len(sorted_arr)):
    value = sorted_arr[i]
    if not d[value]:
        d[value] = i

for value in arr:
    print(d[value], end=" ")
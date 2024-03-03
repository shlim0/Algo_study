# 1h 20m + googling

# 4
# A
# B
# C
# D
# D
# A
# B
# C

import sys
from collections import defaultdict
input = sys.stdin.readline

before, after = defaultdict(str), []

n = int(input().rstrip())

for tc in range(n):
    before[input().rstrip()] = tc
    # before = defaultdict(None, {'A': 0, 'B': 1, 'C': 2, 'D': 3})

for tc in range(n):
    after.append(input().rstrip())
    # after = [D, A, B, C]
cnt = 0

for i in range(n-1):
    for j in range(i+1, n, 1):
        if before[after[i]] > before[after[j]]:
            cnt += 1
            break
print(cnt)
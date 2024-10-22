# 35 min
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N-1)]
d = defaultdict(list)
tree = defaultdict(int)
root = 1

for a1, a2 in arr:
    d[a1].append(a2)
    d[a2].append(a1)

target = [root]
while target:
    parent = target.pop()
    for child in d[parent]:
        if not tree[child]:
            tree[child] = parent
            target.append(child)

for i in range(2, N+1):
    print(tree[i])
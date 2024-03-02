import sys
input = sys.stdin.readline

from collections import defaultdict
n, m = map(int, input().split())

# key: str, value: int
pocketmons = defaultdict(int)

for i in range(n):
    name = input().rstrip()

    pocketmons[name] = str(i + 1)
    pocketmons[str(i + 1)] = name

for _ in range(m):
    print(pocketmons[input().rstrip()])
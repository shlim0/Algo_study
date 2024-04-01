from collections import deque

n = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
stack, visited = set([1]), set([1])

for _ in range(int(input())):
    start, end = map(int, input().split())
    arr[start][end] = 1
    arr[end][start] = 1

while stack:
    now = stack.pop()

    for destination in range(1, n+1):
        if arr[now][destination] == 1 and destination not in visited:
            stack.add(destination)
            visited.add(destination)
            print(now, destination, stack, visited)

print(len(visited) - 1)
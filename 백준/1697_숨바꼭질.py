# 20 min
from collections import deque
import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
Q = deque()
visited = [float('inf') for _ in range(100002)]
Q.append((N, 0))

while Q:
    X, t = Q.popleft()

    if X == K:
        print(t)
        break

    if 0 <= 2*X < len(visited) and visited[2*X] > t+1:
        visited[2*X] = t+1
        Q.append((2*X, t+1))

    if 0 <= X+1 < len(visited) and visited[X+1] > t+1:
        visited[X+1] = t+1
        Q.append((X+1, t+1))

    if 0 <= X-1 < len(visited) and visited[X-1] > t+1:
        visited[X-1] = t+1
        Q.append((X-1, t+1))
import sys
from queue import PriorityQueue

input = sys.stdin.readline
INF = int(1e9)
pq = PriorityQueue()

V, E = list(map(int, input().split()))
arr = [[] for _ in range(V+1)] # [0]은 사용안함
dist = [INF] * (V+1)
start = int(input())

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    arr[u].append((v, w))

pq.put((0, start))
dist[start] = 0

while not pq.empty():
    w, now = pq.get()
    if dist[now] < w:
        continue
    for now_v, now_w in arr[now]:
        if dist[now_v] > dist[now] + now_w:
            dist[now_v] = dist[now] + now_w
            pq.put((dist[now_v], now_v))

for element in range(1, V+1):
    if dist[element] == INF:
        print("INF")
    else:
        print(dist[element])

# https://www.acmicpc.net/board/view/103139
# 10 9
# 1
# 1 2 9
# 2 8 9
# 7 3 10
# 5 6 6
# 3 4 7
# 4 5 2
# 6 10 8
# 8 5 4
# 2 3 10
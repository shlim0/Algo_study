# 72 min 시간초과
# 1h 21min sol
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]  # 1번 도시, ..., n번 도시
dist = [float('inf') for _ in range(n+1)]
pre = [0 for _ in range(n+1)] # 도시 이동 기록 저장

for _ in range(m):
    u, v, w = list(map(int, input().split()))
    arr[u].append((v, w))

start, end = list(map(int, input().split()))
dist[start] = 0
heap = []
heapq.heappush(heap, (dist[start], start)) # w, u

while heap:
    w, u = heapq.heappop(heap)

    if dist[u] < w:
        continue

    for now_v, now_w in arr[u]:
        if dist[now_v] > w + now_w:
            dist[now_v] = w + now_w
            heapq.heappush(heap, (w + now_w, now_v))
            pre[now_v] = u

path = [end]
for i in range(1, n+1):
    path_last = path[len(path) - 1]
    if pre[path_last] > 0:
        path.append(pre[path_last])
    else:
        break
print(dist[end])
print(len(path))
print(*path[::-1])
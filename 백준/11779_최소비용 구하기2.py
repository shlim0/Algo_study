# 72 min 시간초과
# 1h 21min sol
import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]  # 1번 도시, ..., n번 도시
dist = [float('inf') for _ in range(n+1)]
pre = [0 for _ in range(n+1)]   # 도시 이동 기록 저장

for _ in range(m):
    # u: 시작점, v: 도착점, w: 거리(가중치)
    u, v, w = list(map(int, input().split()))
    arr[u].append((v, w))   # 특정 지점과 연결된 모든 지점에 대한 경로 저장

start, end = list(map(int, input().split()))    # 문제에서 주어진 시작과 끝
dist[start] = 0     # 시작 지점의 거리는 항상 0
heap = []
heapq.heappush(heap, (dist[start], start)) # w, u. 거리를 기준으로 우선순위를 정렬

while heap:
    w, u = heapq.heappop(heap)

    if dist[u] < w:         # 기존 거리보다 길면 굳이 탐색할 필요 없으니
        continue

    for now_v, now_w in arr[u]: # 현재 지점에서 연결된 모든 지점의 거리 갱신
        if dist[now_v] > w + now_w: # 기존 거리, 갱신할 거리 비교후 갱신
            dist[now_v] = w + now_w # 거리 갱신
            heapq.heappush(heap, (w + now_w, now_v)) # 연쇄적으로 거리 갱신
            pre[now_v] = u  # 앞서 어떤 지점에서 왔는지 갱신

path = [end]    # 도착 지점에서 역추적
for i in range(1, n+1):
    path_last = path[len(path) - 1]     # 이전에 방문한 지점을 가져옴
    if pre[path_last] > 0:              # 이전에 방문한 지점이 0이면 시작지점을 의미
        path.append(pre[path_last])
    else:
        break
print(dist[end])
print(len(path))
print(*path[::-1])  # 도착 지점에서 시작 지점을 구한걸 역순으로 출력
# 25 min 2퍼틀
from queue import PriorityQueue

pq = PriorityQueue()

V, E = list(map(int, input().split()))
arr = [float('inf') for _ in range(V+1)] # [0]은 사용안함
start = int(input())

arr[start] = 0

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    pq.put(((u, v), w))

while not pq.empty():
    (u, v), w = pq.get()

    arr[v] = min(arr[v], arr[u] + w)

for element in range(1, V+1):
    if arr[element] == float('inf'):
        print("INF")
    else:
        print(arr[element])



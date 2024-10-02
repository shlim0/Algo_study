# 3 min
import sys
import heapq

heap = []
N = int(input())
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    elif x > 0:
        heapq.heappush(heap, x)

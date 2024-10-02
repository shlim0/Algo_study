import sys
from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()
for _ in range(N):
    x = int(sys.stdin.readline())

    if x == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get())
    elif x > 0:
        pq.put(x)
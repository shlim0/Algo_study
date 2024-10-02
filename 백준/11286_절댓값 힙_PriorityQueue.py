import sys
from queue import PriorityQueue

pq = PriorityQueue()
N = int(input())

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[1])
    elif x > 0:
        pq.put((x, x))
    else:
        pq.put((-x, x))
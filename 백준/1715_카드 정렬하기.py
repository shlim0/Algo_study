# 8m 30s
import sys
from queue import PriorityQueue

pq = PriorityQueue()
N = int(input())
for _ in range(N):
    x = int(sys.stdin.readline())
    pq.put(x)

cnt = 0
while pq.qsize() >= 2:
    c1, c2 = pq.get(), pq.get()
    c = c1+c2
    cnt += c
    pq.put(c)

print(cnt)
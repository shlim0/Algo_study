# 20 min
import heapq
# tc1
# 23 / 4
# 64 -> 32 32x -> 16 16 -> 8x 8 16 -> 4 4 16 -> 2 2 4 16 -> 1x 1 2 4 16 -> 1 2 4 16 (END)

X = int(input())
sticks = []

if X < 64:
    heapq.heappush(sticks, 32)
    if not X <= 32:
        heapq.heappush(sticks, 32)
    if X == 32:
        print(1)
        exit()
else:
    print(1)
    exit()

while True:
    stick = heapq.heappop(sticks)
    heapq.heappush(sticks, stick // 2)
    if not X <= sum(sticks):
        heapq.heappush(sticks, stick // 2)
    if X == sum(sticks):
        print(len(sticks))
        break
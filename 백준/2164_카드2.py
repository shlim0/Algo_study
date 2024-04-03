# 10 min
# 1...N
# TOP...DOWN
from collections import deque

card = deque()

for i in range(1, int(input()) + 1):
    card.append(i)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card.pop())
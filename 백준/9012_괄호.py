# 10 min
from collections import deque

for _ in range(int(input())):
    stack = deque()
    tmp = input()
    for i in range(len(tmp)):
        stack.append(tmp[i])

    l_cnt, r_cnt = 0, 0
    while(stack):
        target = stack.popleft()
        if target == "(":
            l_cnt += 1
        elif target == ")":
            r_cnt += 1

        if l_cnt < r_cnt:
            break

    if l_cnt == r_cnt:
        print("YES")
    else:
        print("NO")
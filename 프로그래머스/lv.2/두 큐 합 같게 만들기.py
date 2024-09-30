# 26 min... 바킹독 그는 신이야
# len(q1) == len(q2)
# 1회 cost: pop() and insert()

def solution(queue1, queue2):
    cnt = 0
    q = queue1 + queue2
    p1, p2 = 0, len(queue1)
    s1, s2 = sum(q[p1:p2]), sum(q[p2:len(q)])

    while True:
        if p1 >= p2:
            print(-1)
            return -1

        if s1 == s2:
            print(cnt)
            return cnt
        elif s1 < s2:
            s1 += q[p2]
            s2 -= q[p2]
            p2 += 1
            p2 %= len(q)
            cnt += 1
        elif s1 > s2:
            s1 -= q[p1]
            s2 += q[p1]
            p1 += 1
            p1 %= len(q)
            cnt += 1

solution([3, 2, 7, 2]	,[4, 6, 5, 1]	)
solution([1, 2, 1, 2]	, [1, 10, 1, 2]	)
solution([1, 1]	,[1, 5]	)

# tc3 - 1
# 1, 1        1, 5
# p1          p2
# -> s1 < s2, p2++

# tc3 - 2
# 1, 1, 1     5
# p1          p2
# -> s1 < s2, p2++

# tc3 - 2
# [1, 1, 1, 5]   []
# p1 == p2
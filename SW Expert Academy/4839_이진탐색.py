# 17 min
# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg&&
def binary_search(l, r, target, cnt):
    c = (l + r) // 2
    if c == target:
        return cnt
    elif c < target:
        cnt += 1
        return binary_search(c, r, target, cnt)
    elif c > target:
        cnt += 1
        return binary_search(l, c, target, cnt)

for tc in range(1, int(input()) + 1):
    p, a, b = map(int, input().split())

    a_cnt = binary_search(1, p, a, 0)
    b_cnt = binary_search(1, p, b, 0)

    if a_cnt < b_cnt:
        print(f'#{tc} A')
    elif a_cnt > b_cnt:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
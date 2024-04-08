# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg&&#
# 56 min 5/10 통과 (시간 초과)

def checker(check):
    for val in check:
        if val == 0:
            return False
    return True

def recursive(i, acc):
    global min_value

    if acc >= min_value:
        return

    if checker(check):
        tmp = 0
        for k in sel:
            tmp += int(k)

        if min_value > tmp:
            min_value = tmp
        return
        # print(sel, check, tmp)

    for j in range(N):
        # print(i, j, sel)
        if not check[j]:
            check[j] = 1
            sel[j] = int(arr[i][j])

            recursive(i+1, acc + sel[j])K
            check[j] = 0
            sel[j] = 0

for tc in range(1, int(input())+1):
    min_value = 9999999

    N = int(input())
    arr = [input().split() for _ in range(N)]

    sel = [0] * N # 디버깅용
    check = [0] * N

    recursive(0, 0)
    print(f'#{tc} {min_value}')
    # 2 1 2
    # 5 8 5
    # 7 2 2

    # 2 8 2
    #   5 2
    # 1 5 2 -> ans
    #   5 7
    # 2 5 2
    #   8 7


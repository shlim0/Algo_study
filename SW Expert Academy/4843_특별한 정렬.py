# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg&&#
# 8m 42s

for tc in range(1, int(input()) + 1):
    _ = int(input())
    arr = list(map(int, input().split()))
    asc, desc = sorted(arr), sorted(arr, reverse=True)
    new_sort = []

    for i in range(5):
        new_sort.append(desc[i])
        new_sort.append(asc[i])

    print(f'#{tc}', *new_sort)
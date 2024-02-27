# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg#
# 37m
# 1. 정렬 후
# 2. 더하고 빼기

tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    newData = list()

    for j in range(n-m+1):
        tmp = 0
        for k in range(m):
            tmp += data[j+k]
        newData.append(tmp)

    print(f"#{i+1} " + f"{max(newData)-min(newData)}")
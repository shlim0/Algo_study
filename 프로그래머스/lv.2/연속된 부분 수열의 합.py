# 1:10
# 1:30 시간초과
# def solution(sequence, k):
#     arr = []
#     sum = 0

#     for i in range(len(sequence)):
#         sum = sequence[i]
#         if sum == k:
#             arr.append([i, j])
#             break

#         for j in range(i+1, len(sequence)):
#             sum += sequence[j]

#             if sum > k:
#                 break
#             elif sum == k:
#                 arr.append([i, j])
#                 break

#     arr.sort(key=lambda x: x[1] -x[0])

#     return arr[0]


# 1:55 아까보단 더 맞았으나 시간초과
# from collections import deque
# def solution(sequence, k):
# #     하나씩 순차로 쌓아가다가 sum >= k이 되면 기록하고
# #     k > sum이 될때까지 맨 앞부터 값을 하나씩 뺀 뒤 이후 값을 쌓아가는 방식?

#     ans = []
#     total = deque()
#     s = 0
#     for i in range(len(sequence)):
#         if sum(total) < k:
#             total.append(sequence[i])
#         if sum(total) > k:
#             while sum(total) > k:
#                 total.popleft()
#                 s += 1
#         if sum(total) == k:
#             ans.append([s, i])
#             total.popleft()
#             s += 1

#     ans.sort(key=lambda x: x[1] -x[0])
#     return ans[0]

# def solution(sequence, k):
#         ans = []
#         s = 0
#         result = len(sequence)
#         for i in range(len(sequence)+1):
#             if sum(sequence[s:i]) > k:
#                 while sum(sequence[s:i]) > k:
#                     s += 1
#             if sum(sequence[s:i]) == k and (i-1)-s < result:
#                 ans.append([s, i-1])
#                 s += 1

#         ans.sort(key=lambda x: x[1] -x[0])
#         return ans[0]

# 2:40
# 구글링해보니 구간폭을 기록하고, sum()를 쓰지 않고 합을 기록함.
# 제출해보니, sum()을 매번 사용하여 비교했기 때문에 시간초과가 남을 확인함.
def solution(sequence, k):
    ans = []
    s = 0
    interval = len(sequence)
    sum = 0

    for i in range(len(sequence)):
        sum += sequence[i]

        while sum > k:
            sum -= sequence[s]
            s += 1
        if sum == k and i - s < interval:
            ans = [s, i]
            interval = i - s

    return ans
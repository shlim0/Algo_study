# 1h 10min 시간 초과
# 1. is_used를 1d array로 해야함.
# 2. \ 대각을 r-c 형태로 해서 같은 대각에 있는지를 검사해야함
# 3. arr는 불필요

# # i) 상하: 열이 같은지 체크하면 됨
# # ii) 좌우: 한 행에 퀸 놓으면 다음 행 가기 때문에 노상관
# # iii) 대각: / 대각이랑 \ 대각으로 경우의 수가 나뉨
# #     a) /: 퀸을 놓은 (r,c)와 r+c가 같은 지점
# #     i.e.
# #     [] [] [] []  -> (0, 3)
# #     [] [] [ㅇ] [] -> (1, 2)
# #     [] [] [] []   -> (2, 1)
# #     [] [] [] []   -> (3, 0)
#
# #     b) \: 퀸을 놓은 (r,c)에서 r+c+2x 인 지점 (단, x는 < 0일수도 있음)
# #     i.e.
# #     [] [] [] []  -> (0, 0)
# #     [] [ㅇ] [] [] -> (1, 1)
# #     [] [] [] []   -> (2, 2)
# #     [] [] [] []   -> (3, 3)
#
# cnt = 0
#
# def print2d(arr):
#     for i in range(N):
#         print(*arr[i])
#     print()
#
# def backtrack(k):
#     global cnt
#     if k == N:
#        cnt += 1
#        return
#
#     for i in range(k, N):
#         for j in range(N):
#             if not (is_used1[i][j] or is_used2[i][j] or is_used3[i][j]):
#                 arr[i][j] = 1
#
#                 for ii in range(N):
#                     is_used1[ii][j] = 1
#                     for jj in range(N):
#                         if i+j == ii + jj:
#                             is_used2[ii][jj] = 1
#                         if i+j + 2*(ii-i) == ii + jj:
#                             is_used3[ii][jj] = 1
#
#                 backtrack(k+1)
#
#                 for ii in range(N):
#                     is_used1[ii][j] = 0
#                     for jj in range(N):
#                         if i+j == ii + jj:
#                             is_used2[ii][jj] = 0
#                         if i+j + 2*(ii-i) == ii + jj:
#                             is_used3[ii][jj] = 0
#
#                 arr[i][j] = 0
#         return
#
#
#
# N = int(input())
# arr = [[0]*N for _ in range(N)]
# is_used1 = [[0]*N for _ in range(N)]
# is_used2 = [[0]*N for _ in range(N)]
# is_used3 = [[0]*N for _ in range(N)]
# is_used4 = [[0]*N for _ in range(N)]
# backtrack(0)
# print(cnt)

# https://blog.encrypted.gg/945 참고하여 변형

cnt = 0
def backtrack(x):
    global cnt
    if x == N:
        cnt += 1
        return

    for y in range(N):
        if is_used1[y] or is_used2[x+y] or is_used3[x-y+N-1]:
            continue
        is_used1[y] = 1
        is_used2[x+y] = 1
        is_used3[x-y+N-1] = 1
        backtrack(x+1)
        is_used1[y] = 0
        is_used2[x + y] = 0
        is_used3[x - y + N - 1] = 0

N = int(input())
is_used1 = [0 for _ in range(N)]
is_used2 = [0 for _ in range(2*N)]
is_used3 = [0 for _ in range(2*N)]
backtrack(0)
print(cnt)

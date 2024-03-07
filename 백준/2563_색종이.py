# 13 min
paper = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            # 어차피 100 by 100 정사각형이라 가로, 세로 반전되도 동일한 결과가 나옴.
            paper[i][j] = 1

# cnt = 0
# for i in range(100):
#     for j in range(100):
#         if paper[i][j] == 1:
#             cnt += 1
# print(cnt)

# 위 주석 처리한 코드 대신 사용 가능
print(sum(sum(line) for line in paper))
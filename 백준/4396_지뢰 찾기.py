n = int(input())
map = [input().split() for _ in range(n)]
visited = [input().split() for _ in range(n)]
result = [(['.'] * n) for _ in range(n)]
flag = False

def find():
    global flag

    for i in range(n):
        for j in range(n):
            if visited[i][0][j] == "x":
                if map[i][0][j] == "*":
                    flag = True
                # 00 01 02
                # 10 11 12
                # 20 21 22

                cnt = 0
                # ^, >, v, <
                if not i-1 < 0:
                    if map[i-1][0][j] == "*":
                        cnt += 1
                if not j+1 >= n:
                    if map[i][0][j+1] == "*":
                        cnt += 1
                if not i+1 >= n:
                    if map[i+1][0][j] == "*":
                        cnt += 1
                if not j-1 < 0:
                    if map[i][0][j-1] == "*":
                        cnt += 1

                # 대각
                if not i-1 < 0 and not j-1 < 0:
                    if map[i-1][0][j-1] == "*":
                        cnt += 1
                if not i-1 < 0 and not j+1 >= n:
                    if map[i-1][0][j+1] == "*":
                        cnt += 1
                if not i+1 >= n and not j+1 >= n:
                    if map[i+1][0][j+1] == "*":
                        cnt += 1
                if not i+1 >= n and not j-1 < 0:
                    if map[i+1][0][j-1] == "*":
                        cnt += 1
                result[i][j] = str(cnt)
find()

for i in range(n):
    for j in range(n):
        if flag and map[i][0][j] == "*":
            result[i][j] = "*"

for res in result:
    print(''.join(res))


# 2
# *.
# .*
# ..
# .x
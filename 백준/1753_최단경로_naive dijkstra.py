# 30 min, naive dijkstra -> 시간초과
# 0 < 모든 가중치 <= 10

V, E = list(map(int, input().split()))
start = int(input())

arr = []
res = [float('inf') for _ in range(V)]  # d
is_visited = [0 for _ in range(V)]      # fix

for i in range(E):
    arr.append(list(map(int, input().split())))

is_visited[start-1] = 1
res[start-1] = 0

while 0 in is_visited:
    mn = float('inf')
    to = 0
    for i in range(E):
        u, v, x = arr[i][0], arr[i][1], arr[i][2]

        if is_visited[v-1] == 1:
            continue

        if start == u:
            res[v-1] = min(res[v-1], x + res[start-1]) # 기존 가중치와 더해 연산 필요
            if x < mn:
                to = v
                mn = x

    is_visited[to-1] = 1
    start = to
    # print(to, mn, is_visited, res)

for i in range(V):
    if res[i] == float('inf'):
        print("INF")
    else:
        print(res[i])
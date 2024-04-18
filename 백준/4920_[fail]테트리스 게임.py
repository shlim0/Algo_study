# 34min - 25% 틀림
# 42min - 25% runtime error (입출력 수정)
# 44min - 입출력 힌트보고 바꿨으니 25% 틀림
# 1h - ㄱㄴ랑 ㅡㄱ reverse 있는거 찾았으나 25% 틀림
# 대회 테케랑 풀이(https://blog.naver.com/gywlsdl4889/221364030386)를 봤는데, 그냥 노가다하는 문제...

# 접근
# 5가지 테트리스 조각
# NxN 표를 90도 * 4번 회전시켜서 [0][0] ~ [N-1][N-1] 까지 순회
# -> 테트리스를 회전한다는 것은, NxN 표가 회전한다는 것과 동일하다고 생각함.

super_arr = []
while True:
    N = int(input())
    if N == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(N)]
    super_arr.append(arr)

for TC in range(1, len(super_arr) + 1):
    cnt = 0
    arr = super_arr.pop(0)
    N = len(arr)

    cmp = []


    for _ in range(4):
        arr = list(map(list, zip(*arr[::-1])))

        # 1. ㅡ
        for i in range(N):
            for j in range(N-3):
                cmp.append(sum(arr[i][j:j+4]))

        # 2. ㄱㄴ
        for i in range(N-1):
            for j in range(N-2):
                cmp.append(sum(arr[i][j:j+2]) + sum(arr[i+1][j+1:j+3]))

        # 2-1. ㄱㄴ reverse
        for i in range(N-1):
            for j in range(N-2):
                cmp.append(sum(arr[i][j+1:j+3]) + sum(arr[i+1][j:j+2]))

        # 3. ㅡㄱ
        for i in range(N-1):
            for j in range(N-2):
                cmp.append(sum(arr[i][j:j+3]) + arr[i+1][j+2])

        # 3-1. ㅡㄱ reverse
        for i in range(N-1):
            for j in range(N-2):
                cmp.append(sum(arr[i][j:j+3]) + arr[i+1][j])

        # 4. ㅜ
        for i in range(N-1):
            for j in range(N-2):
                cmp.append(sum(arr[i][j:j+3]) + arr[i+1][j+1])

        # 5. ㅁ
        for i in range(N-1):
            for j in range(N-1):
                cmp.append(sum(arr[i][j:j+2]) + sum(arr[i+1][j:j+2]))

    print(f'{TC}.', max(cmp))
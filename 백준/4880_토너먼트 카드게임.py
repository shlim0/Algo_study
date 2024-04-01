# 1. 절반씩 분할
    # 1-1. 최후 1인이 남는 순간 (3명 중 1명 부전승 고려)
# 2. 가위바위보 대결
# 3. 승자가 다른 승자와 대결 (반복)

# start, end는 갑이 아닌 인덱스임에 유의
def binary(start, end):
    if end - start == 0:
        return start
    else:
        l = binary(start , (start + end) // 2)
        r = binary((start + end) // 2 + 1, end)
        return rsp(l, r)

def rsp(l, r):
    if arr[l] == arr[r]:
        return l
    elif arr[l] - arr[r] == -1 or arr[l] - arr[r] == 2:
        return r
    else:
        return l

for tc in range(1, int(input()) + 1):
    _ = input()
    arr = list(map(int, input().split()))

    ans = binary(0, len(arr) - 1)
    print(f'#{tc} {ans + 1}')
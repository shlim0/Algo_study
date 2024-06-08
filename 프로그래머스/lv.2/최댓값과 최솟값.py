def solution(s):
    arr = list(map(int, s.split()))
    arr.sort()

    ans = f'{arr[0]} {arr[len(arr) - 1]}'

    return ans
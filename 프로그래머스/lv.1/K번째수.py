# 1 5 2 6 3 7 4
#   i     j
# -> 5 2 6 3
# -> sort
# -> 2 3 5 6
#        k

# 8.5 min
def solution(array, commands):
    ans = []

    for command in commands:
        arr = []
        for i in range(command[0]-1, command[1]):
            arr.append(array[i])
        arr.sort()
        ans.append(arr[command[2]-1])

    return ans

solution([1, 5, 2, 6, 3, 7, 4]	,[[2, 5, 3], [4, 4, 1], [1, 7, 3]]	)
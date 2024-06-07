def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            print(stack, numbers[stack[-1]], numbers[i])
            answer[stack.pop()] = numbers[i]
        print(i)
        stack.append(i)

    return answer
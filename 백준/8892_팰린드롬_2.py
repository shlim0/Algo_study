def find(k):
    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            combine = words[i] + words[j]

            if combine == combine[::-1]:
                print(combine)
                return

    print(0)


for tc in range(int(input())):
    k = int(input())
    words = [input() for _ in range(k)]

    find(k)
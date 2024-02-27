# 12min
# n = int(input())
#
# for _ in range(n):
#     data = list(input().split())
#     index = int(data[0]) - 1
#     pre, post = data[1].rsplit(data[1][index], 1)
#     print(pre + post)

for _ in range(int(input())):
    index, word = input().split()
    index = int(index)

    new_word = word[:index-1:1] + word[index::1]
    print(new_word)
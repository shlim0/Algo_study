import sys
input = sys.stdin.readline

# words = []
# for _ in range(int(input())):
#     words.append(input().rstrip())

words = [input().rstrip() for word in range(int(input()))]

words = list(set(words))
words.sort()
words.sort(key= lambda x: len(x))

for word in words:
    print(word)
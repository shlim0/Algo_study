from itertools import permutations

def find():
    for word1, word2 in permutations(words, 2):
        new_word = word1 + word2
        if new_word == new_word[::-1]:
            print(new_word)
            return

    print("0")

for tc in range(int(input())):
    k = int(input())
    words = [input() for _ in range(k)]

    find()
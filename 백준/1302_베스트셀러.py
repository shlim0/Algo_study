from collections import defaultdict

n = int(input())
books = defaultdict(int)

for i in range(n):
    book = input()
    books[book] += 1
#     if books.get(book, -1) == -1:
#         books[book] = 1
#     else:
#         books[book] += 1

sorted_books = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(sorted_books[0][0])
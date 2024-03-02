# 15 min
from collections import defaultdict

table = defaultdict(str)

for tc in range(int(input())):
    name, status = input().split()
    table[name] = status

sorted_table = sorted(table.items(), reverse=True)

for i in sorted_table:
    if i[1] == "enter":
        print(i[0])
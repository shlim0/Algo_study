# 15 min
from collections import defaultdict

table = defaultdict(str)

for tc in range(int(input())):
    name, status = input().split()
    table[name] = status

sorted_table = sorted((name for name in table if table[name] == "enter"), reverse=True)

for name in sorted_table:
    print(name)
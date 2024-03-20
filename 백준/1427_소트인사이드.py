# 15 min
my_str = input()
new_str = sorted(my_str, reverse=True)
ans = str()
for now in new_str:
    ans += now
print(ans)
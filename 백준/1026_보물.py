n = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
c = 0
for i in range(len(a)):
    c += a[i] * b[i]

print(c)
n = int(input())
data = list(map(int, input().split()))
first, last, highest = 0, 0, 0

def check():
    global first, last, highest

    if highest < last - first:
        highest = last - first
    first, last = 0, 0


for j in range(len(data) - 1):
    if data[j] < data[j+1]:
        if first == 0:
            first = data[j]
        if j + 1 == len(data) - 1:
            last = data[j+1]
            check()
    elif first != 0:
        last = data[j]
        check()

if highest:
    print(highest)
else:
    print("0")

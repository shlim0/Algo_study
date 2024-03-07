timetable = [list(map(int, input().split())) for _ in range(int(input()))]
timetable.sort(key=lambda x: (x[1], x[0]))
s, e, cnt = 0, 0, 0

for i, j in timetable:
    if i >= e:
        s, e = i, j
        cnt += 1

print(cnt)
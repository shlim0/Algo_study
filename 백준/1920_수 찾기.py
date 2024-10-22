# 15 min
import sys
input = sys.stdin.readline

def binary(target, l, r):
    global A

    if l > r:
        print(0)
        return

    mid = A[(l + r) // 2]
    if target == mid:
        print(1)
        return
    elif target < mid:
        binary(target, l, (l+r) // 2 -1)
    elif target > mid:
        binary(target, (l+r) // 2 + 1, r)

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for element in B:
    binary(element, 0, len(A)-1)

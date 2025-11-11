import sys

def backtracking(k):
    global res, v

    if k != 0 and v == s:
        res += 1

    for i in range(k, n):
        v += values[i]
        backtracking(i + 1)
        v -= values[i]

n, s = map(int, sys.stdin.readline().split())
values = list(map(int, sys.stdin.readline().split()))

arr = []

v = 0
res = 0

backtracking(0)

print(res)
import sys


def backtracking():
    if len(arr) == m:
        print(*arr)
        return

    last = 0

    for i in range(n):
        if last != values[i]:
            arr.append(values[i])
            last = values[i]

            backtracking()

            arr.pop()

n, m = map(int, sys.stdin.readline().split())
values = list(map(int, sys.stdin.readline().split()))

values.sort()

arr = []

backtracking()

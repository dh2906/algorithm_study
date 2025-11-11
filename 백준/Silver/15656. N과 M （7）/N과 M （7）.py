import sys


def backtracking():
    if len(arr) == m:
        print(*arr)
        return

    for item in values:
        arr.append(item)
        backtracking()
        arr.pop()


n, m = map(int, sys.stdin.readline().split())
values = list(map(int, sys.stdin.readline().split()))

values.sort()

arr = []

backtracking()

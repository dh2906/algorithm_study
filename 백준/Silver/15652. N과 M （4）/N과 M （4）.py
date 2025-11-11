import sys

def backtracking(k):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(k, n + 1):
            arr.append(i)
            backtracking(i)
            arr.pop()

n, m = map(int, sys.stdin.readline().split())
arr = []

backtracking(1)
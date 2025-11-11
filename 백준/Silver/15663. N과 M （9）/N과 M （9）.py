import sys


def backtracking():
    if len(arr) == m:
        print(*arr)
        return

    last = 0

    for i in range(n):
        if not visited[i] and last != values[i]:
            arr.append(values[i])
            visited[i] = True
            last = values[i]

            backtracking()

            arr.pop()
            visited[i] = False

n, m = map(int, sys.stdin.readline().split())
values = list(map(int, sys.stdin.readline().split()))

values.sort()

arr = []
visited = [False for _ in range(n + 1)]


backtracking()

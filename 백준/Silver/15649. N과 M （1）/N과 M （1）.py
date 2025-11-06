import sys

def backtracking(k):
    if k == m:
        print(*arr)
        return

    for j in range(1, n + 1):
        if not visited[j]:
            arr.append(j)
            visited[j] = True
            backtracking(k + 1)
            visited[j] = False
            arr.pop()

n, m = map(int, sys.stdin.readline().split())

arr = []
visited = [False] * 11

backtracking(0)
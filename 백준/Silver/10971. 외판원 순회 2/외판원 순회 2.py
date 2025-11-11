import sys

def backtracking(k, start, cur, val):
    if k == n and w[cur][start] != 0:
        res.append(val + w[cur][start])

    for i in range(n):
        if not visited[i] and w[cur][i] != 0:
            visited[i] = True
            backtracking(k + 1, start, i, val + w[cur][i])
            visited[i] = False

n = int(sys.stdin.readline())

visited = [False for _ in range(n)]
w = []
res = []

for _ in range(n):
    w.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    visited[i] = True
    backtracking(1, i, i, 0)
    visited[i] = False

print(min(res))

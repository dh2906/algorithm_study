import sys

n = int(sys.stdin.readline())

graph = {}

for i in range(1, n + 1):
    graph[i] = []

for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

s = [1]

while s:
    c = s.pop()
    visited[c] = True

    for next in graph[c]:
        if not visited[next]:
            visited[next] = True
            s.append(next)
            parent[next] = c

for i in range(2, n + 1):
    print(parent[i])
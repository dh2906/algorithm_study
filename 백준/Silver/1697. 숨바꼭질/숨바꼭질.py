import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

queue = deque()
visited = [False for _ in range(100001)]

queue.append((n, 0))
visited[n] = True

while queue:
    pos, cnt = queue.popleft()

    dx = [-1, 1, pos]

    if pos == k:
        print(cnt)
        break

    for i in range(3):
        nx = pos + dx[i]

        if 0 <= nx <= 100000 and not visited[nx]:
            visited[nx] = True
            queue.append((nx, cnt + 1))
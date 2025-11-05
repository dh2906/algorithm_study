import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

board = []

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
queue = deque()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

queue.append((0, 0, 0))
visited[0][0][0] = 1

flag = False

while queue:
    y, x, broken = queue.popleft()

    if y == n - 1 and x == m - 1:
        print(visited[y][x][broken])
        flag = True
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == 1 and visited[ny][nx][1] == 0 and broken == 0:
                visited[ny][nx][1] = visited[y][x][0] + 1
                queue.append((ny, nx, 1))

            elif board[ny][nx] == 0 and visited[ny][nx][broken] == 0:
                visited[ny][nx][broken] = visited[y][x][broken] + 1
                queue.append((ny, nx, broken))

if not flag:
    print(-1)
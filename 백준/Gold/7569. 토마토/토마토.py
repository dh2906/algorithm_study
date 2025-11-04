import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())

board = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

dz = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dx = [-1, 1, 0, 0, 0, 0]

queue = deque()

res = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1:
                queue.append((i, j, k))

while queue:
    z, y, x = queue.popleft()

    for i in range(6):
        nz = z + dz[i]
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and board[nz][ny][nx] == 0:
            queue.append((nz, ny, nx))
            board[nz][ny][nx] = board[z][y][x] + 1

for i in board:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()

            res = max(res, k)

print(res - 1)
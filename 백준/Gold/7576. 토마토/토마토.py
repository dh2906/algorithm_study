import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

board = []

queue = deque()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

res = 0

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))

while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 0:
            queue.append((ny, nx))
            board[ny][nx] = board[y][x] + 1

for row in board:
    for item in row:
        if item == 0:
            print(-1)
            exit()

    res = max(res, max(row))

print(res - 1)
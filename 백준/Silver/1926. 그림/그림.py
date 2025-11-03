import sys
from collections import deque

queue = deque()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    cnt = 0
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()
        cnt += 1

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1:
                queue.append((ny, nx))
                board[ny][nx] = 0

    return cnt

n, m = map(int, sys.stdin.readline().split())

board = []
res = [0, 0]

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            board[i][j] = 0
            res[0] += 1
            res[1] = max(res[1], bfs(i, j))

print(res[0])
print(res[1])
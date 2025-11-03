import sys
from collections import deque

def bfs(y, x):
    queue.append((y, x))
    visited[y][x] = True

    while queue:
        (y, x) = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and board[y][x] == board[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))

def getNumOfZone():
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)
                cnt += 1

    return cnt

n = int(sys.stdin.readline())

board = []
queue = deque()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

visited = [[False for _ in range(n)] for _ in range(n)]
a = getNumOfZone()

for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            board[i][j] = 'R'

visited = [[False for _ in range(n)] for _ in range(n)]
b = getNumOfZone()

print(a, b)
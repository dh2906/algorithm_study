import sys
from collections import deque

def burn():
    for _ in range(len(f_queue)):
        y, x = f_queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < r and 0 <= nx < c and board[ny][nx] == '.':
                f_queue.append((ny, nx))
                board[ny][nx] = 'F'

def move():
    flag = False

    for _ in range(len(p_queue)):
        y, x = p_queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                return visited[y][x]

            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx] and board[ny][nx] == '.':
                flag = True
                p_queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    if not flag:
        return 'IMPOSSIBLE'

r, c = map(int, sys.stdin.readline().split())

board = []
visited = [[0 for _ in range(c)] for _ in range(r)]

p_queue = deque()
f_queue = deque()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

res = 0

for _ in range(r):
    board.append(list(sys.stdin.readline()))

for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            p_queue.append((i, j))
            board[i][j] = '.'
            visited[i][j] = 1

        if board[i][j] == 'F':
            f_queue.append((i, j))

while True:
    burn()
    res = move()

    if res:
        print(res)
        break
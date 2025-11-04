import sys
from collections import deque


def burn():
    for _ in range(len(f_queue)):
        y, x = f_queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < h and 0 <= nx < w and board[ny][nx] == '.':
                f_queue.append((ny, nx))
                board[ny][nx] = '*'

def move():
    flag = False

    for _ in range(len(p_queue)):
        y, x = p_queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                return visited[y][x]

            if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx] and board[ny][nx] == '.':
                flag = True
                p_queue.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    if not flag:
        return 'IMPOSSIBLE'

t = int(sys.stdin.readline())

for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())

    board = []
    visited = [[0 for _ in range(w)] for _ in range(h)]

    p_queue = deque()
    f_queue = deque()

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    res = 0

    for _ in range(h):
        board.append(list(sys.stdin.readline()))

    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                p_queue.append((i, j))
                visited[i][j] = 1

            if board[i][j] == '*':
                f_queue.append((i, j))

    while True:
        burn()
        res = move()

        if res:
            print(res)
            break
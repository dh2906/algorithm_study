import sys
from collections import deque

n = int(sys.stdin.readline())

board = []
visited = [[False for _ in range(n)] for _ in range(n)]
queue = deque()

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

res = []
total = 0

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

for i in range(n):
    for j in range(n):

        if board[i][j] == 1 and not visited[i][j]:
            queue.append((i, j))
            visited[i][j] = True
            cnt = 0

            while queue:
                y, x = queue.popleft()
                cnt += 1

                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and board[ny][nx] == 1:
                        queue.append((ny, nx))
                        visited[ny][nx] = True

            res.append(cnt)
            total += 1

res.sort()

print(total)

for item in res:
    print(item)
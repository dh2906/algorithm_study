import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())

    queue = deque()
    board = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    cnt = 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())

        board[y][x] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    y, x = queue.popleft()

                    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        ny = y + dy
                        nx = x + dx

                        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and board[ny][nx] == 1:
                            queue.append((ny, nx))
                            visited[ny][nx] = True

                cnt += 1

    print(cnt)
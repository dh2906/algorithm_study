from collections import deque

N, M = map(int, input().split())
board = []
res = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    q.append((y, x))

    visited[y][x] = True

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue

            if board[ny][nx] == 0:
                water[y][x] += 1

            if board[ny][nx] != 0 and visited[ny][nx] == False:
                q.append((ny, nx))
                visited[ny][nx] = True

for i in range(N):
    board.append(list(map(int, input().split())))

while True:
    ice_cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    water = [[0 for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and board[i][j] != 0:
                bfs(i, j)
                ice_cnt += 1

            if ice_cnt >= 2:
                print(res)
                exit()

    if ice_cnt == 0:
        print(0)
        break

    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                board[i][j] -= water[i][j]

            if board[i][j] < 0:
                board[i][j] = 0

    res += 1
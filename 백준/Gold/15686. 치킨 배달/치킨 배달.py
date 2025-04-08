from itertools import combinations

INF = 1e9
n, m = map(int, input().split())
board = []
chicken_pos = []
house_pos = []
res = []

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken_pos.append((i, j))

        elif board[i][j] == 1:
            house_pos.append((i, j))

for combination in combinations(chicken_pos, m):
    dist = [[INF] * n for _ in range(n)]

    for h in house_pos:
        for i in range(m):
            dist[h[0]][h[1]] = min(dist[h[0]][h[1]], abs(h[0] - combination[i][0]) + abs(h[1] - combination[i][1]))

    tmp = 0

    for i in range(n):
        for j in range(n):
            if dist[i][j] != INF:
                tmp = tmp + dist[i][j]

    res.append(tmp)

print(min(res))
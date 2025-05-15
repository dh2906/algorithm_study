def turn(direction, x, y):
    global dice

    # 동쪽
    if direction == 1:
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    # 서쪽
    elif direction == 2:
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    # 북쪽
    elif direction == 3:
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    # 남쪽
    else:
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

n, m, x, y, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
op = list(map(int, input().split()))
dice = [0 for _ in range(6)]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for o in op:
    nx = x + dx[o]
    ny = y + dy[o]

    if 0 <= nx < n and 0 <= ny < m:
        turn(o, nx, ny)

        if data[nx][ny] == 0:
            data[nx][ny] = dice[-1]

        else:
            dice[-1] = data[nx][ny]
            data[nx][ny] = 0

        print(dice[0])
        
        x, y = nx, ny
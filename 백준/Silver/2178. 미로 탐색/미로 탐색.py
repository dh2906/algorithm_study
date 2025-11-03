from collections import deque

n, m = map(int, input().split())
arr = []
queue = deque()

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(n):
    arr.append(list(map(int, input())))

queue.append((0, 0))

while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= n or nx < 0 or nx >= m:
            continue
        
        if arr[ny][nx] == 1:
            arr[ny][nx] = arr[y][x] + 1
            queue.append((ny, nx))

print(arr[n-1][m-1])

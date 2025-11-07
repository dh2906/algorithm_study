import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())

floor = [0 for _ in range(f + 1)]
queue = deque()

queue.append(s)
floor[s] = 1

while queue:
    x = queue.popleft()

    if x == g:
        print(floor[x] - 1)
        exit()

    for dx in [u, -d]:
        nx = x + dx

        if 1 <= nx <= f and floor[nx] == 0:
            queue.append(nx)
            floor[nx] = floor[x] + 1

print('use the stairs')
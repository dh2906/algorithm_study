import sys
from collections import deque

size = int(sys.stdin.readline())
queue = deque()

while True:
    id = int(sys.stdin.readline())

    if id == -1:
        break

    if id != 0:
        if len(queue) < size:
            queue.append(id)

    else:
        queue.popleft()

print(*queue) if queue else print("empty")
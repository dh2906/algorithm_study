import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()

    op = cmd[0]
    v = cmd[1] if len(cmd) > 1 else None

    if op == 'push':
        queue.append(v)

    elif op == 'pop':
        sys.stdout.write(f"{queue.popleft() if queue else -1}\n")

    elif op == 'size':
        sys.stdout.write(f"{len(queue)}\n")

    elif op == 'empty':
        sys.stdout.write(f"{0 if queue else 1}\n")

    elif op == 'front':
        sys.stdout.write(f"{queue[0] if queue else -1}\n")

    else:
        sys.stdout.write(f"{queue[-1] if queue else -1}\n")
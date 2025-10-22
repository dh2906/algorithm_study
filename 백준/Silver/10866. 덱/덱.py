import sys
from collections import deque

n = int(sys.stdin.readline())

dq = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()

    op = cmd[0]
    v = int(cmd[1]) if len(cmd) > 1 else None

    if op == 'push_front':
        dq.appendleft(v)

    elif op == 'push_back':
        dq.append(v)

    elif op == 'pop_front':
        sys.stdout.write(f"{dq.popleft() if dq else -1}\n")

    elif op == 'pop_back':
        sys.stdout.write(f"{dq.pop() if dq else -1}\n")

    elif op == 'size':
        sys.stdout.write(f"{len(dq)}\n")

    elif op == 'empty':
        sys.stdout.write(f"{0 if dq else 1}\n")

    elif op == 'front':
        sys.stdout.write(f"{dq[0] if dq else -1}\n")

    else:
        sys.stdout.write(f"{dq[-1] if dq else -1}\n")
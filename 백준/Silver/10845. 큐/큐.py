import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    cmd = sys.stdin.readline().split()

    op = cmd[0]
    v = cmd[1] if len(cmd) > 1 else None

    if op == 'push':
        queue.append(v)

    elif op == 'pop':
        print(queue.pop(0) if queue else -1)

    elif op == 'size':
        print(len(queue))

    elif op == 'empty':
        print(0 if queue else 1)

    elif op == 'front':
        print(queue[0] if queue else -1)

    else:
        print(queue[-1] if queue else -1)
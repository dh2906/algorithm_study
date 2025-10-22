import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    cmd = sys.stdin.readline().split()

    op = cmd[0]
    v = int(cmd[1]) if len(cmd) > 1 else None

    if op == 'push':
        stack.append(v)

    elif op == 'pop':
        sys.stdout.write(f"{stack.pop() if stack else -1}\n")

    elif op == 'size':
        sys.stdout.write(f"{len(stack)}\n")

    elif op == 'empty':
        sys.stdout.write(f"{0 if stack else 1}\n")

    else:
        sys.stdout.write(f"{stack[-1] if stack else -1}\n")
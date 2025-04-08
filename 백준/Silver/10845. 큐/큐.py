from collections import deque
import sys

N = int(input())
q = deque()

for i in range(N):
    op = sys.stdin.readline().strip().split()

    if op[0] == 'push':
        q.append(op[1])

    elif op[0] == 'pop':
        print(q.popleft() if q else -1)

    elif op[0] == 'size':
        print(len(q))

    elif op[0] == 'empty':
        print(0 if q else 1)

    elif op[0] == 'front':
        print(q[0] if q else -1)

    elif op[0] == 'back':
        print(q[-1] if q else -1)
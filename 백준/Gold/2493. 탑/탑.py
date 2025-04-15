import sys

N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
stack = []
res = [0 for _ in range(N)]

for i in range(N):
    while stack:
        if tower[i] <= stack[-1][0]:
            res[i] = stack[-1][1]
            break

        else:
            stack.pop()

    stack.append((tower[i], i + 1))

print(*res)
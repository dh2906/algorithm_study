import sys

k = int(sys.stdin.readline())
stack = []

for _ in range(k):
    n = int(sys.stdin.readline())

    stack.append(n) if n != 0 else stack.pop()

print(sum(stack))
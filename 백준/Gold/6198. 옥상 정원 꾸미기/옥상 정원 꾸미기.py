import sys

n = int(sys.stdin.readline())

heights = []
s = []

res = 0

for _ in range(n):
    heights.append(int(sys.stdin.readline()))

for h in heights:
    while s and s[-1] <= h:
        s.pop()

    res += len(s)
    s.append(h)

print(res)
import sys

n, k = map(int, sys.stdin.readline().split())

values = []

for _ in range(n):
    values.append(int(sys.stdin.readline()))

values.sort(reverse = True)

res = 0

for v in values:
    if k >= v:
        res += (k // v)
        k %= v

print(res)
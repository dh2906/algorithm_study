import sys

n = int(sys.stdin.readline())

v = []

for _ in range(n):
    v.append(float(sys.stdin.readline()))

for i in range(1, n):
    v[i] = max(v[i], v[i] * v[i - 1])

print(f'%.3f' % max(v))
import sys

n = int(sys.stdin.readline())

weights = []

for _ in range(n):
    weights.append(int(sys.stdin.readline()))

weights.sort(reverse = True)

res = []

for i in range(n):
    res.append(weights[i] * (i + 1))

print(max(res))
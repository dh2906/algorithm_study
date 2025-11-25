import sys

n = int(sys.stdin.readline())

p = list(map(int, sys.stdin.readline().split()))

p.sort()

for i in range(1, len(p)):
    p[i] += p[i - 1]

print(sum(p))
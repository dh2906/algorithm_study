import sys

n, m = map(int, sys.stdin.readline().split())

dict = {}

for i in range(1, n + 1):
    name = sys.stdin.readline().strip()

    dict[str(i)] = name
    dict[name] = i

for i in range(m):
    s = sys.stdin.readline().strip()

    print(dict[s])
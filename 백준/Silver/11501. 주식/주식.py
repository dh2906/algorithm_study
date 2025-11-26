import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    cost = list(map(int, sys.stdin.readline().split()))

    res = 0
    max_cost = 0

    for c in cost[::-1]:
        if max_cost <= c:
            max_cost = c

        else:
            res += max_cost - c

    print(res)
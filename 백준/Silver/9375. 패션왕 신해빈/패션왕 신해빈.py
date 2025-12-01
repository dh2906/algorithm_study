import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    dict = {}
    res = 1

    for _ in range(n):
        name, type = sys.stdin.readline().split()

        if type not in dict:
            dict[type] = 1

        else:
            dict[type] += 1

    for item in dict.values():
        res *= (item + 1)

    print(res - 1)
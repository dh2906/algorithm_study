import sys

n = int(sys.stdin.readline())

lst = {}

for _ in range(n):
    name, status = sys.stdin.readline().split()

    if status == 'enter':
        lst[name] = 1

    else:
        lst.pop(name)

for name in sorted(lst, reverse = True):
    print(name)
import sys

lst = [(i + 1) for i in range(20)]

for _ in range(10):
    a, b = map(int, sys.stdin.readline().split())

    a -= 1

    lst[a:b] = lst[a:b][::-1]

print(*lst)
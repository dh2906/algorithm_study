import sys

n, m = map(int, sys.stdin.readline().split())

dict = {}

for _ in range(n):
    addr, pw = sys.stdin.readline().split()

    dict[addr] = pw

for _ in range(m):
    addr = sys.stdin.readline().strip()

    print(dict[addr])
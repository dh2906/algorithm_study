import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(" " * (n - 1 - i) + "*" * ((i * 2) + 1))

for i in range(n - 1):
    print(" " * (i + 1) + "*" * (2 * (n - i - 1) - 1))
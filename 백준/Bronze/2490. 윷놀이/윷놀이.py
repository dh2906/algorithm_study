import sys

result = ["D", "C", "B", "A", "E"]

for i in range(3):
    val = list(map(int, sys.stdin.readline().split()))
    print(result[sum(val)])
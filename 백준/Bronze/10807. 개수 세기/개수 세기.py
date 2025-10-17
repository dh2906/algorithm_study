import sys

n = int(sys.stdin.readline())

dic = {i: 0 for i in range(-100, 101)}

values = list(map(int, sys.stdin.readline().split()))

for v in values:
    dic[v] += 1

target = int(sys.stdin.readline())

print(dic[target])
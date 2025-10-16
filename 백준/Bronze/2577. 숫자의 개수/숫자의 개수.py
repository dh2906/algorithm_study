import sys

res = {i: 0 for i in range(10)}

a = int(input())
b = int(input())
c = int(input())

mul = a * b * c

for s in str(mul):
    res[int(s)] += 1

for i in range(10):
    print(res[i])
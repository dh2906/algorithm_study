import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

s = sorted(set(x))

dict = {}

for i in range(len(s)):
    dict[s[i]] = i

for item in x:
    print(dict[item], end = " ")
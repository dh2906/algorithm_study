import sys

n, m = map(int, sys.stdin.readline().split())

dict = {}

for i in range(m):
    stu = sys.stdin.readline().strip()

    dict[stu] = i

res = sorted(dict.items(), key = lambda item:item[1])

for i in range(min(n, len(dict))):
    print(res[i][0])
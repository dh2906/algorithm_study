import sys

str = sys.stdin.readline().split('-')

lst = []

for i in range(len(str)):
    token = str[i].split('+')

    tmp = 0

    for t in token:
        tmp += int(t)

    lst.append(tmp)

res = lst[0]

for n in lst[1::]:
    res -= n

print(res)
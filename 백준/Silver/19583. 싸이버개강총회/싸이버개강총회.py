import sys

s, e, q = sys.stdin.readline().split()

dict = {}
res = {}

for line in sys.stdin:
    time, nickname = line.split()
    if time <= s:
        dict[nickname] = time

    elif e <= time <= q:
        if nickname in dict:
            res[nickname] = 1

print(len(res))
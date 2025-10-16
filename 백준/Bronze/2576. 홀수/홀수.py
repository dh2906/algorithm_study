import sys

odd = []

for i in range(7):
    val = int(sys.stdin.readline())

    if val % 2:
        odd.append(val)

if len(odd) != 0:
    print(sum(odd))
    print(min(odd))

else:
    print(-1)
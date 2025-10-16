import sys

lst = []

for _ in range(9):
    lst.append(int(sys.stdin.readline()))

lst.sort()

for i in range(8):
    for j in range(i+1, 9):
        if lst[i] + lst[j] == sum(lst) - 100:
            for k in range(9):
                if k == i or k == j:
                    continue

                print(lst[k])

            sys.exit()

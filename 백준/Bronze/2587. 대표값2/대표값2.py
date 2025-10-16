import sys

lst = []

for i in range(5):
    lst.append(int(sys.stdin.readline()))

lst.sort()

print(sum(lst) // len(lst))
print(lst[2])
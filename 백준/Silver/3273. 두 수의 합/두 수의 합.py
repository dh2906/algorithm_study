import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())

res = 0

lst.sort()

start = 0
end = len(lst) - 1

while start < end:
    if lst[start] + lst[end] > target:
        end -= 1

    elif lst[start] + lst[end] < target:
        start += 1

    else:
        res += 1
        start += 1

print(res)
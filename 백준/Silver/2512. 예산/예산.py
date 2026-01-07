import sys

n = int(sys.stdin.readline())
loc = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

start = 1
end = max(loc)

while start <= end:
    tot = 0
    mid = (start + end) // 2

    for l in loc:
        if mid > l:
            tot += l

        else:
            tot += mid

    if tot <= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)
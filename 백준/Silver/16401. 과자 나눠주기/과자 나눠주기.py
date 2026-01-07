import sys

m, n = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

start = 1
end = max(l)

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for item in l:
        cnt += (item // mid)

    if cnt >= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)
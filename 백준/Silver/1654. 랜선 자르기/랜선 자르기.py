import sys

n, k = map(int, sys.stdin.readline().split())

lan = []

for _ in range(n):
    lan.append(int(sys.stdin.readline()))

start = 1
end = max(lan)
cnt = 0

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for item in lan:
        cnt += (item // mid)

    if cnt >= k:
        start = mid + 1

    else:
        end = mid - 1

print(end)
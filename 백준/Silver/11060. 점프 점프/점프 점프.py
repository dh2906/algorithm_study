from collections import deque
import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

dp = [-1 for _ in range(n)]
dp[0] = 0

q = deque()

q.append(0)

while q:
    v = q.popleft()

    if v == n - 1:
        break

    for i in range(1, a[v] + 1):
        if v + i < n and dp[v + i] == -1:
            dp[v + i] = dp[v] + 1
            q.append(v + i)

print(dp[n - 1])
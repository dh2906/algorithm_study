import sys

n = int(sys.stdin.readline())

T = []
P = []

for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())

    T.append(t)
    P.append(p)

dp = [0 for _ in range(n + 1)]

for i in range(n):
    dp[i + 1] = max(dp[i], dp[i + 1])

    if T[i] + i <= n:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

print(max(dp))
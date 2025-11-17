import sys

n = int(sys.stdin.readline())

steps = [0 for _ in range(301)]
dp = [[0 for _ in range(3)] for _ in range(301)]

for i in range(1, n + 1):
    steps[i] = int(sys.stdin.readline())

dp[1][1] = steps[1]
dp[1][2] = 0
dp[2][1] = steps[2]
dp[2][2] = steps[1] + steps[2]

for i in range(3, n + 1):
    dp[i][1] = max(dp[i - 2][2], dp[i - 2][1]) + steps[i]
    dp[i][2] = dp[i - 1][1] + steps[i]

print(max(dp[n]))
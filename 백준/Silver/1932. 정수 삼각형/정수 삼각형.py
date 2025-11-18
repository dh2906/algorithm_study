import sys

n = int(sys.stdin.readline())

values = []

for _ in range(n):
    values.append(list(map(int, sys.stdin.readline().split())))

dp = values

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + values[i][j]

        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + values[i][j]

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + values[i][j]

print(max(dp[n - 1]))
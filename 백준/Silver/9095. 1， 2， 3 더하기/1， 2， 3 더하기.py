import sys

t = int(sys.stdin.readline())

numbers = []

for _ in range(t):
    numbers.append(int(sys.stdin.readline()))

m = max(numbers)

dp = [0 for _ in range(m + 1)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, m + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for n in numbers:
    print(dp[n])
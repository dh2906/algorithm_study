import sys

n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]

for i in range(n - 1, -1, -1):
    for j in range(i, -1, -1):
        if numbers[i] < numbers[j]:
            dp[j] = max(dp[j], dp[i] + 1)

print(max(dp))
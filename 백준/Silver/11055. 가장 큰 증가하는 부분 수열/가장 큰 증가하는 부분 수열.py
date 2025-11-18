import sys

n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

dp = [n for n in numbers]

for i in range(n):
    for j in range(i, n):
        if numbers[i] < numbers[j]:
            dp[j] = max(dp[j], dp[i] + numbers[j])

print(max(dp))
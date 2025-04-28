N = int(input())
dp = [0 for _ in range(N + 1)] # dp[n] = n을 1로 만드는 데 최소한의 연산 수
trace = [0 for _ in range(N + 1)] # trace[n] = n을 만드는데 최소 연산의 수를 가진 값
idx = N

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    trace[i] = i - 1

    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        trace[i] = i // 3

    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        trace[i] = i // 2

print(dp[N])
print(N, end = " ")
while idx != 1:
    print(trace[idx], end = " ")
    idx = trace[idx]
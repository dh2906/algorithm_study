import queue

INF = 10e9
N = int(input())
A = list(map(int, input().split()))
dp = [INF for _ in range(N)] # dp[N] -> N번째 칸에 도착하기 위한 최소 점프 수
visit = [False for _ in range(N)]

q = queue.Queue()

q.put(0)
dp[0] = 0

while not(q.empty()):
    i = q.get()
    visit[i] = True

    if i == N - 1:
        break

    m = min(N - i, A[i])

    for idx in range(m, 0, -1):
        next_idx = i + idx

        if next_idx < N and dp[i] + 1 < dp[next_idx] and not(visit[next_idx]):
            q.put(next_idx)
            dp[next_idx] = dp[i] + 1

print(-1 if dp[N-1] == INF else dp[N-1])
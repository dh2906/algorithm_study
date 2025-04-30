N, M = map(int, input().split())
A = list(map(int, input().split()))
cnt = [0 for _ in range(M)]
res = 0

for i in range(0, len(A)):
    if i != 0:
        A[i] += A[i-1]
        
    A[i] %= M
    cnt[A[i]] += 1

    if A[i] % M == 0:
        res += 1

for c in cnt:
    res += (c * (c - 1)) // 2

print(res)
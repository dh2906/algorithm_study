from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
m = int(input())
guess = list(map(int, input().split()))
n_cnt = [0 for _ in range(m)]

a.sort()

for i in range(len(n_cnt)):
    if bisect_right(a, guess[i]) - bisect_left(a, guess[i]) < 1:
        n_cnt[i] = 0

    else:
        n_cnt[i] = 1

for i in range(m):
    print(n_cnt[i])

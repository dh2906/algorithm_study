import sys

def backtracking(k, cnt, sour, bitter):
    if k == n:
        if cnt > 0:
            res.append(abs(sour - bitter))

        return

    backtracking(k + 1, cnt + 1, sour * taste[k][0], bitter + taste[k][1])
    backtracking(k + 1, cnt, sour, bitter)

n = int(sys.stdin.readline())

taste = []

for _ in range(n):
    taste.append(list(map(int, sys.stdin.readline().split())))

res = []

backtracking(0, 0, 1, 0)

print(min(res))

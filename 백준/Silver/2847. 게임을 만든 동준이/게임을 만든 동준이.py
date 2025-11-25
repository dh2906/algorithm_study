import sys

n = int(sys.stdin.readline())

score = []

for _ in range(n):
    score.append(int(sys.stdin.readline()))

res = 0

for i in range(len(score) - 2, -1, -1):
    if score[i] >= score[i + 1]:
        tmp = score[i]
        score[i] = score[i + 1] - 1
        res += tmp - score[i]

print(res)
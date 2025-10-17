import sys, math

n, k = map(int, sys.stdin.readline().split())
students = [[0 for _ in range(6)] for _ in range(2)]

res = 0

for i in range(n):
    s, y = map(int, sys.stdin.readline().split())
    students[s][y - 1] += 1

for i in range(2):
    for j in range(6):
        res += math.ceil(students[i][j] / k)

print(res)
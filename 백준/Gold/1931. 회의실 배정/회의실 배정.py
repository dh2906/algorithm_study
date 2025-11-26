n = int(input())
d = [[0 for _ in range(2)] for _ in range(n)]
cnt = 1
for i in range(n):
    d[i][0], d[i][1] = map(int, input().split())

d.sort(key = lambda x : (x[1], x[0]))

end_time = d[0][1]

for i in range(1, n):
    if d[i][0] >= end_time:
        cnt += 1
        end_time = d[i][1]

print(cnt)
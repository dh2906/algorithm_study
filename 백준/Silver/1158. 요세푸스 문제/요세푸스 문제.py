N, K = map(int, input().split())
circle = [(i + 1) for i in range(N)]
res = []
cur = 0

while circle:
        cur += K - 1
        cur %= len(circle)
        res.append(str(circle.pop(cur)))

print("<" + ", ".join(res)[:] + ">")
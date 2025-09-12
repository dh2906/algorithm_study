N = int(input())
balloons = [(i + 1) for i in range(N)]
values = list(map(int, input().split()))
cur = 0

res = [balloons.pop(cur)]
val = values.pop(cur)

while balloons:
    cur += val - 1 if val > 0 else val
    cur %= len(balloons)

    res.append(balloons.pop(cur))
    val = values.pop(cur)

print(*res)

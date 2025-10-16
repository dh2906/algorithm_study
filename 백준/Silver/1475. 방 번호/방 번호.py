import sys, math

cnt = {i: 0 for i in range(9)}

number = sys.stdin.readline().strip()

for ch in number:
    n = int(ch)
    if n == 9:
        cnt[6] += 1
    else:
        cnt[n] += 1

cnt[6] = math.ceil(cnt[6] / 2)

print(max(cnt.values()))

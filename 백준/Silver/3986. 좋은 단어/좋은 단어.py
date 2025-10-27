import sys

n = int(sys.stdin.readline())

res = 0

for _ in range(n):
    word = sys.stdin.readline().rstrip()

    s = []

    for w in word:
        if s and s[-1] == w:
            s.pop()

        else:
            s.append(w)

    if not s:
        res += 1

print(res)
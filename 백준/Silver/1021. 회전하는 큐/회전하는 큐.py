import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))

dq = deque([(i + 1) for i in range(n)])
res = 0

for target in targets:
    while True:
        if dq[0] == target:
            dq.popleft()
            break

        else:
            if dq.index(target) < (len(dq) // 2) + 1:
                t = dq.index(target)
                res += t
                dq.rotate(-t)

            else:
                t = len(dq) - dq.index(target)
                res += t
                dq.rotate(t)

print(res)
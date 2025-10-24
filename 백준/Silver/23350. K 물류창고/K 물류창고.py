import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

dq = deque()

counter = [0 for _ in range(m + 1)]
containers = [[] for _ in range(m + 1)]

current_priority = m
res = 0

for _ in range(n):
    dq.append(list((map(int, sys.stdin.readline().split()))))
    counter[dq[-1][0]] += 1

while dq:
    priority, weight = dq[0]

    if current_priority == priority:
        if containers[priority] and containers[priority][-1] < weight:
            temp = []

            while containers[priority] and containers[priority][-1] < weight:
                res += containers[priority][-1]
                temp.append(containers[priority].pop())

            res += weight + sum(temp)
            containers[priority].append(dq.popleft()[1])
            containers[priority] += temp[::-1]

        else:
            res += weight
            containers[priority].append(dq.popleft()[1])

        counter[priority] -= 1

        if counter[priority] == 0:
            current_priority -= 1

    else:
        res += weight
        dq.rotate(-1)

print(res)
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

    if current_priority == priority: # 가장 앞에 있는 컨테이너 우선순위가 낮은 경우 (먼저 적재해야 하는 경우)
        if containers[priority] and containers[priority][-1] < weight: # 이미 적재된 상태에서 새로 적재하려는 중량이 더 무거운 경우 -> 재배치
            temp = []

            while containers[priority] and containers[priority][-1] < weight: # 가벼운 컨테이너를 만나거나 빌 때까지 반복
                res += containers[priority][-1]
                temp.append(containers[priority].pop())

            res += weight + sum(temp)
            containers[priority].append(dq.popleft()[1])
            containers[priority] += temp[::-1]

        else: # 처음 적재하거나 적재하려는 중량이 더 가벼운 경우 -> 적재 가능
            res += weight
            containers[priority].append(dq.popleft()[1])

        counter[priority] -= 1

        if counter[priority] == 0:
            current_priority -= 1

    else:
        res += weight
        dq.rotate(-1)

print(res)
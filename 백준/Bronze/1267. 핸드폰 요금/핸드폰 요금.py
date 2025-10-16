import sys

y_cost = 0
m_cost = 0

n = int(sys.stdin.readline())
calls = list(map(int, sys.stdin.readline().split()))

for call in calls:
    y_cost += ((call // 30) + 1) * 10
    m_cost += ((call // 60) + 1) * 15

if y_cost > m_cost:
    print("M", m_cost)

elif y_cost < m_cost:
    print("Y", y_cost)

else:
    print("Y M", y_cost)
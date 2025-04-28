import sys

N = int(sys.stdin.readline())
ropes = []
weights = []

for i in range(N):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)

for i in range(len(ropes)):
    weights.append(ropes[i] * (i + 1))

print(max(weights))
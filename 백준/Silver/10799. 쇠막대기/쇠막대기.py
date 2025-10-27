import sys

brackets = sys.stdin.readline().rstrip()

s = []

cnt = 0
res = 0

for i in range(len(brackets)):
    if brackets[i] == '(':
        s.append(brackets[i])

    else:
        s.pop()

        if brackets[i-1] == '(':
            res += len(s)

        else:
            res += 1

print(res)
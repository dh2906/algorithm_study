import sys

n = int(sys.stdin.readline())
i = 1
stack = []
res = []

for _ in range(n):
    v = int(sys.stdin.readline())

    while i <= v:
        stack.append(i)
        i += 1
        res.append('+')

    if v == stack[-1]:
        stack.pop()
        res.append('-')

    else:
        print('NO')
        exit()

for item in res:
    sys.stdout.write(f"{item}\n")
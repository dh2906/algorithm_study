import sys

str = sys.stdin.readline().strip()

stack = []
res = ''
check = False

for s in str:
    if s == '<':
        check = True
        for _ in range(len(stack)):
            res += stack.pop()

    stack.append(s)

    if s == '>':
        check = False
        for _ in range(len(stack)):
            res += stack.pop(0)

    if s == ' ' and check == False:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            res += stack.pop()
        res += ' '

if stack:
    for _ in range(len(stack)):
        res += stack.pop()

print(res)

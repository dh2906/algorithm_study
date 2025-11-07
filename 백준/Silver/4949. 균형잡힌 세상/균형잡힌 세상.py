import sys

while True:
    str = sys.stdin.readline().rstrip()
    stack = []
    flag = False

    if str == '.':
        break

    for s in str:
        if s == '[' or s == '(':
            stack.append(s)

        elif s == ']' or s == ')':
            if not stack:
                flag = True
                break

            if (s == ']' and stack[-1] == '[') or (s == ')' and stack[-1] == '('):
                stack.pop()

            else:
                flag = True
                break

    if not flag and not stack:
        print('yes')

    else:
        print('no')
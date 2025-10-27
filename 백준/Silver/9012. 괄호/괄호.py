import sys

t = int(sys.stdin.readline())

for _ in range(t):
    brackets = sys.stdin.readline().strip()
    s = []
    flag = True

    for b in brackets:
        if b == '(':
            s.append(b)

        else:
            if len(s) != 0:
                s.pop()

            else:
                flag = False
                break

    print('YES' if flag and not s else 'NO')
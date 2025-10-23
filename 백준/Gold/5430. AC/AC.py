import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    lst = deque(sys.stdin.readline()[1:-2].split(','))

    if n == 0:
        lst = deque()

    r_cnt = 0
    flag = False

    for op in p:
        if op == 'R':
            r_cnt += 1

        elif op == 'D':
            if lst:
                if r_cnt % 2 == 0:
                    lst.popleft()

                else:
                    lst.pop()

            else:
                print('error')
                flag = True
                break

    if not flag:
        if r_cnt % 2 != 0:
            lst.reverse()
        
        print('[' + ','.join(lst) + ']')
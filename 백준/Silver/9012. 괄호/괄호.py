import sys

n = int(sys.stdin.readline())
str = ""

for i in range(n):
    str = sys.stdin.readline().strip()
    vps = []
    is_break = False
    
    for j in str:
        if j == '(':
            vps.append(1)

        else:
            if len(vps) > 0:
                vps.pop()

            else:
                print("NO")
                is_break = True
                break

    if is_break == True:
        continue

    else:
        if len(vps) == 0:
            print("YES")

        else:
            print("NO")

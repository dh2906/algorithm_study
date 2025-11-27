import sys

n = int(sys.stdin.readline())

dict = {}

res = 0

for _ in range(n):
    chat = sys.stdin.readline().strip()

    if chat == 'ENTER':
        dict = {}

    else:
        if chat not in dict:
            res += 1
            dict[chat] = 1

print(res)
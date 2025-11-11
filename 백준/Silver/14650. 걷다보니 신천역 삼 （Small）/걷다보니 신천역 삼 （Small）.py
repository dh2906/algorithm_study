import sys

def backtracking():
    global res, num

    if len(num) == n:
        if int(num) % 3 == 0:
            res += 1
            
        return

    for item in lst:
        if len(num) == 0 and item == "0":
            continue

        num += item
        backtracking()
        num = num[:-1]

n = int(sys.stdin.readline())

lst = ["0", "1", "2"]

num = ""
res = 0

backtracking()

print(res)

import sys

n, m = map(int, sys.stdin.readline().split())

group_dict = {}
member_dict = {}

for _ in range(n):
    group_name = sys.stdin.readline().strip()
    num = int(sys.stdin.readline())

    lst = []

    for _ in range(num):
        member_name = sys.stdin.readline().strip()

        member_dict[member_name] = group_name
        lst.append(member_name)

    lst.sort()
    group_dict[group_name] = lst

for _ in range(m):
    question = sys.stdin.readline().strip()
    type = int(sys.stdin.readline())

    if type == 0:
        answer = group_dict[question]

        for a in answer:
            print(a)

    else:
        print(member_dict[question])
import sys

res = 0

dict1 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
dict2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

for s in str1:
    dict1[s] += 1

for s in str2:
    dict2[s] += 1

for i in range(ord('a'), ord('z') + 1):
    s = chr(i)

    if dict1[s] != dict2[s]:
        res += abs(dict1[s] - dict2[s])

print(res)
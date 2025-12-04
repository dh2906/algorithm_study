import sys

str = sys.stdin.readline().strip()
target = sys.stdin.readline().strip()
result = 0

num = 0

while num <= len(str) - len(target) :
  if str[num : num + len(target)] == target :
    result += 1
    num += len(target)

  else :
    num += 1

print(result)
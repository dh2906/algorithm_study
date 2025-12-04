import sys

str = sys.stdin.readline().strip()
cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro_alpha:
    str = str.replace(i, '~')

print(len(str))

N, G = input().split()
N = int(N)
players = []
dict = {}
res = 0

for _ in range(N):
    players.append(input())

for i in players:
    dict[i] = True

length = len(dict)

if G == 'Y':
    res = length // 1

elif G == 'F':
    res = length // 2

else:
    res = length // 3

print(res)
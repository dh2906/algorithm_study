N = int(input())
M = int(input())
S = input()

P = "IOI" + "OI" * (N - 1)
res = 0

for i in range(len(S) - len(P) + 1):
    if S[i] == 'I' and S[i:i + len(P)] == P:
        res += 1

print(res)
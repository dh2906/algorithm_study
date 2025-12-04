import sys

n, m = map(int, sys.stdin.readline().split())

list = []
s = ''
dna = ['A', 'C', 'G', 'T']
res = 0

for i in range(n):
    data = sys.stdin.readline().strip()
    list.append(data)

for i in range(m):
    a_count, c_count, g_count, t_count = 0, 0, 0, 0

    for j in range(n):
        if list[j][i] == dna[0]:
            a_count += 1
        elif list[j][i] == dna[1]:
            c_count += 1
        elif list[j][i] == dna[2]:
            g_count += 1
        elif list[j][i] == dna[3]:
            t_count += 1

    count_list = [a_count, c_count, g_count, t_count]
    selected_dna = dna[count_list.index(max(count_list))]

    s += selected_dna

    for k in range(n):
        if list[k][i] != selected_dna:
            res += 1

print(s)
print(res)
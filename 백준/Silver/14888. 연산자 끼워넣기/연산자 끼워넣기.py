n = int(input())
An = list(map(int, input().split()))
op = list(map(int, input().split()))
op_cnt = []
res = []

def sol(x, tot):
  if x == n:
    res.append(tot)
    return
  
  if op[0] >= 1:
    op[0] -= 1
    sol(x+1, tot+An[x])
    op[0] += 1

  if op[1] >= 1:
    op[1] -= 1
    sol(x+1, tot-An[x])
    op[1] += 1
    
  if op[2] >= 1:
    op[2] -= 1
    sol(x+1, tot*An[x])
    op[2] += 1
    
  if op[3] >= 1:
    op[3] -= 1
    
    if tot < 0:
      sol(x+1, -(-(tot)//An[x]))

    else:
      sol(x+1, tot//An[x])

    op[3] += 1
    
sol(1, An[0])

print(max(res))
print(min(res))

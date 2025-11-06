n, m = map(int, input().split())
arr = []
isused = [False] * 11


def dfs(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
            
        print()
        return

    for j in range(1, n+1, 1):
        if j not in arr:
            arr.append(j)
            isused[j] = True
            dfs(k+1)
            isused[j] = False
            arr.pop()

dfs(0)

n, m = map(int, input().split())
high = list(map(int, input().split()))

start = 1
end = max(high)

while start <= end:
    sum = 0
    mid = (start + end) // 2

    for i in range(n):
        if mid < high[i]:
            sum += high[i] - mid

        if sum > m:
            break
            
    
    if sum >= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)
    

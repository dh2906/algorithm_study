def Check(k):
    for i in range(k):
        if board[k] == board[i] or abs(board[k] - board[i]) == k - i:
            return False
    return True

def backtracking(k):
    global result

    if k == N:
        result += 1
        return

    for i in range(N):
        board[k] = i
        if Check(k):
            backtracking(k + 1)


N = int(input())
board = [0 for i in range(N)]
result = 0

backtracking(0)

print(result)
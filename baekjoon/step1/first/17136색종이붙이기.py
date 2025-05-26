from collections import deque

board = [list(map(int, input().split())) for _ in range(10)]
papers = [0] * 6
result = 100

def dfs(num, papers):
    global result

    if num == 100:
        result = min(result, sum(papers))
        return 

    y = num // 10
    x = num % 10

    if board[y][x] == 1:
        for level in range(5, 0, -1):
            if papers[level] < 5 and check_zero(level, y, x):
                change_zero(level, y, x, 0)
                papers[level] += 1
                dfs(num + 1, papers)
                change_zero(level, y, x, 1)
                papers[level] -= 1
    else:
        dfs(num + 1, papers)

def check_zero(level, y, x):
    if not (y + level <= 10 and x + level <= 10):
        return False
    
    for i in range(level):
        for j in range(level):
            if board[y+i][x+j] == 0:
                return False
    return True

def change_zero(level, y, x, t):
    for i in range(level):
        for j in range(level):   
            board[y+i][x+j] = t
dfs(0, papers)
print(result if result != 100 else -1)
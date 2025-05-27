from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
result = -1

def dfs(board, count):
    global result
    if count == 5:
        result = max(result, max(map(max, board)))
        return 
    
    temp_board = deepcopy(board)
    
    #왼쪽
    merged = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if board[y][x] != 0:
                move_num(y, x, 0, -1, board, merged)
    dfs(board, count + 1)
    board = deepcopy(temp_board)
    merged = [[False] * N for _ in range(N)]

    #오른쪽
    for y in range(N):
        for x in range(N - 1, -1, -1):
            if board[y][x] != 0:
                move_num(y, x, 0, 1, board, merged)
    dfs(board, count + 1)
    board = deepcopy(temp_board)
    merged = [[False] * N for _ in range(N)]

    #위쪽
    for x in range(N):
        for y in range(N):
            if board[y][x] != 0:
                move_num(y, x, -1, 0, board, merged)
    dfs(board, count + 1)
    board = deepcopy(temp_board)
    merged = [[False] * N for _ in range(N)]

    #아래쪽
    for x in range(N):
        for y in range(N-1, -1, -1):
            if board[y][x] != 0:
                move_num(y, x, 1, 0, board, merged)
    dfs(board, count + 1)
    board = deepcopy(temp_board)
    merged = [[False] * N for _ in range(N)]
    
    return 

def move_num(y, x, dy, dx, board, merged):
    while 0 <= y + dy < N and 0 <= x + dx < N:
        if board[y + dy][x + dx] == 0:
            board[y+dy][x+dx], board[y][x] = board[y][x], board[y+dy][x+dx]
            y += dy
            x += dx
        elif board[y+dy][x+dx] == board[y][x] and not merged[y+dy][x+dx]:
            board[y + dy][x + dx] += board[y][x]
            board[y][x] = 0
            merged[y+dy][x+dx] = True
            break
        else:
            break
dfs(board, 0)
print(result)
N, t, M = map(int, input().split())

board = [[-1] * N for _ in range(M)]

for _ in range(t):
    y, x = map(int, input().split())
    board[y-1][x-1] = 0
    board[y-1][x] = 1

dir = [1, -1] #우측 하단 ↘, 좌측 하단 ↙

result = 100

def check():
    for num in range(N):
        y, x = 0, num
        # print(f"이동 전 : {y}, {x}")
        while y < M:
            if board[y][x] != -1:
                x += dir[board[y][x]]
            y += 1
        #  print(f"이동 후 : {y}, {x}")
        # print()
        if x != num:
            return False
    return True

def dfs(count, num):
    global result

    if check(): #최솟값 갱신 및 가지치기
        if count >= result:
            return
        else:
            # print(f"이후 : {board}")
            result = count
    
    if count >= 3: #종료 조건
        return 

    if num < N * M:
        y, x = num // N, num % N
        dfs(count, num + 1)
        if x < N - 1 and board[y][x] == -1 and board[y][x + 1] == -1:
            board[y][x], board[y][x + 1] = 0, 1
            dfs(count + 1, num + 1)
            board[y][x], board[y][x + 1] = -1, -1
        

# print(f"기존 : {board}")
# print()
dfs(0, 0)
print(-1 if result == 100 else result)
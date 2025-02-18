from collections import deque

n = int(input())

board = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    visited[i][j] = 1
    queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < width:
                if visited[nx][ny] == 0 and board[nx][ny] > check:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
        
limit = 0

for _ in range(n):
    temp = list(map(int, input().split()))
    if max(temp) > limit:
        limit = max(temp)
    board.append(temp)

width = len(board[0])
check = 0
result = [0]

while check < limit:
    count = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and board[i][j] > check:
                count += 1
                bfs(i, j)
    result.append(count)
    check += 1
print(max(result))
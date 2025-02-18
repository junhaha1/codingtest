
from collections import deque
#0:북, 1:동, 2:남, 3:서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m  = map(int, input().split())
x, y, d = map(int, input().split())
board = []

for i in range(n):
    board.append(list(map(int, input().split())))

def bfs(x, y, d):
    queue = deque()
    queue.append((x, y, d))
    board[x][y] = 2
    count = 1
    
    while queue:
        x, y, d = queue.popleft()
        check = False
        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0:
                    check = True
                    board[nx][ny] = 2
                    count += 1
                    queue.append((nx, ny, d))
                    break
        
        if check == False: #후진해야 함. 
            nx = x-dx[d]
            ny = y-dy[d]
            if board[nx][ny] == 1: #뒤에가 벽
                return count
            else:
                queue.append((nx, ny, d))
    return count

print(bfs(x, y, d))
            
        
        
    
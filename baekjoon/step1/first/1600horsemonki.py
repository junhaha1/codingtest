from sys import stdin
from collections import deque

input = stdin.readline
k = int(input())

w, h = map(int, input().rstrip().split())

board = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0] * (k+1) for _ in range(w)] for _ in range(h)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

hx = [2, 2, -2, -2, 1, -1, 1, -1] #좌우
hy = [-1, 1, 1, -1, 2, 2, -2, -2] #상하

#방문 안 했는데 1인 것은 벽
def bfs():
    q = deque()
    visited[0][0][0] = 1
    q.append((0, 0, 0))
    while q:
        x, y, z = q.popleft()
        
        if x == h - 1 and y == w - 1:
            return visited[x][y][z] -1 
        
        for i in range(4): #단순 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny][z] == 0 and board[nx][ny] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z)) 
                    
        if z < k: #말로 이동할 수 있는 횟수가 남아있다면
            for i in range(8): #말로 이동
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < h and 0 <= ny < w and visited[nx][ny][z+1] == 0 and board[nx][ny] == 0:
                    visited[nx][ny][z+1] = visited[x][y][z] + 1
                    q.append((nx, ny, z+1))
                    
    return -1  
       
print(bfs())
# print(board)
# print(horse)
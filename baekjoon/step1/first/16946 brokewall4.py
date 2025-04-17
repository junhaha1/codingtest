from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
result = [[0] * m for _ in range(n)]
dis = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(r, c, number): 
    q = deque()
    q.append((r, c)) 
    board[r][c] = number
    cnt = 1

    while q:
        r, c = q.popleft()
        for d in dis:
            nr = r + d[0]
            nc = c + d[1]
            
            if 0<= nr < n and 0 <= nc < m and board[nr][nc] == 0: 
                board[nr][nc] = number
                cnt += 1 #현재 방문 칸수 늘리기
                q.append((nr, nc))
    return cnt

for i in range(n):
    for j in range(m):
        if board[i][j] == 1: 
            board[i][j] = -1

group = {}
number = 1
for i in range(n):
    for j in range(m):
        if board[i][j] == 0: 
            value = bfs(i,j, number)
            group[number] = value
            number += 1

for i in range(n):
    for j in range(m):
        temp = set()
        if board[i][j] == -1:
            for d in dis:
                ni = i + d[0]
                nj = j + d[1]
                if 0<= ni < n and 0 <= nj < m and board[ni][nj] in group.keys():
                    temp.add(board[ni][nj])
            val = 1
            for t in temp:
                val += group[t]
            result[i][j] = val % 10
        print(result[i][j], end='')
    print()
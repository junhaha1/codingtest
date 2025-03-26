from sys import stdin
from collections import deque
import copy

input = stdin.readline

n, m = map(int, input().rstrip().split())

board = []

for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    board.append(temp)

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_shape = 0

def bfs(x, y, check):
    q = deque()
    cnt = 1
    visited[x][y] = True
    board[x][y] = check
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < m and board[nx][ny] == 1 and visited[nx][ny] == False:
                cnt += 1
                visited[nx][ny] = True
                board[nx][ny] = check
                q.append((nx, ny))
    return cnt

#그룹화
group = {}
num = 1
for x in range(n):
    for y in range(m):
        if board[x][y] == 1 and visited[x][y] == False:
            value = bfs(x, y, num)
            group[num] = value
            num += 1

for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            temp = set()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<= nx < n and 0 <= ny< m and board[nx][ny] in group.keys():
                    temp.add(board[nx][ny])
            temp_sum = 1
            for t in temp:
                temp_sum += group[t]
            max_shape = max(max_shape, temp_sum)

print(max_shape)
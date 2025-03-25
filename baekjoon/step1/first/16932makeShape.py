from sys import stdin
from collections import deque
import copy

input = stdin.readline

n, m = map(int, input().rstrip().split())

board = []

for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    board.append(temp)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_shape = 0

def bfs(cboard, x, y):
    q = deque()
    cnt = 1
    cboard[x][y] = -1
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < m and cboard[nx][ny] == 1:
                cnt += 1
                cboard[nx][ny] = -1
                q.append((nx, ny))
    # print(cboard, cnt)
    # input()
    return cnt

for x in range(n):
    for y in range(m):
        if board[x][y] == 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0<= ny < m and board[nx][ny] == 1:
                    #print(x, y)
                    max_shape = max(max_shape, bfs(copy.deepcopy(board), x, y))
                    break

print(max_shape)


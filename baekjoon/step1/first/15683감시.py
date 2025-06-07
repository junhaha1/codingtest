from sys import stdin
from collections import deque
from copy import deepcopy

input = stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
mp = [(-1, 0), (0, 1), (1, 0), (0, -1)] #시계 방향

cctv_dir = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

def dfs(board, pos, zero, number):
    global result
    
    result = min(result, zero) 

    if number >= len(pos): #큐가 비었으면 종료
        return 

    t_board = deepcopy(board)
    cctv, y, x = pos[number]

    for dirs in cctv_dir[cctv]:
        count = 0
        for dir in dirs:
            ny = y 
            nx = x
            while 0 <= ny + mp[dir][0] < N and 0 <= nx + mp[dir][1] < M:
                ny += mp[dir][0]
                nx += mp[dir][1]
                if board[ny][nx] == 6:
                    break
                elif board[ny][nx] == 0:
                    board[ny][nx] = '#'
                    count += 1
        dfs(board, pos, zero - count, number + 1)
        board = deepcopy(t_board)

result = 0
pos = []

for y in range(N):
    for x in range(M):
        if board[y][x] == 0:
            result += 1
        elif 0 < board[y][x] < 6:
            pos.append((board[y][x], y, x))

dfs(board, pos, result, 0)
print(result)

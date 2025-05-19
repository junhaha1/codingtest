from sys import stdin
from collections import deque

input = stdin.readline

N, Q = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(2**N)]


levels = list(map(int, input().split()))

def slice_turn(sub):
    return [list(reversed(col)) for col in zip(*sub)]

def trun_search(L):
    rows = 2 ** N
    cols = 2 ** N

    for i in range(0, rows, 2 ** L):
        for j in range(0, cols, 2 ** L):
            subgrid = [row[j:j+(2 ** L)] for row in board[i:i+(2 ** L)]]
            rotated = slice_turn(subgrid)

            for x in range(2**L):
                for y in range(2 ** L):
                    board[i + x][j + y] = rotated[x][y]


def check_ice():
    to_reduce = []
    dir = [(1, 0),(0, 1), (-1, 0), (0, -1)]
    for i in range(2 ** N):
        for j in range(2 ** N):
            if board[i][j] == 0:
                continue
            count = 0
            for d in dir:
                ni = i + d[0]
                nj = j + d[1]
                if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and board[ni][nj] != 0:
                    count += 1
            if count < 3:
                to_reduce.append((i, j))
    
    for i, j in to_reduce:
        board[i][j] -= 1

def bfs(i, j):
    count = 1 #방문한 칸수
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    dir = [(1, 0),(0, 1), (-1, 0), (0, -1)]
    while q:
        i, j = q.popleft()
        for d in dir:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < 2 ** N and 0 <= nj < 2 ** N and not visited[ni][nj] and board[ni][nj] != 0:
                visited[ni][nj] = True
                count += 1
                q.append((ni, nj))
    return count

for level in levels:
    trun_search(level)
    check_ice()

sum_ice = 0

for b in board:
    sum_ice += sum(b)

visited = [[False] * (2**N) for _ in range(2 **N)]

blocks = []

for i in range(2 ** N):
    for j in range(2 ** N):
        if not visited[i][j] and board[i][j] > 0:
            blocks.append(bfs(i, j))

#print(*board, sep='\n')

print(sum(map(sum, board)))
print(max(blocks) if blocks else 0)
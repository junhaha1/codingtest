from sys import stdin
from collections import deque

input = stdin.readline

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(i, j, number):
    q = deque()
    q.append((i, j))
    visited[i][j] = True

    count = 1
    hums = board[i][j]

    while q:
        i, j = q.popleft()
        for d in dir:
            ni = i + d[0]
            nj = j + d[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and L <= abs(board[i][j] - board[ni][nj]) <= R:
                visited[ni][nj] = True
                hums += board[ni][nj]
                count += 1
                q.append((ni, nj))
                groups.append((ni, nj, number))

    return hums // count, count

avail = True
day = 0

while avail:
    avail = False
    groups = [] #그룹별 좌표 저장
    hum = [] #그룹별 평균 인구 수 
    visited = [[False] * N for _ in range(N)]
    g_num = 0 #그룹 번호

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                result, count = bfs(i, j, g_num)
                if count > 1:
                    groups.append((i, j, g_num))
                    hum.append(result)
                    g_num += 1

    if len(groups) > 0:
        avail = True
        day += 1
        for i, j, num in groups:
            board[i][j] = hum[num]

print(day)
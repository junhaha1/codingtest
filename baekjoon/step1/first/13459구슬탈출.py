from sys import stdin
from collections import deque

input = stdin.readline
N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]

ry = rx = 0
by = bx = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            ry = i
            rx = j
            board[i][j] = '.'
        if board[i][j] == 'B':
            by = i
            bx = j
            board[i][j] = '.'


def move_ball(y, x, dy, dx):
    count = 0

    #해당 방향 한칸 앞이랑 현재 위치에 대해서 비교
    while board[y + dy][x + dx] != '#' and board[y][x] != 'O':
        y += dy
        x += dx
        count += 1

    return y, x, count

def bfs(ry, rx, by, bx):
    q = deque()
    q.append((ry, rx, by, bx, 0))
    dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    #불필요한 큐 삽입을 막기 위해 이전에 등록된 경로는 큐에 삽입되지 않도록 함. 
    #공간 복잡도 방지용 변수
    visited_route = set()

    while q:
        ry, rx, by, bx, depth = q.popleft()
        if depth >= 10:
            continue
        for dy, dx in dir:
            nry, nrx, r_count = move_ball(ry, rx, dy, dx)
            nby, nbx, b_count = move_ball(by, bx, dy, dx)

            #빨강 공이 먼저 들어갔을 때 파랑 공도 안 들어가야 성공
            if board[nry][nrx] == 'O' and board[nby][nbx] != 'O':
                print(1)
                exit(0)
            
            if board[nby][nbx] == 'O':
                continue
            
            #두 공의 위치가 겹칠 때 더 많이 움직인 공이 뒤늦게 굴러온 공이므로 한칸 뒤에 위치하도록 함. 
            if (nry, nrx) == (nby, nbx):
                if r_count > b_count:
                    nry -= dy
                    nrx -= dx
                else:
                    nby -= dy
                    nbx -= dx

            #이미 갔던 좌표가 아니라면 큐에 삽입
            if (nry, nrx, nby, nbx) not in visited_route:
                visited_route.add((nry, nrx, nby, nbx))
                q.append((nry, nrx, nby, nbx, depth + 1))

bfs(ry, rx, by, bx)
print(0)
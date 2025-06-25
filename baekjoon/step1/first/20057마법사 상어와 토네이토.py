from sys import stdin
input = stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

move = [
    [ #좌
        (0, -1), (-2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (0, -2, 0.05), 
        (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (2, 0, 0.02)
    ], 
    [ #하
        (1, 0), (-1, -1, 0.01), (-1, 1, 0.01), (0, -2, 0.02), (0, -1, 0.07), (0, 1, 0.07), 
        (0, 2, 0.02), (1, -1, 0.1),  (1, 1, 0.1), (2, 0, 0.05)
    ], 
    [ #우
        (0, 1), (-2, 0, 0.02), (-1, -1, 0.01), (-1, 0, 0.07), (-1, 1, 0.1),  
        (0, 2, 0.05), (1, -1,0.01), (1, 0, 0.07), (1, 1, 0.1), (2, 0, 0.02)
    ], 
    [ #상
        (-1, 0), (-2, 0, 0.05),(-1, -1, 0.1),  (-1, 1, 0.1),(0, -2, 0.02), 
        (0, -1,0.07), (0, 1,0.07), (0, 2, 0.02), (1, -1, 0.01), (1, 1, 0.01)
    ], 
]

def move_sand(y, x, sand, i, N):
    out = 0
    total = sand
    for d in move[i][1:]:
        dy, dx, c = d
        temp = int(sand * c)
        if 0 <= y + dy < N and 0 <= x + dx < N:
            board[y+dy][x+dx] += temp
        else:
            out += temp
        total -= temp

    dy, dx = move[i][0]
    ny = y + dy
    nx = x + dx

    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += total
    else:
        out += total

    return out

check = 0 #방향 전환
count = 1 #해당 방향 이동 횟수
result = 0 #격자 밖으로 나간 모래 
dir = 0 #방향 왼쪽부터

i, j = N // 2, N // 2 #출발 좌표

pos = [(0, -1), (1, 0), (0, 1), (-1, 0)]

while not (i <= 0 and j <= 0): #(1, 1)에 도달할 때까지 반복
    for _ in range(count):
        i += pos[dir][0]
        j += pos[dir][1]
        result += move_sand(i, j, board[i][j], dir, N)
        board[i][j] = 0 #모래를 0으로 초기화
    check += 1
    dir = (dir + 1) % 4
    
    if check == 2: #2번 움직였다면
        count += 1
        check = 0
    # print("----")
    # print(*board, sep='\n')
    # print(i, j)
    # input()
print(result)

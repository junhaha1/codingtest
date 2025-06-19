from collections import deque
N = int(input())

board = [[0] * N for _ in range(N)]
board[0][0] = 1 #뱀의 시작점
infos = [0] * 100001 #방향 정보

for _ in range(int(input())):
    i, j = map(int, input().split())
    board[i-1][j-1] = 2 #사과

for _ in range(int(input())):
    s, d = input().split()#방향 정보
    infos[int(s)] = d

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
pos = deque()
pos.append((0,0))
second = 0
idx = 1 #오른쪽
y = 0
x = 0

while True:
    second += 1
    y += dir[idx][0]
    x += dir[idx][1]

    if not (0 <= y < N and 0 <= x < N): #벽에 부딪쳤다면 종료
        break
    if board[y][x] == 1: #뱀 일부분이라면 종료
        break

    if board[y][x] == 2: #사과라면
        pos.appendleft((y, x))
        board[y][x] = 1
    else: #사과가 아니라면
        pos.appendleft((y, x))
        board[y][x] = 1
        oy, ox = pos.pop()
        board[oy][ox] = 0 #빈공간으로 다시 초기화
    
    #방향 전환
    if infos[second] == 'D':
        idx = (idx + 1) % 4
    
    elif infos[second] == 'L':
        idx = (idx - 1) % 4

    # #로그 출력용
    # print(*board, sep = '\n')
    # print(second)
    # input()

print(second)

from collections import deque, defaultdict
import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]

def throw_stick(dir, col, row_board):
    x = None
    if dir < 0: #왼쪽
        for i in range(col):
            if row_board[i] == 'x':
                x = i
                break
    else: #오른쪽
        for i in range(col - 1, -1, -1):
            if row_board[i] == 'x':
                x = i
                break
    return x

def group_mineral(visited, board, ny, nx):
    q = deque()
    group = []
    visited[ny][nx] = True

    q.append((ny, nx))
    group.append([ny, nx])

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == 'x' and not visited[ny][nx]:
                q.append((ny, nx))
                group.append([ny, nx])
                visited[ny][nx] = True

    group.sort(reverse=True)
    return group

    
def fall_mineral(pos, R, board):

    for y, x in pos: #미네랄 추락을 위한 보드판 초기화
        board[y][x] = '.'

    while True:
        new_pos = []
        for i in range(len(pos)):
            if pos[i][0] + 1 < R and board[pos[i][0] + 1][pos[i][1]] != 'x':
                new_pos.append([pos[i][0] + 1, pos[i][1]])
            else:
                break
        if len(pos) != len(new_pos):
            break
        else:
            pos = new_pos
        
    for y, x in pos:
        board[y][x] = 'x'


lr = -1 #막대기 방향
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N = int(input()) #막대기 던진 횟수
heights = map(int, input().split())

for height in heights:

    row = R - height #막대기를 던진 위치
    col = throw_stick(lr, C, board[row]) #미네랄 위치 찾기
    lr *= -1 #방향 바꾸기
    
    if col == None: #미네랄이 없다면 건너뛰기
        continue
    
    board[row][col] = '.'
    visited = [[False] * C for _ in range(R)]

    groups = dict()
    num = 0

    for dy, dx in dirs:
        ny, nx = row + dy, col + dx
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == 'x' and not visited[ny][nx]:
            num += 1
            groups[num] = group_mineral(visited, board, ny, nx)
    
    # print(groups)
    # print(*board, sep='\n')
    
    
    if num == 1: #미네랄 그룹이 1개라면 건너뛰기
        continue


    for pos in groups.values():
        if pos[0][0] < R - 1: #이미 바닥에 붙어있는 미네랄 덩어리가 아니라면 미네랄 추락
            fall_mineral(pos, R, board)
            # print(*board, sep='\n')

for i in range(len(board)):
    print(''.join(board[i]))
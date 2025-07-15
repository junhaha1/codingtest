from collections import deque

def solution(game_board, table):
    answer = 0
    spaces = []
    blocks = []
    
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 0:
                size, space, game_board = bfs(game_board, i, j, 0, 1)
                spaces.append((size, space))
                
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 1:
                size, block, table = bfs(table, i, j, 1, 0)
                blocks.append((size, block))
    
    spaces.sort(reverse=True)
    blocks.sort(reverse=True)
    
    used = [False] * len(blocks) #블럭 사용여부를 갱신

    # print(spaces)
    # print(blocks)
    
    for s_size, space in spaces: #블럭을 넣을 공간과 블럭을 매칭하는 로직
        check = False
        for i in range(len(blocks)):
            b_size = blocks[i][0]
            block = blocks[i][1]

            if used[i] == False and s_size == b_size: #사용여부와 크기가 일치하는지 확인
                for _ in range(4):
                    if block == space:
                        answer += b_size
                        used[i] = True
                        check = True
                        break
                    else:
                        block = rotate(block)
            if check: #공간과 블럭이 매칭됐을 경우, 블럭 순회 종료
                break
    
    return answer

def rotate(block): #블럭 회전 함수
    return [list(row) for row in zip(*block[::-1])]


def bfs(matrix, x, y, value, target): #BFS 탐색을 통해 블럭 뽑아내는 함수
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pos_x = [x]
    pos_y = [y]  
    
    size = 1
    
    matrix[x][y] = target
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(matrix) and 0 <= ny <len(matrix[0]) and matrix[nx][ny] == value:
                matrix[nx][ny] = target
                q.append((nx, ny))
                
                pos_x.append(nx)
                pos_y.append(ny)
                
                size += 1
    
    min_row, max_row = min(pos_x), max(pos_x)
    min_col, max_col = min(pos_y), max(pos_y)
    
    len_row = max_row - min_row + 1
    len_col = max_col - min_col + 1
    
    block = make_block(pos_x, pos_y, min_row, min_col, len_row, len_col)
    
    return size, block, matrix

def make_block(pos_x, pos_y, min_row, min_col, row, col): #블럭을 스케일링하는 함수
    block = [[0] * col for _ in range(row)]
    
    for nx, ny in list(zip(pos_x, pos_y)):
        block[nx - min_row][ny - min_col] = 1
    
    return block
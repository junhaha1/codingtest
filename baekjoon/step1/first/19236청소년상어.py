from sys import stdin
from copy import deepcopy

input = stdin.readline

board = [[None] * 4 for _ in range(4)]
fish_pos = dict()
max_score = 0

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
dir = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def move_fishes(board, fish_pos, shark_pos):
    for fish_num in range(1, 17):
        if fish_num not in fish_pos:
            continue

        y, x = fish_pos[fish_num]
        d = board[y][x][1] #해당 물고기 방향

        for i in range(8):
            nd = (d + i) % 8
            ny = y + dir[nd][0]
            nx = x + dir[nd][1]

            if 0 <= ny < 4 and 0 <= nx < 4 and (ny, nx) != shark_pos:
                if board[ny][nx][0] != 0:
                    swap_fish = board[ny][nx][0]
                    fish_pos[swap_fish] = (y, x)

                board[ny][nx], board[y][x] = (fish_num, nd), board[ny][nx]
                fish_pos[fish_num] = (ny, nx)
                break

def dfs(board, fish_pos, shark_pos, shark_dir, score):
    global max_score
    
    move_fishes(board, fish_pos, shark_pos)

    temp_board = deepcopy(board)
    temp_fish_pos = deepcopy(fish_pos)

    y, x = shark_pos
    moved = False  # 상어가 한 번이라도 이동했는지

    for step in range(1, 4): #해당 방향으로 최대 3번만 이동 가능 4 * 4이므로.
        ny = y + dir[shark_dir][0] * step
        nx = x + dir[shark_dir][1] * step

        if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx][0] != 0: #물고기가 없는 곳이 아니라면 
            moved = True
            eat_fish_num, new_dir = board[ny][nx] #먹은 물고기 번호, 새로운 방향

            board[ny][nx] = (0, 0) #상어가 이동한 곳의 물고기를 먹었으므로 0으로 초기화 
            del fish_pos[eat_fish_num] #먹은 물고기 딕셔너리에서 삭제

            dfs(board, fish_pos, (ny, nx), new_dir, score + eat_fish_num)

            board = deepcopy(temp_board)
            fish_pos = deepcopy(temp_fish_pos)
            
    if not moved:
        max_score = max(max_score, score)

# 입력 처리
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        fish_num = data[2 * j]
        direction = data[2 * j + 1] - 1
        board[i][j] = (fish_num, direction)
        fish_pos[fish_num] = (i, j)

first_fish_num, first_fish_dir = board[0][0]
board[0][0] = (0, 0) #상어가 해당 물고기를 먹음. 
del fish_pos[first_fish_num]

dfs(board, fish_pos, (0, 0), first_fish_dir, first_fish_num)

print(max_score)
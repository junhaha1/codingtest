N, M, y, x, T = map(int, input().split())

dice = [0, 0, 0, 0, 0, 0] #top, bottom, north, south, east, west

dir = [(), (0, 1), (0, -1), (-1, 0), (1, 0)] #동 1, 서 2, 북 3, 남 4 

board = [list(map(int, input().split())) for _ in range(N)]
moves = list(map(int, input().split()))

for move in moves:
    ny = y + dir[move][0]
    nx = x + dir[move][1]
    if not (0 <= ny < N and 0 <= nx < M): #해당 케이스 건너뛰기
        continue

    y = ny
    x = nx

    #주사위 굴리기
    if move == 1: #동
        top, bottom, east, west = dice[0], dice[1], dice[4], dice[5]
        dice[0], dice[1], dice[4], dice[5] = west, east, top, bottom
    elif move == 2: #서
        top, bottom, east, west = dice[0], dice[1], dice[4], dice[5]
        dice[0], dice[1], dice[4], dice[5] = east, west, bottom, top
    elif move == 3: #북
        top, bottom, north, south = dice[0], dice[1], dice[2], dice[3]
        dice[0], dice[1], dice[2], dice[3] = south, north, top, bottom
    elif move == 4: #남
        top, bottom, north, south = dice[0], dice[1], dice[2], dice[3]
        dice[0], dice[1], dice[2], dice[3] = north, south, bottom, top

    # 보드 바닥이 0이라면 주사위 바닥면을 복사
    if board[ny][nx] == 0:
        board[ny][nx] = dice[1]
    # 보드 바닥이 0이 아니라면 주사위 바닥면에 복사
    else: 
        dice[1] = board[ny][nx]
        board[ny][nx] = 0
    
    print(dice[0])
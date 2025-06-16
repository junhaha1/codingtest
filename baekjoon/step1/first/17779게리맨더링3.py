from sys import stdin 
input = stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
pos = []

def updateSection(x, y, d1, d2, section, N): #5번 경계선 찾기
    #x,y부터 시계 반대 방향으로 돌면서 경계선 채우기
    nx, ny = x, y
    while nx < x + d1 and ny > y - d1:
        section[nx][ny] = 5
        nx += 1
        ny -= 1
    while nx < x + d1 + d2 and ny < y - d1 + d2:
        section[nx][ny] = 5
        nx += 1
        ny += 1
    while nx > x + d2 and ny < y + d2:
        section[nx][ny] = 5
        nx -= 1
        ny += 1
    while nx > x and ny > y:
        section[nx][ny] = 5
        nx -= 1
        ny -= 1

def fillSection(x, y, d1, d2, section, N): #경계선을 필두로 지역구 표시 채워넣기
    max_count = 0
    min_count = int(1e9)

    #1구역 값구하기
    temp = 0
    for i in range(x + d1):
        for j in range(y + 1):
            if section[i][j] == 5:
                break
            else:
                temp += board[i][j]
    max_count = max(max_count, temp)
    min_count = min(min_count, temp)

    #2구역 값 구하기
    temp = 0
    for i in range(x + d2 + 1):
        for j in range(N - 1, y, -1):
            if section[i][j] == 5:
                break
            else:
                temp += board[i][j]
    max_count = max(max_count, temp)
    min_count = min(min_count, temp)

    #3구역 값 구하기
    temp = 0
    for i in range(x + d1, N):
        for j in range(y - d1 + d2):
            if section[i][j] == 5:
                break
            else:
                temp += board[i][j]
    max_count = max(max_count, temp)
    min_count = min(min_count, temp)

    #4구역 값 구하기
    temp = 0
    for i in range(x + d2 + 1, N):
        for j in range(N - 1, y - d1 + d2 - 1, - 1):
            if section[i][j] == 5:
                break
            else:
                temp += board[i][j]
    max_count = max(max_count, temp)
    min_count = min(min_count, temp)

    
    #5구역 값 구하기
    temp = 0
    temp += board[x][y] + board[x+d1+d2][y-d1+d2]
    for i in range(x + 1, x + d1 + d2):
        flag = False
        for j in range(N):
            if section[i][j] == 5:
                temp += board[i][j]
                flag = not flag
            elif section[i][j] != 5 and flag:
                temp += board[i][j]
    max_count = max(max_count, temp)
    min_count = min(min_count, temp)

    # print(*section, sep= '\n')
    # print(temp)
    # print()
    # input()

    return max_count - min_count

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                section = [[0] * N for _ in range(N)]
                if 0 <= x + d1 + d2 < N and 0 <= y - d1 < y < y + d2 < N:
                    pos.append((x, y, d1, d2))

result = int(1e9)
for x, y, d1, d2 in pos:
    section = [[0] * N for _ in range(N)]
    updateSection(x, y, d1, d2, section, N)
    result = min(result, fillSection(x, y, d1, d2, section, N))

print(result)
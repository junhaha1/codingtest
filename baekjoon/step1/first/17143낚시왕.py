from sys import stdin
input = stdin.readline

R, C, N = map(int, input().split())
sharks = [[]]
sea = [[0] * C for _ in range(R)]
dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
result = 0 #잡은 상어 무게

for i in range(1, N + 1):
    r, c, s, d, z = map(int, input().split())
    sea[r - 1][c - 1] = i
    sharks.append([r - 1, c - 1, s, d - 1, z])


def fishing_shark(idx, row): #상어 잡기
    size = 0
    for r in range(row):
        if sea[r][idx] != 0: #바다가 아니라면
            num = sea[r][idx] #상어 번호
            size = sharks[num][4] #상어 무게를 더하기
            sharks[num] = [] #해당 상어 정보 없애기
            sea[r][idx] = 0 #해당 바다에서 상어 없애기
            break
    return size

def move_shark(row, col): #상어 이동하기
    board = [[0] * col for _ in range(row)]
    r, c, s, d, z = 0, 1, 2, 3, 4#행 0, 열 1, 초 2, 방향 3, 사이즈 4

    for i in range(1, len(sharks)):
        #이미 잡힌 상어라면 건너뛰기
        if len(sharks[i]) == 0: continue 
        #주기 계산 
        cycle = 0
        if sharks[i][d] in [0, 1]: #상하라면
            cycle = sharks[i][s] % (2 * (row - 1))
        else:
            cycle = sharks[i][s] % (2 * (col - 1))
        
        for _ in range(cycle): #상어를 이동
            #바다 크기보다 넘어갈려고 할때 방향을 바꾸어 이동
            if not (0 <= sharks[i][r] + dir[sharks[i][d]][0] < row and 0 <= sharks[i][c] + dir[sharks[i][d]][1] < col):  
                if sharks[i][d] == 0:
                    sharks[i][d] = 1
                elif sharks[i][d] == 1:
                    sharks[i][d] = 0
                elif sharks[i][d] == 2:
                    sharks[i][d] = 3
                elif sharks[i][d] == 3:
                    sharks[i][d] = 2
            sharks[i][r] += dir[sharks[i][d]][0]
            sharks[i][c] += dir[sharks[i][d]][1]


        # print(f"{i}번 상어 이동 - 뱡향: {sharks[i][d]}, 좌표 : ({sharks[i][r]}, {sharks[i][c]}, 크기: {sharks[i][z]})")
        #이미 해당 좌표에 상어가 있다면
        if board[sharks[i][r]][sharks[i][c]] != 0: 
            if sharks[board[sharks[i][r]][sharks[i][c]]][z] < sharks[i][z]: #현재 상어가 크다면
                num = board[sharks[i][r]][sharks[i][c]]
                sharks[num] = [] #잡아먹힌 상어
                board[sharks[i][r]][sharks[i][c]] = i #현재 상어로 교체
            else: #현재 상어가 작을 때
                sharks[i] = [] #현재 상어가 잡아먹히기
        #해당 좌표에 상어가 없을 경우
        else:
            board[sharks[i][r]][sharks[i][c]] = i

    return board

# print(*sea, sep= '\n')
for i in range(C): #낚시꾼 이동
    result += fishing_shark(i, R) #상어 잡기
    sea = move_shark(R, C)
    # print(f"{i}번째")
    # print(*sea, sep= '\n')
    # print()

print(result)
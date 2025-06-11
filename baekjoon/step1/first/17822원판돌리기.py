from sys import stdin
from collections import deque
input = stdin.readline

N, M, K = map(int, input().split())

board = [deque(list(map(int, input().split()))) for _ in range(N)] #현재 원판
visited = [deque([True] * M) for _ in range(N)] #중복 처리 했는지 

truns = [list(map(int, input().split())) for _ in range(K)] #회전 방식
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] #사방 탐색을 위한 변수

#초기값
count = N * M #원판에 존재하는 수의 갯수
scores = sum(map(sum, board)) #원판에 존재하는 수의 총합

# print(scores)

for trun in truns:
    x, d, k = trun #원판 번호 배수, 방향, 회전 칸수

    if scores == 0: #scores가 0이라면 더이상 진행하는 의미가 없으므로 종료
        break

    #회전 동작
    for i in range(x-1, N, x):
        for _ in range(k): #이동하는 칸수만큼 반복
            if d == 0: #시계 방향
                board[i].appendleft(board[i].pop())
                visited[i].appendleft(visited[i].pop())
            else: #반시계 방향
                board[i].append(board[i].popleft())
                visited[i].append(visited[i].popleft())

    pos = [] #중복된 수가 있는 경우
    #인접한 수 찾기
    for y in range(N):
        for x in range(M):
            if visited[y][x] == False: #중복 제거된 수는 건너뛰기
                continue
            for d in dir:
                ny = y + d[0]
                nx = x + d[1]

                if nx >= M: #맨끝이랑 맨앞이랑 비교 원형이기 때문에
                    nx = 0

                if 0 <= ny < N and visited[ny][nx] == True and board[y][x] == board[ny][nx]:
                    pos.append((y, x))
                    break
    
    count -= len(pos)
    for p in pos: #중복처리
        y, x = p
        visited[y][x] = False
        scores -= board[y][x]

    if not len(pos): #인접한 수가 하나도 없는 경우 
        avg = scores / count
        for y in range(N):
            for x in range(M):
                if visited[y][x]:
                    if board[y][x] > avg:
                        board[y][x] -= 1
                        scores -= 1
                    elif board[y][x] < avg:
                        board[y][x] += 1
                        scores += 1
print(scores)


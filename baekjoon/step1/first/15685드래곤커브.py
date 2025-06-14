from sys import stdin
input = stdin.readline
board = [[0] * 101 for _ in range(101)]

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for _ in range(int(input())):
    x, y, d, g = map(int, input().split())

    #0세대 처리
    board[y][x] = 1
    y += dir[d][0]
    x += dir[d][1]
    board[y][x] = 1

    dis = [d]
    for _ in range(g):
        new_dis = dis[::-1] #현재 선분들의 방향 순서를 역순으로 재정렬
        for i in range(len(new_dis)):
            #90도 회전한 선분 방향 추가하기
            nd = (new_dis[i] + 1) % 4
            dis.append(nd)

            #해당 선분의 끝점에 방문처리하기
            y += dir[nd][0]
            x += dir[nd][1]

            board[y][x] = 1

result = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i+1][j] and board[i][j+1] and board[i+1][j+1]:
            result += 1

print(result)

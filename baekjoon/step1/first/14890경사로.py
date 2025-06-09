N, L = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

streets = []
#row방향
for r in range(N):
    temp = []
    target = board[r][0]
    count = 1
    for c in range(1, N):
        if board[r][c] != target:
            temp.append([target, count])
            target = board[r][c]
            count = 1
        else: #같을 경우
            count += 1
    temp.append([target, count])
    streets.append(temp)

#col방향
for c in range(N):
    temp = []
    target = board[0][c]
    count = 1
    for r in range(1, N):
        if board[r][c] != target:
            temp.append([target, count])
            target = board[r][c]
            count = 1
        else: #같을 경우
            count += 1
    temp.append([target, count])
    streets.append(temp)

result = 0
for street in streets:
    flag = True
    for i in range(len(street) - 1):
        if abs(street[i][0] - street[i + 1][0]) != 1:
            flag = False
            break
        t = i if street[i][0] < street[i+1][0] else i + 1
        if street[t][1] < L:
            flag = False
            break

        street[t][1] -= L
    
    if flag:
        #print(street)
        result += 1

print(result)


score = [0] * 33
for i in range(1, 21):
    score[i] = i * 2
score[21], score[22], score[23] = 13, 16, 19
score[24], score[25], score[26] = 25, 22, 24
score[27], score[28], score[29] = 28, 27, 26
score[30], score[31], score[20] = 30, 35, 40

# 이동 경로
next_pos = [0] * 33
for i in range(0, 20):
    next_pos[i] = i + 1
next_pos[20] = 32  # 도착 지점
next_pos[21] = 22
next_pos[22] = 23
next_pos[23] = 24
next_pos[24] = 30
next_pos[25] = 26
next_pos[26] = 24
next_pos[27] = 28
next_pos[28] = 29
next_pos[29] = 24
next_pos[30] = 31
next_pos[31] = 20

def move(pos, d):
    if pos == 32:
        return 32
    
    #특수칸 처리를 위해 한칸 이동했으므로 1칸 이동
    if pos == 5:
        pos = 21
        d -= 1
    elif pos == 10:
        pos = 25
        d -= 1
    elif pos == 15:
        pos = 27
        d -= 1

    for _ in range(d):
        pos = next_pos[pos]
        if pos == 32:
            break
    return pos

dices =  list(map(int, input().split()))
obj = [0, 0, 0, 0] #말의 위치

result = 0

#현재 보드판 인덱스, 현재 다이스 번호, 누적합, 현재 말의 번호, 보드판 인덱스 
def dfs(depth, total):
    global result 
    if depth == 10:
        result = max(result, total)
        return 
    
    for i in range(4):
        if obj[i] == -1: #도착했다면 건너뛰기
            continue

        cur_pos = obj[i]
        new_pos = move(cur_pos, dices[depth])
        #도착지가 아니고 다른 말들이 해당 위치에 존재한다면 건너뛰기
        if new_pos != 32 and new_pos in obj: 
            continue

        temp = obj[i]
        if new_pos == 32:
            obj[i] = -1
            dfs(depth + 1, total)
        else:
            obj[i] = new_pos
            dfs(depth + 1, total + score[new_pos])
        obj[i] = temp

dfs(0, 0)
print(result)
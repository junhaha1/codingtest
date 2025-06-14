from sys import stdin
from collections import deque
input = stdin.readline

N, M, energe = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

y, x = map(int, input().split())
taxi = [y-1, x-1]
dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]

#승객 좌표 저장
for _ in range(M):
    sy, sx, ey, ex = map(int, input().split())
    board[sy-1][sx-1] = (ey-1, ex-1)

#현재 택시 위치에서 최단거리의 승객 찾기
def find_people(taxi_pos, current_energe):
    visited = [[False] * N for _ in range(N)]
    
    q = deque()
    q.append((taxi_pos[0], taxi_pos[1], 0))
    visited[taxi_pos[0]][taxi_pos[1]] = True

    candidates = []

    while q:
        y, x, consume_energe = q.popleft()

        if current_energe <= consume_energe: #연료 고갈로 해당 위치에서 움직일 수 없음. 
            continue

        if board[y][x] != 0: #최단 거리 승객을 찾음. 
            candidates.append((consume_energe, y, x))
            continue
        
        for d in dir:
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 1 and visited[ny][nx] == False:
                visited[ny][nx] = True
                q.append((ny, nx, consume_energe + 1))
    
    if len(candidates) == 0:
        return False, False, False, False
    
    candidates.sort()
    #print(candidates)
    consume_energe, y, x = candidates[0]
    dest = board[y][x]
    board[y][x] = 0

    return True, (y, x), dest, current_energe - consume_energe
    

#현재 택시 위치에서 도착지까지 최단거리로 이동하기
def arrive_destination(taxi_pos, dest, current_energe):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((taxi_pos[0], taxi_pos[1], 0))
    visited[taxi_pos[0]][taxi_pos[1]] = True

    while q:
        y, x, consume_energe = q.popleft()

        if y == dest[0] and x == dest[1]: #목적지에 도착했을 경우
            current_energe += consume_energe
            return True, (y, x), current_energe #현재 택시 위치, 충전된 현재 연료량
        
        if current_energe <= consume_energe: #연료 고갈로 해당 위치에서 움직일 수 없음. 
            continue

        for d in dir:
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] != 1 and visited[ny][nx] == False:
                visited[ny][nx] = True
                q.append((ny, nx, consume_energe + 1))
        
    return False, False, False

for _ in range(M):
    check, taxi, dest, energe = find_people(taxi, energe)
    if check == False: #손님을 못찾거나 연료가 고갈된 경우
        energe = -1
        break
    
    check, taxi, energe = arrive_destination(taxi, dest, energe)
    if check == False: #목적지를 도착할 수 없거나 연료가 고갈된 경우
        energe = -1
        break

print(energe)
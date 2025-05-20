from sys import stdin
from collections import deque

N = int(input()) # N * N 보드판 의미
sea = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열 바다

shark_pos = None # 상어의 위치
shark_size = 2 # 상어의 사이즈
eat_fish = 0 #현재까지 누적된 먹은 물고기 수
time = 0 #상어가 엄마 상어를 부르기까지 시간
dire = [(-1, 0), (0, -1), (1, 0), (0, 1)] #우선순위 : 가장 위쪽, 가장 왼쪽이므로 다음과 같이 초기화

for i in range(N):
    for j in range(N):
        if sea[i][j] == 9: #상어의 위치 찾기
            shark_pos = (i, j) 
            sea[i][j] = 0

def bfs(shark_pos, shark_size):
    visited = [[-1] * N for _ in range(N)] # -1부터 시작
    fishes = []
    q = deque()
    q.append(shark_pos)
    visited[shark_pos[0]][shark_pos[1]] += 1

    while q:
        y, x = q.popleft()
        for dy, dx in dire:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == -1:
              if sea[ny][nx] <= shark_size: #해당 위치에 값이 상어 사이즈보다 작다면 이동가능
                visited[ny][nx] = visited[y][x] + 1 #시작 위치에서 해당 위치까지 방문 확인 + 거리 계산
                q.append((ny, nx))
                if 0 < sea[ny][nx] < shark_size: #해당 위치값이 0(빈칸)이 아니고 상어 사이즈 보다 작다면 먹을 수 있는 후보 물고기
                  fishes.append((visited[ny][nx], ny, nx)) #거리, y좌표, x좌표 삽입

    return sorted(fishes)


while True:
    fishes = bfs(shark_pos, shark_size) #아기 상어가 먹을 수 있는 후보 물고기 찾기
    if not fishes: #먹을 수 있는 후보 물고기가 없으면 종료
      break

    dis, fish_y, fish_x = fishes[0] #거리순으로 오름차순 후 우선순위가 제일 높은 첫번째 물고기
    shark_pos = (fish_y, fish_x) #먹은 물고기 위치로 상어 위치
    sea[fish_y][fish_x] = 0 #먹힌 물고기는 0으로 비움
    eat_fish += 1 #먹은 물고기 수 누적 
    time += dis #1칸 이동할 때 1초 걸리므로 거리 자체가 이동한 초와 같음. 

    if eat_fish == shark_size:
        shark_size += 1
        eat_fish = 0 #다음 누적을 위해 0으로 초기화
    
print(time)
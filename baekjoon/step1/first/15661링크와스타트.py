from sys import stdin
input = stdin.readline

N = int(input())
player = [0] * N # 0: 링크 팀, 1 : 스타 팀
board = [list(map(int, input().split())) for _ in range(N)]
result = 10 ** 6

def select_team(player):
    star = []
    link = []
    for i, t in enumerate(player):
        if t == 0:
            link.append(i)
        if t == 1:
            star.append(i)
    return star, link

def cal_team(team):
    sum_player = 0
    for i in team:
        for j in team:
            sum_player += board[i][j]
    return sum_player

def dfs(start, player, s_count):
    global result
    if s_count == N // 2:
        star, link = select_team(player)
        star_score = cal_team(star)
        link_score = cal_team(link)
        result = min(result, abs(star_score - link_score))
        return 
    
    for i in range(start, N):
        if player[i] == 0: #링크 팀이면 스타 팀으로 바꿔보기
            player[i] = 1
            dfs(i+1, player, s_count + 1)

            player[i] = 0 #경로 복원

dfs(0, player, 0)
print(result)

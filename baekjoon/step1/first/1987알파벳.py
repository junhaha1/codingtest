from sys import stdin
input = stdin.readline

def dfs(pos, alpha, count):
    global max_count
    flag = False

    for dy, dx in dire:
        ny = pos[0] + dy
        nx = pos[1] + dx
        if 0<= ny < R and 0 <= nx < C:
            i = ord(board[ny][nx]) % ord('A')
            if alpha[i] == 0:
                alpha[i] = 1
                dfs((ny, nx), alpha, count + 1)
                alpha[i] = 0
                flag = True
    if not flag:
        max_count = max(max_count, count)

R, C = map(int, input().split())
board = [list(input().rstrip()) for _ in range(R)]
dire = [(1,0), (-1, 0), (0, -1), (0, 1)]

max_count = 1
alpha = [0] * 26 #첫 시작점
alpha[ord(board[0][0]) % ord('A')] = 1
dfs((0, 0), alpha, max_count)

print(max_count)
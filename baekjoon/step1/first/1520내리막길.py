from sys import stdin
import sys
sys.setrecursionlimit(10 ** 6)

input = stdin.readline

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(y, x):
    if y == M - 1 and x == N - 1:
        return 1
    
    if dp[y][x] != -1: #이미 계산되었을 경우
        return dp[y][x]

    dp[y][x] = 0 #방문 처리
    for d in dir:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < N and 0 <= ny < M:
            if board[ny][nx] < board[y][x]:
                dp[y][x] += dfs(ny, nx)
    
    return dp[y][x]

print(dfs(0, 0))
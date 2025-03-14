from sys import stdin

input = stdin.readline

n, m = map(int, input().rstrip().split())

board = [list(map(int, input().rstrip().split())) for _ in range(n)]

ans = 0
for i in range(n): #행
  for j in range(m): #열
    #1번 도형
    if i + 3 < n: #세로
      ans = max(board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j], ans)
    if j + 3 < m: #가로
      ans = max(board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j+3], ans)
    #2번 도형
    if i + 1 < n and j + 1 < m:
      ans = max(board[i][j] + board[i+1][j] + board[i][j+1] + board[i+1][j+1], ans)
    #3번 도형
    if i + 2 < n:
      if j + 1 < m: 
        temp = max(board[i+2][j+1], board[i][j+1]) + board[i][j] + board[i+1][j] + board[i+2][j]
        ans = max(temp, ans)
      if j - 1 >= 0:
        temp = max(board[i+2][j-1], board[i][j-1]) + board[i][j] + board[i+1][j] + board[i+2][j]
        ans = max(temp, ans)
    if j + 2 < m:
      if i + 1 < n:
        temp = max(board[i+1][j+2], board[i+1][j]) + board[i][j] + board[i][j+1] + board[i][j+2]
        ans = max(temp, ans)
      if i - 1 >= 0:
        temp = max(board[i-1][j+2], board[i-1][j]) + board[i][j] + board[i][j+1] + board[i][j+2]
        ans = max(temp, ans)
    
    #4&5번 도형 세로
    if j + 1 < m:
      if i - 1 >= 0 and i + 1 < n: #||
        #4번 도형
        temp = max(board[i-1][j] + board[i+1][j+1], board[i-1][j+1] + board[i+1][j]) + board[i][j] + board[i][j+1]
        ans = max(temp, ans)
        
        #5번 도형
        temp = max(board[i-1][j] + board[i+1][j], board[i-1][j+1] + board[i+1][j+1]) + board[i][j] + board[i][j+1]
        ans = max(temp, ans)
    # 4&5번 도형 가로
    if i + 1 < n:
      if j-1 >=0 and j + 1 < m:
        #4번 도형
        temp = max(board[i][j-1] + board[i+1][j+1], board[i][j+1] + board[i+1][j-1]) + board[i][j] + board[i+1][j]
        ans = max(temp, ans)
        
        temp = max(board[i][j-1] + board[i][j+1], board[i+1][j-1] + board[i+1][j+1]) + board[i][j] + board[i+1][j]
        ans = max(temp, ans)
        
print(ans)
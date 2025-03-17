from sys import stdin
from collections import deque

input = stdin.readline().rstrip

S = int(input())
visited = [[False] * 1001 for _ in range(1001)]
visited[1][0] = True

def bfs():
  q = deque()
  q.append((1,0,0)) #현재 스티커 수, 클립보드, 횟수
  
  while q:
    s, c, cnt = q.popleft()
    
    if s == S:
      print(cnt)
      return 
    
    #복사하기
    if not visited[s][s]:
      visited[s][s] = True
      q.append((s,s,cnt + 1))
    
    #붙여넣기
    if s + c <= 1000 and not visited[s+c][c]:
      visited[s+c][s] = True
      q.append((s+c, c, cnt+1)) 
    
    #삭제하기
    if s - 1 > 0 and not visited[s-1][c]:
      visited[s-1][s] = True
      q.append((s-1, c, cnt+1)) 
bfs()
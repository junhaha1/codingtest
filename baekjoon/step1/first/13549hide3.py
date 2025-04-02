from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().rstrip().split())

dis = [0] * 100001
visited = [False] * 100001 

def bfs(s, e):
  q = deque()
  visited[s] = True
  q.append(s)
  
  while q:
    x = q.popleft()
    
    nx = [x + 1, x - 1, x * 2]
    
    if x == k:
      print(dis[k])
      return
    
    for i in range(len(nx)):
      if i == 2:
        cnt = 0
      else:
        cnt = 1
        
      if 0 <= nx[i] <= 100000:
        if visited[nx[i]] == False:
          dis[nx[i]] = dis[x] + cnt
          visited[nx[i]] = True
          q.append(nx[i])
        elif visited[nx[i]] == True and dis[nx[i]] > dis[x] + cnt:
          dis[nx[i]] = dis[x] + cnt
          q.append(nx[i])
          
bfs(n, k)
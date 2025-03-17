from sys import stdin
from collections import deque

n, k = map(int, input().rstrip().split())

dist = [0] * 100001
move = [0] * 100001

def path(x):
  arr = []
  temp = x
  for _ in range(dist[x] + 1):
    arr.append(temp)
    temp = move[temp]
  print(*arr[::-1])
 
def bfs():
  queue = deque()
  queue.append(n)
  while queue:
    x = queue.popleft()
    
    if x == k:
      print(dist[x])
      path(x)
      return x
    
    for i in (x+1, x-1, x*2):
      if 0<= i <=100000 and dist[i] == 0:
        dist[i] = dist[x] + 1
        queue.append(i)
        move[i] = x
bfs()
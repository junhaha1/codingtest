from collections import deque

def solution(maps):
  def bfs(a, b):
    q = deque()
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    q.append((a, b))
    
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    visited[a][b] = True
    
    while q:
      ox, oy  = q.popleft()
      
      if visited[len(maps)-1][len(maps[0])-1]:
        return maps[len(maps)-1][len(maps[0])-1]
      
      for i in range(4):
        nx = ox + dx[i]
        ny = oy + dy[i]
        if 0 <= nx < len(maps) and 0<= ny < len(maps[0]) and maps[nx][ny] != 0 and not visited[nx][ny]:
          maps[nx][ny] = maps[ox][oy] + 1
          visited[nx][ny] = True
          q.append((nx, ny))
    return - 1 
  
  answer = bfs(0, 0)
  return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
from collections import deque

def solution(n, wires):
  graph = [[] for _ in range(n+1)]
  
  for wire in wires:
    s, e = wire
    graph[s].append(e)
    graph[e].append(s)
    
  def bfs(s):
    visited = [True] + [False] * (n)
    q = deque()
    visited[s] = True
    cnt = 1
    q.append(s)
    
    while q:
      p = q.popleft()
      for c in graph[p]:
        if visited[c] == False:
          visited[c] = True
          cnt += 1
          q.append(c)
    return cnt
  
  result = int(1e9)
  for wire in wires:
    a, b = wire
    graph[a].remove(b)
    graph[b].remove(a)
    
    result = min(abs(bfs(a) - bfs(b)), result)
    
    graph[a].append(b)
    graph[b].append(a)

  return result
  

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
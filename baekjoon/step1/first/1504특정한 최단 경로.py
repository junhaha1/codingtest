from sys import stdin
import heapq

input = stdin.readline

n, e = map(int, input().rstrip().split())

INF = int(1e9)
graph = [[] for _ in range(n+1)]

for _ in range(e):
  st, en, weight = map(int, input().split())
  graph[st].append((en, weight))
  graph[en].append((st, weight))
  
v1, v2 = map(int, input().split())

def dijkstra(start, target):
  distance = [INF] * (n + 1)
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    for node in graph[now]:
      cost = dist + node[1]
      if cost < distance[node[0]]:
        distance[node[0]] = cost
        heapq.heappush(q, (cost, node[0]))
  return distance[target]

result = []
sv1 = dijkstra(1, v1)
sv2 = dijkstra(1, v2)
v1v2 = dijkstra(v1, v2)
v1e = dijkstra(v1, n)
v2e = dijkstra(v2, n)

result.append(sv1 + v1v2 + v2e)
result.append(sv2 + v1v2 + v1e)

if min(result) >= INF:
  print(-1)
else:
  print(min(result))
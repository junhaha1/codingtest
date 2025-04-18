from sys import stdin
import heapq

n = int(input())
m = int(input())

INF = int(1e9)

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  s, e, w = map(int, input().rstrip().split())
  graph[s].append((e, w))
  
S, E = map(int, input().rstrip().split())

def dijkstra(start):
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
        
dijkstra(S)

print(distance[E])
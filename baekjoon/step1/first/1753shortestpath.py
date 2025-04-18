from sys import stdin
import heapq

input = stdin.readline

v, e = map(int, input().rstrip().split())
S = int(input())
INF = int(1e9)
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
  st, ed, w = map(int, input().rstrip().split())
  graph[st].append((ed, w))
  
def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for node in graph[now]:
      cost = dist + node[1]
      if cost < distance[node[0]]:
        distance[node[0]] = cost
        heapq.heappush(q, (cost, node[0]))

dijkstra(S)

for r in distance[1:]:
  if r == INF:
    print('INF')
  else:
    print(r)
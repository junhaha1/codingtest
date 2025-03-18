from sys import stdin
import heapq

input = stdin.readline

INF = int(1e9)

n, m, k, x = map(int, input().rstrip().split()) #도시 수, 도로 수, 거리 수, 출발 도시 번호

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    s, e = map(int, input().rstrip().split())
    graph[s].append((e, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(x)

non = True
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        non = False

if non:
    print(-1)
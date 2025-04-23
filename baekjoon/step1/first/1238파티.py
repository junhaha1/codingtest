from sys import stdin
import heapq

input = stdin.readline

N, M, X = map(int, input().rstrip().split())

INF = int(1e9)
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)] #X마을로 도착하는 마을들의 경로를 역방향으로 만듬. 

dist1 = [INF] * (N + 1) #다른 마을들이 X마을에 도착하는 최소 거리
dist2 = [INF] * (N + 1) #X마을에서 다른 마을들에 도착하는 최소 거리

for _ in range(M):
    st, ed, ct = map(int, input().rstrip().split()) #시작 노드,  도착 노드, 비용
    graph[st].append((ed, ct))
    reverse_graph[ed].append((st, ct))

def dijkstra(start, board, graph):
    q = []
    heapq.heappush(q,(0, start))
    board[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if board[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < board[node[0]]:
                board[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

dijkstra(X, dist1, graph)
dijkstra(X, dist2, reverse_graph)

result = 0
for i in range(1, N + 1):
    result = max(result, dist1[i] + dist2[i])

print(result)
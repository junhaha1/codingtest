from sys import stdin 

input = stdin.readline

n = int(input()) #도시 개수
m = int(input()) #버스의 개수
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n + 1)]
path = [[-1] * (n + 1) for _ in range(n + 1)]

#순회찾기
def find_k(start, end):
  if path[start][end] == -1:
    return []
  k = path[start][end]
  return find_k(start, k) + [k] + find_k(k, end)

for _ in range(m):
  a, b, c = map(int, input().rstrip().split())
  graph[a][b] = min(graph[a][b], c)

for i in range(1, n + 1):
  graph[i][i] = 0
    
#플로이드 워셜 구현
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      if graph[a][b] > graph[a][k] + graph[k][b]:
        graph[a][b] = graph[a][k] + graph[k][b]
        path[a][b] = k

#이 반복문을 통해 무조건 INF 값을 미리 0으로 만들어두기
for j in range(1, n + 1):
  for i in range(1, n + 1):
    if graph[i][j] == INF:
      graph[i][j] = 0

for i in range(1, n + 1):
  print(*graph[i][1:])

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if graph[i][j] == INF or graph[i][j] == 0:
      print(0)
      continue
    
    result = [i] + find_k(i, j) + [j]
    print(len(result), *result)
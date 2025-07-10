from collections import deque
def solution(n, edge):
    distance = [0] * (n + 1)
    visited = [False] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    def bfs(x):
        q = deque()
        q.append((x, 0))
        
        while q:
            node, count = q.popleft()
            
            if not visited[node]:
                visited[node] = True
                distance[node] = count
            
                for child in graph[node]:
                    if not visited[child]:
                        q.append((child, count + 1))
                    
    bfs(1)
    
    max_dis = max(distance)
    return distance.count(max_dis)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
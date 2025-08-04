from collections import deque
import sys 

input = sys.stdin.readline


def bfs(num):
    dir = [int(1e9)] * (N + 1)
    visited = [False] * (N + 1)

    #정점 num부터 출발
    q = deque()
    dir[num] = 0
    visited[num] = True
    for next, cost in graph[num]:
        dir[next] = cost
        visited[next] = True
        q.append(next)

    while q:
        node = q.popleft()
        for next, cost in graph[node]:
            if not visited[next]:
                visited[next] = True
                dir[next] = min(dir[next], dir[node] + cost)
                q.append(next)
    
    return dir

def far_node(dir):
    cost = 0
    num = None
    for i in range(1, N + 1):
        if cost < dir[i]:
            cost = dir[i]
            num = i
    
    return num

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N):
    temp = list(map(int, input().split()))
    node = temp[0]
    if len(temp) >= 4:
        info = temp[1:-1]
        for i in range(0, len(info), 2):
            next, cost = info[i], info[i + 1]
            graph[node].append((next, cost))

dir = bfs(1)
node = far_node(dir)
dir = bfs(node)

print(max(dir[1:]))
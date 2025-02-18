from collections import deque
f, s, g, u, d = map(int, input().split())

visited = [0 for _ in range(f + 1) ]

dy = [u, d * -1]

def bfs():
    queue = deque()
    visited[s] = 1
    queue.append(s)
    
    while queue:
        i = queue.popleft()
        if i == g:
            print(visited[i] - 1)
            return
        for j in range(2):
            new_i = i + dy[j]
            if 1 <= new_i <= f:
                if visited[new_i] == 0:
                    visited[new_i] = visited[i] + 1
                    queue.append(new_i)
    
    print('use the stairs')
    return 

bfs()
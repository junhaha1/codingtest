from collections import deque
def solution(n, m, hole):
    board = [[0] * n for _ in range(m)]
    visited = [[[0] * n for _ in range(m)] for _ in range(2)]
    
    for x, y in hole:
        board[y-1][x-1] = -1
    
    dis = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    jumps = [(2, 0), (-2, 0), (0, -2), (0, 2)]
    
    q = deque()
    q.append((0, 0, 1))
    visited[1][0][0] = True
    
    while q:
        ox, oy, t = q.popleft()
        if ox == m-1 and oy == n-1:
            return visited[t][ox][oy]-1
        
        for d in dis:
            nx = ox + d[0]
            ny = oy + d[1]
            if 0<= nx < m and 0<= ny < n and board[nx][ny] == 0 and visited[t][nx][ny] == 0:
                visited[t][nx][ny] = visited[t][ox][oy] + 1
                q.append((nx, ny, t))
                
        if t > 0:
            for j in jumps:
                nx = ox + j[0]
                ny = oy + j[1]
                
                if 0<= nx < m and 0<= ny < n and board[nx][ny] == 0 and visited[t-1][nx][ny] == 0:
                    visited[t-1][nx][ny] = visited[t][ox][oy] + 1
                    q.append((nx, ny, t-1))
    return -1


print(solution(4, 4, [[2, 3], [3, 3]]))
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))
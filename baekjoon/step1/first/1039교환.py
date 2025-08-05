from collections import deque

N, K = map(int, input().split())

def bfs(start: str, K):
    q = deque()
    visited = [set() for _ in range(K + 1)]
    visited[0].add(start)
    num_list = list(start)
    q.append((num_list, 0))

    max_val = -1

    while q:
        num_list, count = q.popleft()
        if count == K:
            max_val = max(max_val, int(num_list))
            continue

        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):
                temp_list = list(num_list)
                temp_list[i], temp_list[j] = temp_list[j], temp_list[i]
                
                if temp_list[0] == '0': #맨 앞이 0이 존재할 수 없음.
                    continue
                
                temp = ''.join(temp_list)
                if temp not in visited[count + 1]:
                    visited[count + 1].add(temp)
                    q.append((temp, count + 1))
    
    return max_val


number = str(N)

if len(number) == 1:
    print(-1)
else:
    value = bfs(number, K)
    print(value)
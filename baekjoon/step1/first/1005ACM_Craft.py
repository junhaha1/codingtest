from sys import stdin
from collections import deque

input = stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())

    times = [0] + list(map(int, input().split())) #건물 건설 시간
    graph = [[] for _ in range(N + 1)] #인접 리스트
    in_degree = [0] * (N + 1)    #진입차수로 판단
    q = deque() 
    result =[]

    for _ in range(K):
        s, e = map(int, input().split())
        graph[s].append(e)
        in_degree[e] += 1
    
    for i in range(1, N + 1): #진입차수 0인거 큐에 삽입
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
                
    print(result)


    # print(graph)
    # print(in_degree)
    # print(q)

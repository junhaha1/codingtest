from collections import deque

N, M = map(int, input().split())

dag = [[] for _ in range(N + 1)]

in_degree = [0] * (N + 1)

for _ in range(M):
    st, ed = map(int, input().split())
    dag[st].append(ed)

    in_degree[ed] += 1

q = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

while q:
    k = q.popleft()
    for t in dag[k]:
        in_degree[t] -= 1
        if in_degree[t] == 0:
            q.append(t)
    print(k, end=" ")
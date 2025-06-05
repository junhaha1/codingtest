import heapq

N, M = map(int, input().split())

flag = [False] * 101
pos = [[] for _ in range(101)]

products = list(map(int, input().split()))

for i in range(M):
    pos[products[i]].append(i)

queue = []
result = 0
for p in products:
    if flag[p]:
        pos[p].pop(0)
    elif flag[p] == False and len(queue) >= N:
        temp = -1
        idx = -1
        for i in range(N):
            if not pos[queue[i]]:
                idx = i
                break
            elif pos[queue[i]] and pos[queue[i]][0] > temp:
                temp = pos[queue[i]][0]
                idx = i
        
        pos[p].pop(0)
        flag[p] = True
        flag[queue[idx]] = False

        queue[idx] = p
        result += 1
    elif flag[p] == False and len(queue) < N:
        pos[p].pop(0)
        flag[p] = True
        queue.append(p)

print(result)
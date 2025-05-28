import heapq

N, K = map(int,input().split())
objs = []
bags = []
heap = []
for _ in range(N):
    w, v = map(int, input().split())
    objs.append([w, v])

for _ in range(K):
    s = int(input())
    bags.append(s)
    
objs.sort()
bags.sort()

result = 0
idx = 0
for bag in bags:
    
    while idx < N and objs[idx][0] <= bag:
        heapq.heappush(heap, -objs[idx][1])
        idx += 1
    
    if heap:
        result -= heapq.heappop(heap)
    
print(result)
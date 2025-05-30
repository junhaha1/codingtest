import heapq

N = int(input())

lec = [tuple(map(int, input().split())) for _ in range(N)]
lec.sort()

heap = [lec[0][1]]

for i in range(1, N):
    if lec[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap,lec[i][1])
    else:
        heapq.heappush(heap,lec[i][1])

print(len(heap))
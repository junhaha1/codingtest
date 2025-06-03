import heapq
N = int(input())

q = []

for _ in range(N):
    dead, noodle = map(int, input().split())
    heapq.heappush(q, (dead, noodle))

result = []
while q:
    dead, noodle = heapq.heappop(q)
    if len(result) < dead:
        heapq.heappush(result, noodle)
    else:
        heapq.heappop(result)
        heapq.heappush(result, noodle)

print(sum(result))

import sys
import heapq

input = sys.stdin.readline

N = int(input())

left = [] #중앙값 이하인 수
right = [] #중앙값 초과인 수

for _ in range(N):
    num = int(input())
    heapq.heappush(left, -num)

    #크기 비교를 통한 오름차순 유지
    if right and -left[0] > right[0]:
        max_left = -heapq.heappop(left)
        min_right = heapq.heappop(right) 

        heapq.heappush(left, -min_right)
        heapq.heappush(right, max_left)
    
    #균형 유지하기
    if len(left) - len(right) > 1:
        heapq.heappush(right, -heapq.heappop(left))
    
    print(-left[0])
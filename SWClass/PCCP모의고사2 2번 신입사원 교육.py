import heapq

def solution(ability, number):
    heapq.heapify(ability)
    for i in range(number):
      p1 = heapq.heappop(ability)
      p2 = heapq.heappop(ability)
      
      print(p1, p2)
      p3 = p1 + p2
      
      heapq.heappush(ability, p3)
      heapq.heappush(ability, p3)
    return sum(ability)
  
print(solution([1, 2, 3, 4], 3))
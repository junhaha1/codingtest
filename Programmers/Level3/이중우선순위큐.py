import heapq
def solution(operations):
    
    max_heap = []
    min_heap = []
    
    for oper in operations:
        c, num = oper.split()
        
        if c == 'I': #삽입
            heapq.heappush(max_heap, int(num) * -1)
            heapq.heappush(min_heap, int(num))
            
        elif c == 'D': #삭제
            value = 0
            if len(max_heap) > 0 and int(num) == 1: #최대값 삭제
                value = heapq.heappop(max_heap) 
                min_heap.remove(value * -1)
                heapq.heapify(min_heap)
                
            elif len(min_heap) > 0 and int(num) == -1: #최소값 삭제
                value = heapq.heappop(min_heap) 
                max_heap.remove(value * -1)
                heapq.heapify(max_heap)
    
    if len(max_heap) > 0 and len(min_heap) > 0:
        return [max_heap[0] * -1, min_heap[0]]
    else:
        return [0, 0]
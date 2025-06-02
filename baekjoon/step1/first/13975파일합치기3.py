import heapq

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    heapq.heapify(nums)

    print(nums)

    result = 0
    while len(nums) > 1:
        value = heapq.heappop(nums) + heapq.heappop(nums)
        result += value
        heapq.heappush(nums, value)

    print(result)
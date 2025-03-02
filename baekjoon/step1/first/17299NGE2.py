from sys import stdin

cn = [0] * 1000001
input = stdin.readline
n = int(input())

nums = list(map(int, input().split()))

result = [-1] * n
stack = []

for i in nums:
    cn[i] += 1
    
for i in range(n):
    while stack and cn[nums[i]] > cn[nums[stack[-1]]]:
        result[stack[-1]] = nums[i]
        stack.pop()
    stack.append(i)
    
print(*result)
from sys import stdin
from collections import deque

#단조스택
#인덱스로 접근

input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))

result = [-1] * n
stack = []

for i in range(n):
    while stack and nums[i] > nums[stack[-1]]:
        result[stack[-1]] = nums[i]
        stack.pop()
    stack.append(i)
    
print(*result)

    
        
        
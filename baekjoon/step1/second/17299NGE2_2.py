from sys import stdin

input = stdin.readline

n = int(input().rstrip())
result = [-1] * n

nums = list(map(int, input().rstrip().split()))
cnt = [0] * 1000001
stack = []

for j in nums:
    cnt[j] += 1

for i in range(n):
    while stack and cnt[nums[stack[-1]]] < cnt[nums[i]]:
        result[stack[-1]] = nums[i]
        stack.pop()

    stack.append(i)

print(*result)
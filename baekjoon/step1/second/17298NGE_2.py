from sys import stdin

input = stdin.readline

n = int(input())
num = list(map(int, input().rstrip().split()))
result = [-1] * n

stack = []

for i in range(len(num)):
    while stack and num[stack[-1]] < num[i]:
        result[stack[-1]] = num[i]
        stack.pop()

    stack.append(i)

print(*result)

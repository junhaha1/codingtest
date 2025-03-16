from sys import stdin

input = stdin.readline

n = int(input())
ts = list(map(int, input().split()))

result = [0] * n
stack = [n-1]

for i in range(n-2,-1,-1):
    while stack and ts[i] > ts[stack[-1]]:
        result[stack[-1]] = i + 1
        stack.pop()
    stack.append(i)

print(*result)
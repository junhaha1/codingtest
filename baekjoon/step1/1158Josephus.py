from sys import stdin
from collections import deque
input = stdin.readline

n, k = map(int, input().split())

num = deque([i + 1 for i in range(n)])

result = '<'
i = 1
while num:
    if i % k == 0:
        result += str(num.popleft())
        if len(num) != 0:
            result += ', '
    else:
        num.append(num.popleft())
    i += 1

print(result + '>')

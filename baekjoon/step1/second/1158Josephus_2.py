from sys import stdin
from collections import deque

n, k = map(int, input().rstrip().split())
queue = deque([i for i in range(1, n + 1)])

cnt = 1

result = []

while queue:
    num = queue.popleft()
    if cnt % k == 0:
        result.append(str(num))
    else:
        if queue:
            queue.append(num)
        else:
            result.append(str(num))
    cnt += 1

print('<' + ', '.join(result) + '>')
    
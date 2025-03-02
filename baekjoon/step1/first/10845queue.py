from collections import deque
from sys import stdin

input = stdin.readline

queue = deque()
command = int(input())

for _ in range(command):
    m = input().rstrip()
    if "push" in m:
        m, i = m.split()
        queue.append(int(i))
    elif m == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif m == "size":
        print(len(queue))
    elif m == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif m == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif m == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
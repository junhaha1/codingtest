from sys import stdin
from collections import deque

input = stdin.readline
deck = deque()

m = int(input())

for _ in range(m):
    c = input().rstrip()
    if "push_front" in c:
        c, n = c.split()
        deck.appendleft(int(n))
    elif "push_back " in c:
        c, n = c.split()
        deck.append(int(n))
    elif c == "pop_front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.popleft())
    elif c == "pop_back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop())
    elif c == "size":
        print(len(deck))
    elif c == "empty":
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif c == "front":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
    elif c == "back":
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[-1])
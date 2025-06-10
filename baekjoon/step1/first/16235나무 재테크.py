from sys import stdin
from collections import deque
input = stdin.readline

N, M, K = map(int, input().split())

board = [[5] * N for _ in range(N)]
extra = [list(map(int, input().split())) for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

count = 0

for _ in range(M):
    x, y, num = map(int, input().split())
    trees[x-1][y-1].append(num)
    count += 1

def add_extra(): #양분 주기
    for r in range(N):
        for c in range(N):
            board[r][c] += extra[r][c]

for _ in range(K): #주어진 K년 만큼 반복
    grows = []
    #봄, 여름
    for r in range(N):
        for c in range(N):
            dead = 0
            new_tree = deque()
            for age in trees[r][c]:
                if board[r][c] >= age:
                    board[r][c] -= age
                    new_tree.append(age + 1)
                    if (age + 1) % 5 == 0:
                        for d in dir:
                            nr = r + d[0]
                            nc = c + d[1]
                            if 0 <= nr < N and 0 <= nc < N:
                                grows.append((nr, nc))
                else:  
                    dead += age // 2
                    count -= 1
            trees[r][c] = new_tree
            board[r][c] += dead

    #가을, 겨울
    for grow in grows:
        r, c = grow
        trees[r][c].appendleft(1)
        count += 1
    #겨울
    add_extra()

print(count)